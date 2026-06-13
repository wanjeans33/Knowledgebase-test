RAGBench: Explainable Benchmark for
Retrieval-Augmented Generation Systems
RobertFriel∗ MashaBelyi∗ AtindriyoSanyal
GalileoTechnologiesInc. GalileoTechnologiesInc. GalileoTechnologiesInc.
rob@rungalileo.io masha@rungalileo.io atin@rungalileo.io
Abstract
Retrieval-AugmentedGeneration(RAG)hasbecomeastandardarchitecturalpat-
ternforincorporatingdomain-specificknowledgeintouser-facingchatapplica-
tions powered by Large Language Models (LLMs). RAG systems are charac-
terized by (1) a document retriever that queries a domain-specific corpus for
context information relevant to an input query, and (2) an LLM that generates
a response based on the provided query and context. However, comprehen-
sive evaluation of RAG systems remains a challenge due to the lack of unified
evaluationcriteriaandannotateddatasets. Inresponse,weintroduceRAGBench:
thefirstcomprehensive, large-scaleRAGbenchmarkdatasetof100kexamples.
It covers five unique industry-specific domains and various RAG task types.
RAGBench examples are sourced from industry corpora such as user manuals,
makingitparticularlyrelevantforindustryapplications. Further,weformalizethe
TRACeevaluationframework: asetofexplainableandactionableRAGevalua-
tionmetricsapplicableacrossallRAGdomains. Wereleasethelabeleddataset
athttps://huggingface.co/datasets/rungalileo/ragbench. RAGBench
explainablelabelsfacilitateholisticevaluationofRAGsystems,enablingaction-
ablefeedbackforcontinuousimprovementofproductionapplications. Thorough
extensivebenchmarking,wefindthatLLM-basedRAGevaluationmethodsstrug-
gletocompetewithafinetunedRoBERTamodelontheRAGevaluationtask. We
identifyareaswhereexistingapproachesfallshortandproposetheadoptionof
RAGBenchwithTRACetowardsadvancingthestateofRAGevaluationsystems.
1 Introduction
Despiteremarkablereasoningandconversationalabilities,out-of-the-boxpre-trainedLargeLanguage
Models(LLMs)struggletoreasonaboutout-of-domain,knowledge-intensivequeries[20,13]. In
response, Retriever-Augmented Generation (RAG) systems [20, 19] are becoming increasingly
popular in user-facing dialogue applications [34]. Generally, RAG systems comprise a retriever
component that queries relevant documents from an in-domain corpus and a downstream LLM
generatormodelthatincorporatestheretrieveddocumentsalongwiththeoriginaluserquerytooutput
aninformedresponse. TheadditionalcontexthelpsgroundtheLLMinfactualinformationandhas
beenshowntoboostperformanceonknowledge-intensivetasks[20].
Still,whenusedinproductionsettings,RAGsystemsarepronetohallucinationsasthegenerator
model struggles to retrieve relevant information from the context [1, 30, 7]. In the absence of a
one-fits-allapproach,application-specificRAGsystemsmustbefine-tunedforoptimalperformance
ondomain-specifictasks. However,thechoiceofretrieverandgeneratormodelsforeachapplication
is complex and has serious implications on overall system quality and costs. With numerous
*EqualContributions
Preprint.Underreview.
5202
naJ
61
]LC.sc[
2v50011.7042:viXra

commercialandopen-sourcegenerativeLLMsreadilyavailable1andmanyvariableparametersinthe
RAGsystemdesign(Figure1),tuninganoptimalsystemforaparticularRAGapplicationinvolves
iterativeevaluationofmultipleconfigurations. ThismotivatestheneedforautomatedRAGevaluation
solutions.
Inresponse,automatedRAGevaluationsystemslikeRAGAS[9]andTruLens[36]haveemerged.
These systems adopt a zero-shot LLM prompt-based approach to predict a set of curated RAG
evaluationmetrics. However, thelackofunifiedRAGbenchmarksmakesitdifficulttocompare
approachesagainsteachother. Eachnewstudydesignsanewdataset,oftenemployingLLMsas
generatorsandlabelers[9,32,4],whichrendersthemirreproducible. AfewbenchmarkslikeRGB
[4],AttributionBench[22]andRAGTruth[40]havebeenproposedrecently,buttheyaresmallin
sizeandtargetadisjointsetoflabels. TheexactRAGevaluationcriteriaalsovaryfromstudyto
study. ARES[32]andRAGAS[9]defineacontextrelevancemetrictoevaluatethequalityofthe
retrieved documents, along with answer relevance and faithfulness to evaluate the quality of the
generativemodel. However,othershaveexploredothermetricslikecorrectness[1]noiserejection
and robustness [4], to name a few. Finally, most studies evaluate on small in-domain evaluation
datasetsthatarespecifictoeachnewapplication[32,33,9,1,4],leavingcross-domaingeneralization
anopenquestion.
In this work we propose RAGBench: a comprehensive dataset for training and benchmarking
RAG evaluation models. RAGBench comprises data sourced from multiple domains along with
acomprehensivesuiteofevaluationmetrics. Specifically,weadoptexistingmetricdefinitionsfor
contextrelevance,answerfaithfulness[9,32]andintroducetwonewmetrics: contextutilizationand
answercompleteness. WearguethatthisnewsuiteofmetricsbetterdescribestheoverallRAGsystem
performance,withthepotentialtoprovidegranular,actionableinsightstotheRAGpractitioner.
Weevaluatestate-of-theartLLMsandexistingRAGevaluationsystemsonRAGBench. Wefindthat
a400M-parameterDeBERTa-largemodelthatwasfine-tunedonRAGBenchoutperformsfew-shot
LLMjudgesacrossnumerousdomainsandtasktypes. Wehighlightthisresulttomotivatefuture
workaimedatleveragingthesedataforadvancingRAGevaluationmodelsandimprovingonthe
proposedbenchmark.
2 RelatedWork
Wedifferentiateourworkfromexistingground-truthRAGdatasetslikeChatRAGBench[23],CRAG
[41],DomainRAG[38],andALCE[10]. ThesedatasetscontainRAGsampleswithground-truth
responsesandareusedforend-to-endevaluationofRAGsystemsviaresponse-levelmetricslike
exactmatchorROUGEscores. Incontrast,wedesignRAGBenchtoenabledevelopmentofmore
matureevaluationsystemsthateffectivelyevaluatedifferentpartsoftheRAGsystemalongmultiple
dimensionslikeretrieverrelevance,adherenceandcompletenessoftheresponse.
VariousRAGbenchmarksfocusspecificallyonhallucinationdetection[40,33,21,5]. FELM[5]
is a multi-domain and task dataset with factuality labels for open domain QA. RAGTruth [40],
DelucionQA[33],andHaluEval[21]areRAG-specificdatasetswithbothsyntheticaswellashuman-
annotatedlabelsforhallucinationsinLLMreseponses. Whiletheseareappropriatebenchmarksfor
hallucinationdetectionmodels,theydonotofferthelevelofgranularityweofferwithRAGBench
thatisnecessarytounderstandtheRAGsystemasawhole.
RAGevaluation Recently,severalparalleleffortshaveproposedapproachestoautomatedRAG
evaluation. InRAGAS[9],theauthorsqueryanLLM-judge(GPT-3.5)withacuratedpromptto
evaluatecontextrelevance,answerrelevanceandfaithfulnessofaRAGresponse. Next,Saad-Falcon
et al. [32] propose ARES, a framework for fine-tuning smaller NLI models to predict the same
metrics. Inparallel,Chenetal.[4]developaheuristicsystemtoprobeLLM’srobustnesstonoisyand
irrelevantcontextdocuments,andAdlakhaetal.[1]exploreheuristicalgorithmstoestimateRAG
correctnessandfaithfulness. ThelackofestablishedRAGbenchmarksmakesitdifficulttocompare
theseapproachesagainsteachother. WeaimtoaddressthislimitationbyintroducingRAGBench.
FinetunedRAGevaluationmodels Fine-tunedLLMjudgesareanotheracommonwaytoap-
proachtheLLMevaluationtask[16,44,40]. Anumberofstudiesalsoleveragesmall,fine-tuned
1https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
2

Figure1:RAGsystemworkflow,withhighlightedvariableparameters:(1)Contextformatandlength,
(2)retrievermodel,(3)numberofretrieveddocuments,and(4)generationmodel.
NaturalLanguageInference(NLI)modelsforRAGhallucinationdetection[2,22,32]. NLImodels
measurethedegreeofentailmentbetweenapremiseandahypothesis,whichhasbeensuccessfully
repurposedforevaluatingLLMresponseattributioninRAGsetting. Inthiswork,wetrainandevalu-
ateanNLImodelforRAGevaluationusingRAGBench. Thefine-tunedmodelnotonlyoutperforms
LLMjudgesinhallucination/attributiondetectionbutalsoexcelsonthenewRAGevaluationmetrics
wepropose.
3 RAGBenchConstruction
3.1 ComponentDatasets
RAGBenchisacollectionofreal-worlddatasetsthatspandifferentdomainsandRAGtasktypes.
Wesourcedatafromopen-bookQuestion-Answer(QA)datasets(CovidQA[26],PubmedQA[14],
HotpotQA[42],MSMarco[28],CUAD[12],EManual[27],TechQA[3],FinQA[6],TAT-QA[47],
ExpertQA[25],HAGRID[15]),aswellonethatwasspecificallyadaptedforRAG(DelucionQA[33]).
Wetransformall12componentdatasetstoastandardizedRAGformatwithconsistentannotations.
Tobestrepresentreal-worldRAGscenarios,wevaryanumberparameterstoconstructthebenchmark:
thesourcedomain,numberofcontextdocuments,contexttokenlength,andtheresponsegenerator
modelFigure1illustrateswherethesevariableparametersfallintheRAGpipeline.
SourceDomains RAGBenchcomprisesfivedistinctdomains: bio-medicalresearch(PubmedQA,
CovidQA),generalknowledge(HotpotQA,MSMarco,HAGRID,ExperQA),legalcontracts(CuAD),
customersupport(DelucionQA,EManual,TechQA),andfinance(FinBench,TAT-QA).Weselect
thesespecificdomainsbasedonavailabilityofdata,andapplicabilitytoreal-worldRAGapplications
acrossdifferentindustryverticals. Fordetaileddescriptionsofeachcomponentdatasource,referto
Appendix7.2.
ContextTokenLength ContexttokenlengthinRAGBenchrangesfrom100to11ktokens,which
wereportinTable1. Notably,CUADdocumentsfeaturelongcontextsofupto11ktokenseach,
comparedtotherelativelyshortcontextinPubMedQA.
Task Types We curate RAGBench to inlcude a variety of difficult RAG task types. Customer
supportdatasetssimulateacommonapplicationofRAGinindustrysettings. FinQAandTAT-QA
requirenumericalreasoningoverhybridtabularandtextdata. HotpotQA,CovidQA,andPubMedQA
necessitateretrievalandreasoningovermultiplecontextdocs. TheCUADdatasetisachallenging
additiontoRAGBenchforseveralreasons: (i)itrepresentsadifficultandhighly-specializedreal-
worlddomaininwhichof-the-shelfpre-trainedLLMmodelsstruggletoperformwell[24],and(ii)it
isequallychallenginginRAGcontextduetoverylongcontextlengthsoflegalcontractdocuments.
3

|             | Table1:    | RAGBenchcomponentdatasets. |            |        |             |       |
| ----------- | ---------- | -------------------------- | ---------- | ------ | ----------- | ----- |
|             |            | Document                   | Question   | doc    |             |       |
| Dataset     | Domain     |                            |            | #docs  | #Train #Dev | #Test |
|             |            | Source                     | Source     | length |             |       |
|             | biomedical | research                   | automated  |        |             |       |
| PubMedQA    |            |                            |            | 4 99   | 19.5k 2.5k  | 2.5k  |
|             | research   | abstracts                  | heuristics |        |             |       |
|             | biomedical | research                   |            |        |             |       |
| CovidQA-RAG |            |                            | expert     | 4 122  | 2.5k 534    | 492   |
|             | research   | papers                     |            |        |             |       |
|             | general    |                            | crowd-     |        |             |       |
| HotpotQA    |            | wikipedia                  |            | 4 126  | 3.7k 847    | 776   |
|             | knowledge  |                            | sourced    |        |             |       |
|             | general    |                            | user       |        |             |       |
| MSMarco     |            | webpages                   |            | 10 94  | 3.7k 790    | 839   |
|             | knowledge  |                            | webqueries |        |             |       |
generalknowl-
| HAGRID |     | wikipedia | expert | 3 153 | 2.0k 322 | 1.3k |
| ------ | --- | --------- | ------ | ----- | -------- | ---- |
edge
generalknowl-
| ExpertQA |     | googlesearch | expert | 3 548 | 1.6k 202 | 203 |
| -------- | --- | ------------ | ------ | ----- | -------- | --- |
edge
legal
| CUAD | legal |     | expert | 1 11k | 1.5k 506 | 508 |
| ---- | ----- | --- | ------ | ----- | -------- | --- |
contracts
customer
| DelucionQA |     | Jeepmanual | LLM | 3 296 | 1.5k 177 | 182 |
| ---------- | --- | ---------- | --- | ----- | -------- | --- |
support
customer
| EManual |     | TVmanual | annotator | 3 165 | 1k 132 | 132 |
| ------- | --- | -------- | --------- | ----- | ------ | --- |
support
customer
| TechQA |     | Technotes | techforums | 5 1.8k | 1.2k 302 | 310 |
| ------ | --- | --------- | ---------- | ------ | -------- | --- |
support
earning
| FinQA | finance |     | expert | 3 310 | 12k 1.7k | 2.2k |
| ----- | ------- | --- | ------ | ----- | -------- | ---- |
reports
financial
| TAT-QA | finance |     | expert | 5 96 | 26k 3.2k | 3.2k |
| ------ | ------- | --- | ------ | ---- | -------- | ---- |
reports
| Total |     |     |     |     | 78k 12k | 11k |
| ----- | --- | --- | --- | --- | ------- | --- |
QuestionSources Allcomponentdatasetsincludedomain-specificquestionsthatrepresentreal-
worlduserqueriesaboutvarioustopics. QuestionsforDelucionQA,HotpotQA,andEManualare
crowd-sourced;questionsforCovidQA,CUAD,HAGRID,ExpertQA,andFinQAarecomposedby
domainexperts;MSMarcoissourcedfromreal-worlduserwebsearchqueries;likewise,TechQA
questionsareuserqueriespostedonIBMtechnicalforums; PubMedQAistheonlydatasetwith
automatically-generatedquestionsfromresearcharticletitles.
ResponseGeneration ForeachcomponentdatasetwegenerateresponseswithLLMs. Exceptions
tothisareHAGRIDandExpertQAdatasets,whichcontainLLM-generatedresponsesintheoriginal
data. Tointroducevariabilityintothedataset,wegeneratetworesponsesperinputwithdifferent
modes: GPT-3.5(gpt-3.5-0125)andClaude3Haiku. Bothareproprietarymodelsthatareofferedat
areasonablepricepoint2,whichwebelievemakethemsuitablecandidatesforgeneratingreal-world
RAGresponses. ForCUADweonlygenerateresponseswithClaude3Haikuduetoprohibitively
longcontextlengthsthatexceedtheGPT-3.516ktokenlimit. Toencourageadiversedistribution
oflabelsinRAGBench,weuseabasicprompt(Appendix7.3)thatdoesnotexplicitlyrequirethe
modeltosticktotheprovidedcontextwhengeneratingtheresponse. Wesetthetemperatureto1.0
forgeneration.
DataSplits Wespliteachcomponentdatasetintotrain,validation,andtestsets,ensuringthereis
nooverlapinqueriesacrosssplitsfromthesamedatasource. RAGBenchtotals100ksamples,split
acrosstrain,validation,andtestsets. ComponentdatasetstatisticsarereportedinTable1.
3.2 TRACeEvaluationFramework
Weproposeasuiteoffourcomprehensivemetricstoevaluatethequalityoftheretrieverandthe
response generator components of RAG. An optimal RAG system must balance accuracy and
efficiency. Theretrievershouldpreciselyreturnallthenecessaryinformationtoaddresstheuser
2https://openai.com/api/pricing/,https://www.anthropic.com/api
4

Figure2: ExampleofRAGQuestion,Context,andResponse. Relevantcontextspansarehighlighted,
andutilizedspansareunderlined.
query,avoidinganysuperfluousdata. Thegeneratormusteffectivelyutilizetheretrievedinformation,
ensuringtheresponseisstrictlybasedontheprovidedcontextwithoutintroducinganyhallucinations
intheoutput.
Towardscomprehensiveevaluationoftheabovementionedcriteria,weintroducetheTRACeevalua-
tionframeworktomeasureuTilization,Relevance,Adherence,andCompletenessofaRAGsystem.
Utilization,Adherence,andCompletenessmeasurethequalityofthegenerator. Adherencehereis
synonymouswithpreviouslyproposedanswerfaithfullness,groundednes,andattribution,allterms
usedinliteraturetomeasurehowwellanLLMoutputadherestoasourceoffactualinformation.
Relevancemeasuresthequalityoftheretrieveroutputwithrespecttothequery. Belowweformalize
thedefinitionofeachmetric.
Definitions LetDbeasetofcontextdocuments{d ...d }retrievedforaRAGinputquery. We
|     |     | 1 n |     |     |
| --- | --- | --- | --- | --- |
defineasetofrelevanttokensind asR ={t ,...t }. R encodesinformationincontextdocument
|     | i i | 1 r i |     |     |
| --- | --- | ----- | --- | --- |
d thatisusefulforansweringthequery. Similarly,wedefineU ={t ,...t }asthesetofutilized
| i   |     |     | i 1 u |     |
| --- | --- | --- | ----- | --- |
tokens in document d , which reflect information that the generation model is using to produce
i
a response. Refer to Figure 2 for a visual representation of relevant and utilized spans. Len(x)
measuresthelengthofstringsinx,whichcanbeinterpretedascharacterlength,tokenlength,or
sentencelength. Forcalculatingground-truthmetrics,weemploysentence-length,sinceitalignsbest
withourannotationschema(Section3.4). However,tokenorcharacterlengthmayalsobesuitable
forotherusecases.
ContextRelevance ContextRelevanceisdefinedin[9,32]asthefractionoftheretrievedcontext
thatisrelevanttotheinputquery. Lowrelevancepointstoaninefficientretrieverthatsuppliesexcess
informationtothegenerationmodel. Longcontextinputsintothegeneratormayaccrueunnecessary
costs,aswellascompromisethequalityofthegeneratedoutput. Wemeasurerelevanceofcontext
documentd i as:
|     |                    | Len(R | )   |     |
| --- | ------------------ | ----- | --- | --- |
|     | documentrelevance= |       | i   | (1) |
|     |                    | Len(d | )   |     |
i
Example-levelrelevancecanbeaggregatedoverallcontextdocumentsintheexampleas:
|     |     | (cid:80)|D| | Len(R ) |     |
| --- | --- | ----------- | ------- | --- |
i
|     | examplerelevance= | i=1 |     | (2) |
| --- | ----------------- | --- | --- | --- |
(cid:80)|D|
Len(d i )
i=1
ContextUtilization ContextUtilizationisanewmetricintroducedinTRACe. Weaimtomeasure
thethefractionoftheretrievedcontextthatisusedbythegeneratortoproducetheresponse. Low
UtilizationincombinationwithlowRelevancepointstoagreedyretriever,whilelowUtilization
alonepointstoaweakgeneratorthatfailstoleveragetheprovidedcontextefficiently.Document-level
andexample-levelUtilizationaredefinedas:
(cid:80)|D|
|                      | Len(U | )                   | Len(U               | )   |
| -------------------- | ----- | ------------------- | ------------------- | --- |
|                      |       | i                   | i=1                 | i   |
| documentutilization= |       | exampleutilization= |                     | (3) |
|                      | Len(d | )                   | (cid:80) |D | Len(d | )   |
|                      |       | i                   | i =1                | i   |
Completeness Completenessisanothernewmetricsweintroducetomeasurehowwelltheresponse
incorporatesalltherelevantinformationinthecontext. NotethatthisisdifferentfromUtilization;it
ispossibletohavehighRelevanceandhighUtilization,butlowCompletenesswhenthegenerator
5

Figure3: Distributionsofrelevance,utilization,andcompletenesslabelsinRAGBench. Y-axisis
normalizedtovisualizedensities.
utilizesirrelevantinformationinthecontexttoproducealowqualityresponse. Completenessfor
documentd iscalculatedasthefractionofutilizedsubstringsamongallrelevantsubstrings:
i
Len(R ∩U )
completeness= i i (4)
Len(R )
i
Andcanbeextendedtoexample-levelbyconsideringallrelevantandutilizedsubstringsacrossall
contextdocuments.
Adherence AdherenceisdesignedtodetecthallucinationsinRAGresponses. Ourdefinitionof
Adherenceissynonymouswithanswerfaithfullness[9,32],groundednes[36],andattribution[31].
Foralignmentwithexistinghallucinationdetectionapproaches,wedefineexample-leveladherence
asabooleanindicatingwhetherornotallpartsoftheresponsearegroundedinthecontext. However,
inourannotationschema(Section3.4)wealsodefineA ={t ,...t }asthesetofresponsetokens
i 1 a
thataresupportedbythecontexttoenablegranularAdherenceevaluation.
3.3 RAGBenchStatistics
RAGBenchcomponentdatasetscontainbetween1%-20%hallucinations. ExpertQA,CovidQA,and
MSMarcocontainthehighestfractionofhallucinatedresponses(12%,16%,and13%,respectively),
whileCuad,FinQA,andTAT-QAcontaintheleast(about1%foreach). Wevisualizedistributionsof
relevance,utilization,andcompletenessscoresinFigure3.
3.4 LLMannotator
We prompt GPT-4 (gpt-4-0125-preview) to produce ground truth Adherence, Relevance, and
Utilization labels for input (documents, query, response) tuples in RAGBench. Completeness is
easilyderivedfromspan-levelRelevanceandUtilizationannotations,thuswedon’trequestexplicit
annotationsforit.
Forhighqualitylabels,weuseproventechniqueslikechainofthought[39]thathavebeenshown
to maximize the correlation between GPT-4 and human judgements [43, 46]. For relevance and
utilizationwerequesttheLLM-annotatortodirectlyidentifyrelevantandutilizedsub-stringsinthe
inputdocuments. Foradherence,weinstructtheLLMtoidentifywhichresponsesentences,ifany,
aresupportedbytheprovidedcontext. Wecanthenderiveanexample-levelbooleanadherencelabel
bycheckingifallresponsesentencesaresupported. Theexactpromptusedforannotationisprovided
inAppendix7.4. Weapplypost-processingstepstoensurehighquality,reliableannotationsfromour
GPT-labeler,whichweoutlineinAppendix7.5.
AlignmentwithHumanJudgements Wevalidateourmetricformulationsandlabelingapproach
onahumanannotatedbenchmark. DelucionQA[33]isacuratedcollectionofuserqueriesonthe
operationofJeep’s2023Gladiatormodel. NaturallanguagequeriesarefirstgeneratedbyanLLM,
thenreviewedandfilteredbyhumanannotators.ContextdocumentsaresourcedfromJeep’sGladiator
UserManual, andresponsesaregeneratedbyvariousLLMs. Combinedwithexample-leveland
span-levelannotationsforhallucination,DelucionQArepresentsarealisticdistributionofreal-world
userqueriesandRAGresponses. WefindthatourGPTannotatorachieves93%and95%example-
andspan-levelagreementwithhumanjudgementsontheDelucionQAtestsplit(Table2).
6

Table 2: GPT-4 annotator achieves high alignment with human judgements. We report F1 and
AccuracyalignmentmetricsonhumanannotatedsubsetsofDelucionQA.Adherenceannotations
areevaluatedagainstDelucionQAhuman-annotatedlabels. RelevanceandUtilizationareevaluated
againstDelucionQA(40): asubsetof40examplesrandomlysampledfromtheDelucionQAtestset
andannotatedbytheauthors.
| TestSet                  | Metric      | F1 Accuracy |
| ------------------------ | ----------- | ----------- |
| DelucionQA-examplelevel  | Adherence   | 0.96 0.93   |
| DelucionQA-spanlevel     | Adherence   | 0.97 0.95   |
| DelucionQA(40)-spanlevel | Utilization | 0.92 0.94   |
| DelucionQA(40)-spanlevel | Relevance   | 0.76 0.78   |
(a)Retrievervs.Relevance (b)LLMvs.Hallucination
(c)Promptvs.Utilization (d)Promptvs.Completeness
Figure4: RelationshipbetweenRAGsystemconfigurationandTRACemetrics. (a)Thechoiceand
configurationofRAGretrievercomponentaffectstheaveragerelevanceoftheretrievedcontext. In
thisexample,adenseretrieverwithalownumberofdocumentsperquery(k=2)yieldsthehighest
averagecontextrelevance. (b)ThechoiceofLLMandgenerationpromptaffecthowwelltheRAG
systemutilizestheprovidedcontext. PromptingtheLLMwithadetailedchain-of-thoughtprompt
leadstoreducedhallucinations,aswellashigherresponseutilization(c)andcompleteness(d)rates.
Tovalidaterelevanceandutilizationannotations,wealsoannotateasmallsubsetofDelucionQA
withgranularrelevanceandutilizationlabels. WerefertothissubsetasDelucionQA(40)inTable
2. Similartoadherence,weobservehighcorrelationbetweenrelevanceandutilizationjudgements
fromGPT-4andhumans. Detailsoftheannotationprocessandadditionalvalidationsarefoundin
Appendix7.6.
7

3.5 RAGCaseStudy
WedesignacasestudytofurthermotivateandvalidatetheproposedTRACeframework. Wesample
100realisticworldknowledgequeriesfromtheRAGTruth[40]QAtrainingset,alongwith2,512
uniquecontextdocumentchunksfromthesamedatasettouseasinputsintoourmockRAGsystems.
WesimulateRAGsetupsofvaryingqualitybycontrollingfourconfigurableparameters:theretriever
(sparseTF-IDFvs. dense),numberofretrieveddocuments(2vs. 4),generationmodel(GPT-3.5-
turbovs. GPT-4o),and4versionsofthegenerationprompttemplate. Forillustrativepurposes,
weevaluateoneprompttemplatecomprisingofonlythequestion(nocontext)vs. threeRAG-style
templatesthatencouragetheLLMtoutilizetheprovidedcontextand/orutilizechain-of-thought
(CoT).ThefullgenerationtemplatesareprovidedinAppendix7.7. Wegenerateresponsesforthe
100 RAGTruth queries with each of the 32 resulting RAG systems and use our LLM annotation
prompttoevaluatetheTRACemetrics.
Figure4demonstrateshowthedifferentRAGconfigurationsinfluenceTRACemetrics. Forexample,
weconfirmthatthechoiceofthegenerativeLLMmodelaffectstheamountofhallucinations(or
non-adherentresponses)inthegeneratedtext. Notsurprisingly,GPT-4ocombinedwithachain-of-
thoughtpromptyieldsthelowestamountofhallucinationcomparedtotheweakerGPT-3.5model
andlessdetailedprompts. Curiously,wefindthatGPT-3.5hallucinatesmorewhenpromptedwith
CoT,whichmaypointtolimitationsinthemodel’sabilitytoreasonaboutcomplexconcepts4b.
Overall,wefindthatpromptingtheLLMtothinkstep-by-stepandexplainitsreasoningleadsto
higherutilizationoftheprovidedcontextandmorecompleteresponses(4c,4d). Finally,weshow
thatthechoiceoftheretrieveraffectsaveragerelevanceoftheretrievedcontextdocumentsperquery
4a.
4 Experiments
4.1 LLMJudge
WebenchmarksafewLLMevaluatorsonRAGBench: (1)zero-shotGPT-3.5-judge,wherewequery
GPT-3.5withourannotationprompt, (2)RAGAS[9], and(3)TruLens[36]. RAGASemploysa
seriesoffew-shotpromptstoGPT-3.5tomeasureanswergroundedness(Adherence)andContext
Relevancemetrics.Trulensisanotherzero-shotpromptingapproachthatmeasuresanswerfaithfulness
(Adherence)andContextRelevance.
4.2 Fine-tunedJudge
We fine-tune a DeBERTa-v3-Large [11] NLI checkpoint3 from Laurer et al. [18] with one key
architecturemodification: weaddashallowpredictionheadforeachoftheoutputRAGmetrics,
whichallowsustocomputeallTRACemetricsinasingleforwardpass. Thisisbothcost-effective
andenablestransferlearningfromheadtoheadthroughback-propagationdowntothesharedbase
layers. Eachpredictionheadisasinglelayerfeed-forwardnetthatactsonthetoken-leveloutputof
thelastDeBERTalayer.
WeattachtwoheadsonthecontexttokenstoestimateRelevanceandUtilizationprobabilities,and
anotherheadontheresponsetokenstoestimateAdherence. Fortraining,webroadcastsentence-level
annotations to tokens, and tune to maximize token-level probabilities of Relevant, Utilized, and
Adherentspans. Atinference,weimposeaprobabilitythreshold=0.5topredictRelevantandUtilized
spansandAdherentspansandcalculateTRACemetricsusingequations2,3,and4. Forcomparison
withexistinghallucinationdetectionapproaches,wealsoaggregateAdherenceprobabilitiesacross
theentireresponsetoproduceanexample-levelresponseadherencelabel. Fordetailsabouttraining
andhyperparameters,refertoAppendix7.8.
4.3 Evaluation
Our granular annotation schema allows for various evaluation setups. For example, we could
evaluateeitherspan-levelorexample/response-levelpredictions. Foreasycomparisonwithexisting
RAGevaluationapproachesthatarelessgranular,wereportareaunderthereceiver-operatorcurve
3https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli
8

Table3:Benchmarkevaluationontestsplits.ReportingAUROCforpredictinghallucinatedresponses
(Hal), RMSEforpredictingContextRelevance(Rel)andutilization(Util). ∗ indicatesstatistical
significanceat95%confidenceintervals,measuredbybootstrapcomparingthetopandsecond-best
results. RAGASandTrulensdonotevaluateUtilization.
GPT-3.5 RAGAS TruLens DeBERTA
Dataset Hal↑ Rel↓ Util↓ Hal↑ Rel↓ Util↓ Hal↑ Rel↓ Util↓ Hal↑ Rel↓ Util↓
PubMedQA 0.51 0.21∗ 0.16 0.54 0.37 - 0.62 0.45 - 0.80∗ 0.26 0.17
CovidQA-RAG 0.57 0.18 0.11 0.58 0.17 - 0.62 0.58 - 0.77∗ 0.19 0.11
HotpotQA 0.59 0.11 0.08 0.62 0.14 - 0.64 0.73 - 0.85∗ 0.11 0.08
MSMarco 0.65 0.23 0.11 0.63 0.25 - 0.62 0.61 - 0.70 0.22 0.10
HAGRID 0.58 0.22 0.15 0.62 0.22 - 0.67 0.69 - 0.81∗ 0.20∗ 0.13
ExpertQA 0.55 0.31 0.23 0.57 0.28 - 0.70 0.60 - 0.87∗ 0.18∗ 0.11∗
DelucionQA 0.57 0.18 0.10 0.70∗ 0.22 - 0.55 0.64 - 0.64 0.15∗ 0.10
EManual 0.54 0.17 0.11∗ 0.57 0.27 - 0.61 0.64 - 0.76∗ 0.13∗ 0.13
TechQA 0.51 0.10 0.05 0.52 0.12 - 0.57 0.70 - 0.86∗ 0.08∗ 0.04∗
FinQA 0.57 0.10 0.13 0.57 0.06∗ - 0.53 0.79 - 0.81∗ 0.10 0.10
TAT-QA 0.52 0.20 0.17∗ 0.63 0.18∗ - 0.59 0.72 - 0.83∗ 0.27 0.23
CUAD 0.51 0.27 0.11 0.66 0.19∗ - 0.40 0.66 - 0.80∗ 0.24 0.10
(AUROC)ontheresponse-levelhallucinationdetectiontask,androotmeansquarederror(RMSE)
forexample-levelcontextRelevanceandUtilizationpredictions.
5 Results
Table3reportsresultsontestsplitsofeachRAGBenchcomponentdataset. Wecomparebaseline
LLMmethodswithafinetunesDeBERTAencoderthattrainedonthefullRAGBenchtrainsplit.
WeobservethatthefinetunedDeBERTamodeltrainedonRAGBenchachievescompetitiveperfor-
mancewithbillion-parameterLLMjudgesacrossnumerousdomainsubsetsoftheRAGBenchtest
set. Onthehallucinationdetectiontask,DeBERTAAUROCscoresrangefrom0.64to0.86. While
RMSEforrelevanceandutilizationrangefrom0.04to0.26,dependingonthedomainandtask.
EstimatingContextRelevanceisDifficult AsshowninTable3, RelevanceRMSEscoresare
generallyhigherthanthoseforUtilization,indicatingagreaterdifficultyintherelevanceprediction
task. Utilizationcanbeassessedthroughastraightforwardsemanticcomparisonbetweenthecontext
andtheresponse. Incontrast,relevanceisamoreintricatemetric. DuetothenatureofRAG,the
majority of retrieved documents are semantically related to the query. However, mere semantic
similarityisinsufficient. Themodelmustascertainwhethertheprovidedcontextincludesspecific
informationnecessarytoaccuratelyanswerthequestion. Thus,thetaskinherentlyinvolvesderiving
thecorrectanswer,followedbyassessingwhatinformationinthecontextmaybeusedtoarriveat
thatanswer.
6 Conclusion
InthispaperweintroduceRAGBench,alarge-scaledatasetcomposedofreal-worldRAGexamples
intendedfortrainingandbenchmarkingpowerfulRAGevaluationmodels. Tothisend,weformulate
TRACe,aRAGevaluationframeworkcomprisingfourmetrics: uTilization,Relevance,Adherence,
andCompleteness. TRACestandardizestheevaluationprocess,offeringaconsistentandsystem-
aticapproachtomeasuringRAGsystemperformanceacrossvariousdimensions. Weproposean
automatedapproachtogenerateTRACelabelsforRAGBenchwithanLLManddemonstratehigh
correlationbetweenourapproachandhumanjudgements.
WebenchmarkexistingRAGevaluationframeworksonRAGBenchanddemonstratethata400M
parameter DeBERTa model finetuned on RAGBench data performs competitively with billion-
9

parameter LLM Judges and commercial RAG evaluation systems. Though, the gap between the
best-performingRAGevaluatorandgroundtruthisstilllarge. Wemotivatefutureworktoleverage
RAGBenchtowardfine-tuningmorepowerfulevaluationmodelstoexplorethepotentialfornarrowing
theperformancegapbetweenthesemodelsandthegroundtruth.
Ourcontributionsaddresstheneedforstandardizedbenchmarksandmethodologies,enablingmore
preciseandactionableinsightsintothestrengthsandweaknessesofdifferentRAGsystems. This,
in turn, will facilitate iterative improvement of RAG models, driving forward the capabilities of
retrieval-augmentedgenerationinreal-worldapplications.
References
[1] V. Adlakha, P. BehnamGhader, X. H. Lu, N. Meade, and S. Reddy. Evaluating correct-
nessandfaithfulnessofinstruction-followingmodelsforquestionanswering. arXivpreprint
arXiv:2307.16877v1,2023.
[2] B.Bohnet,V.Q.Tran,P.Verga,R.Aharoni,D.Andor,L.B.Soares,M.Ciaramita,J.Eisenstein,
K. Ganchev, J. Herzig, K. Hui, T. Kwiatkowski, J. Ma, J. Ni, L. S. Saralegui, T. Schuster,
W.W.Cohen,M.Collins,D.Das,D.Metzler,S.Petrov,andK.Webster. Attributedquestion
answering: Evaluationandmodelingforattributedlargelanguagemodels,2023.
[3] V.Castelli,R.Chakravarti,S.Dana,A.Ferritto,R.Florian,M.Franz,D.Garg,D.Khandelwal,
S. McCarley, M. McCawley, M. Nasr, L. Pan, C. Pendus, J. Pitrelli, S. Pujar, S. Roukos,
A. Sakrajda, A. Sil, R. Uceda-Sosa, T. Ward, and R. Zhang. The TechQA dataset. In
D. Jurafsky, J. Chai, N. Schluter, and J. Tetreault, editors, Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 1269–1278, Online, July
2020.AssociationforComputationalLinguistics. doi: 10.18653/v1/2020.acl-main.117. URL
https://aclanthology.org/2020.acl-main.117.
[4] J. Chen, H. Lin, X. Han, and L. Sun. Benchmarking large language models in retrieval-
augmentedgeneration. arXivpreprintarXiv:2309.01431,2023.
[5] s. chen, Y. Zhao, J. Zhang, I.-C. Chern, S. Gao, P. Liu, and J. He. Felm: Bench-
marking factuality evaluation of large language models. In A. Oh, T. Naumann,
A. Globerson, K. Saenko, M. Hardt, and S. Levine, editors, Advances in Neural
Information Processing Systems, volume 36, pages 44502–44523. Curran Associates,
Inc.,2023. URLhttps://proceedings.neurips.cc/paper_files/paper/2023/file/
8b8a7960d343e023a6a0afe37eee6022-Paper-Datasets_and_Benchmarks.pdf.
[6] Z. Chen, W. Chen, C. Smiley, S. Shah, I. Borova, D. Langdon, R. Moussa, M. Beane, T.-
H. Huang, B. Routledge, and W. Y. Wang. FinQA: A dataset of numerical reasoning over
financialdata. InM.-F.Moens,X.Huang,L.Specia,andS.W.-t.Yih,editors,Proceedings
ofthe2021ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages3697–
3711,OnlineandPuntaCana,DominicanRepublic,Nov.2021.AssociationforComputational
Linguistics. doi: 10.18653/v1/2021.emnlp-main.300. URLhttps://aclanthology.org/
2021.emnlp-main.300.
[7] S. Chiesurin, D. Dimakopoulos, M. A. Sobrevilla Cabezudo, A. Eshghi, I. Papaioannou,
V.Rieser,andI.Konstas. Thedangersoftrustingstochasticparrots: Faithfulnessandtrustin
open-domainconversationalquestionanswering. InA.Rogers,J.Boyd-Graber,andN.Okazaki,
editors,FindingsoftheAssociationforComputationalLinguistics: ACL2023,pages947–959,
Toronto,Canada,July2023.AssociationforComputationalLinguistics. doi: 10.18653/v1/2023.
findings-acl.60. URLhttps://aclanthology.org/2023.findings-acl.60.
[8] E. Dinan, S. Roller, K. Shuster, A. Fan, M. Auli, and J. Weston. Wizard of wikipedia:
Knowledge-poweredconversationalagents,2019.
[9] S. Es, J. James, L. Espinosa Anke, and S. Schockaert. RAGAs: Automated evaluation of
retrievalaugmentedgeneration. InProceedingsofthe18thConferenceoftheEuropeanChapter
of the Association for Computational Linguistics: System Demonstrations. Association for
ComputationalLinguistics,Mar.2024.
10

[10] T. Gao, H. Yen, J. Yu, and D. Chen. Enabling large language models to generate text with
citations. InH.Bouamor,J.Pino,andK.Bali,editors,Proceedingsofthe2023Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing,pages6465–6488,Singapore,Dec.2023.
Association for Computational Linguistics. doi: 10.18653/v1/2023.emnlp-main.398. URL
https://aclanthology.org/2023.emnlp-main.398.
[11] P. He, J. Gao, and W. Chen. DeBERTav3: Improving deBERTa using ELECTRA-style
pre-training with gradient-disentangled embedding sharing. In The Eleventh International
ConferenceonLearningRepresentations,2023. URLhttps://openreview.net/forum?
id=sE7-XhLxHA.
[12] D.Hendrycks,C.Burns,A.Chen,andS.Ball. Cuad: Anexpert-annotatednlpdatasetforlegal
contractreview. NeurIPS,2021.
[13] Y.HuangandJ.Huang. Asurveyonretrieval-augmentedtextgenerationforlargelanguage
models,2024.
[14] Q. Jin, B. Dhingra, Z. Liu, W. Cohen, and X. Lu. PubMedQA: A dataset for biomedical
researchquestionanswering. InK.Inui, J.Jiang, V.Ng, andX.Wan, editors, Proceedings
ofthe2019ConferenceonEmpiricalMethodsinNaturalLanguageProcessingandthe9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages
2567–2577,HongKong,China,Nov.2019.AssociationforComputationalLinguistics. doi:
10.18653/v1/D19-1259. URLhttps://aclanthology.org/D19-1259.
[15] E.Kamalloo,A.Jafari,X.Zhang,N.Thakur,andJ.Lin. Hagrid: Ahuman-llmcollaborative
datasetforgenerativeinformation-seekingwithattribution,2023.
[16] S.Kim,J.Suk,S.Longpre,B.Y.Lin,J.Shin,S.Welleck,G.Neubig,M.Lee,K.Lee,and
M.Seo.Prometheus2:Anopensourcelanguagemodelspecializedinevaluatingotherlanguage
models,2024.
[17] T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein,
I.Polosukhin,M.Kelcey,J.Devlin,K.Lee,K.N.Toutanova,L.Jones,M.-W.Chang,A.Dai,
J.Uszkoreit, Q.Le, andS.Petrov. Naturalquestions: abenchmarkforquestionanswering
research. TransactionsoftheAssociationofComputationalLinguistics,2019.
[18] M.Laurer,W.vanAtteveldt,A.Casas,andK.Welbers. Lessannotating,moreclassifying–
addressingthedatascarcityissueofsupervisedmachinelearningwithdeeptransferlearning
andbert-nli. OpenScienceFrameworkPreprint,2022. URLhttps://osf.io/74b8k.
[19] K.Lee,M.-W.Chang,andK.Toutanova. Latentretrievalforweaklysupervisedopendomain
questionanswering.InA.Korhonen,D.Traum,andL.Màrquez,editors,Proceedingsofthe57th
AnnualMeetingoftheAssociationforComputationalLinguistics,pages6086–6096,Florence,
Italy,July2019.AssociationforComputationalLinguistics. doi: 10.18653/v1/P19-1612. URL
https://aclanthology.org/P19-1612.
[20] P.Lewis,E.Perez,A.Piktus,F.Petroni,V.Karpukhin,N.Goyal,H.Küttler,M.Lewis,W.-t.
Yih,T.Rocktäschel,S.Riedel,andD.Kiela. Retrieval-augmentedgenerationforknowledge-
intensivenlptasks. InProceedingsofthe34thInternationalConferenceonNeuralInformation
Processing Systems, NIPS ’20, Red Hook, NY, USA, 2020. Curran Associates Inc. ISBN
9781713829546.
[21] J. Li, X. Cheng, X. Zhao, J.-Y. Nie, and J.-R. Wen. HaluEval: A large-scale hallucination
evaluationbenchmarkforlargelanguagemodels. InH.Bouamor,J.Pino,andK.Bali,editors,
Proceedingsofthe2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,
pages6449–6464,Singapore,Dec.2023.AssociationforComputationalLinguistics. doi: 10.
18653/v1/2023.emnlp-main.397. URL https://aclanthology.org/2023.emnlp-main.
397.
[22] Y. Li, X. Yue, Z. Liao, and H. Sun. Attributionbench: How hard is automatic attribution
evaluation? arXivpreprintarXiv:2402.15089v1,2024.
11

[23] Z.Liu,W.Ping,R.Roy,P.Xu,C.Lee,M.Shoeybi,andB.Catanzaro. Chatqa: Buildinggpt-4
levelconversationalqamodels. arXivpreprintarXiv:2401.10225,2024.
[24] V.Magesh,F.Surani,M.Dahl,M.Suzgun,C.D.Manning,andD.E.Ho. Hallucination-free?
assessingthereliabilityofleadingailegalresearchtools,2024.
[25] C.Malaviya,S.Lee,S.Chen,E.Sieber,M.Yatskar,andD.Roth. Expertqa: Expert-curated
questionsandattributedanswers,2024.
[26] T.Möller,A.Reina,R.Jayakumar,andM.Pietsch. COVID-QA:Aquestionansweringdataset
forCOVID-19. InProceedingsofthe1stWorkshoponNLPforCOVID-19atACL2020,Online,
July2020.AssociationforComputationalLinguistics. URLhttps://aclanthology.org/
2020.nlpcovid19-acl.18.
[27] A. Nandy, S. Sharma, S. Maddhashiya, K. Sachdeva, P. Goyal, and N. Ganguly. Question
answeringoverelectronicdevices: Anewbenchmarkdatasetandamulti-tasklearningbased
QAframework. InM.-F.Moens,X.Huang,L.Specia,andS.W.-t.Yih,editors,Findingsof
theAssociationforComputationalLinguistics: EMNLP2021,pages4600–4609,PuntaCana,
DominicanRepublic,Nov.2021.AssociationforComputationalLinguistics. doi: 10.18653/
v1/2021.findings-emnlp.392. URLhttps://aclanthology.org/2021.findings-emnlp.
392.
[28] T. Nguyen, M. Rosenberg, X. Song, J. Gao, S. Tiwary, R. Majumder, and
L. Deng. Ms marco: A human generated machine reading comprehension dataset.
November 2016. URL https://www.microsoft.com/en-us/research/publication/
ms-marco-human-generated-machine-reading-comprehension-dataset/.
[29] F. Petroni, A. Piktus, A. Fan, P. Lewis, M. Yazdani, N. De Cao, J. Thorne, Y. Jernite,
V. Karpukhin, J. Maillard, V. Plachouras, T. Rocktäschel, and S. Riedel. KILT: a bench-
markforknowledgeintensivelanguagetasks. InK.Toutanova,A.Rumshisky,L.Zettlemoyer,
D. Hakkani-Tur, I. Beltagy, S. Bethard, R. Cotterell, T. Chakraborty, and Y. Zhou, editors,
Proceedings of the 2021 Conference of the North American Chapter of the Association for
ComputationalLinguistics: HumanLanguageTechnologies,pages2523–2544,Online,June
2021.AssociationforComputationalLinguistics. doi: 10.18653/v1/2021.naacl-main.200. URL
https://aclanthology.org/2021.naacl-main.200.
[30] H. Rashkin, D. Reitter, G. S. Tomar, and D. Das. Increasing faithfulness in knowledge-
groundeddialoguewithcontrollablefeatures. InC.Zong,F.Xia,W.Li,andR.Navigli,editors,
Proceedingsofthe59thAnnualMeetingoftheAssociationforComputationalLinguisticsand
the 11th International Joint Conference on Natural Language Processing (Volume 1: Long
Papers),pages704–718,Online,Aug.2021.AssociationforComputationalLinguistics. doi:
10.18653/v1/2021.acl-long.58. URLhttps://aclanthology.org/2021.acl-long.58.
[31] H.Rashkin,V.Nikolaev,M.Lamm,L.Aroyo,M.Collins,D.Das,S.Petrov,G.S.Tomar,I.Turc,
andD.Reitter. Measuringattributioninnaturallanguagegenerationmodels. Computational
Linguistics,49(4):777–840,122023.
[32] J.Saad-Falcon,O.Khattab,C.Potts,andM.Zaharia.Ares:Anautomatedevaluationframework
forretrieval-augmentedgenerationsystems. arXivpreprintarXiv:2311.09476v2,2024.
[33] M.Sadat,Z.Zhou,L.Lange,J.Araki,A.Gundroo,B.Wang,R.Menon,M.Parvez,andZ.Feng.
Delucionqa: Detectinghallucinationsindomain-specificquestionanswering. pages822–835,
012023. doi: 10.18653/v1/2023.findings-emnlp.59.
[34] S. Siriwardhana, R. Weerasekera, E. Wen, T. Kaluarachchi, R. Rana, and S. Nanayakkara.
Improvingthedomainadaptationofretrievalaugmentedgeneration(RAG)modelsforopen
domainquestionanswering.TransactionsoftheAssociationforComputationalLinguistics,11:1–
17,2023. doi: 10.1162/tacl_a_00530. URLhttps://aclanthology.org/2023.tacl-1.1.
[35] J.Thorne,A.Vlachos,C.Christodoulopoulos,andA.Mittal. FEVER:alarge-scaledataset
forfactextractionandVERification. InM.Walker,H.Ji,andA.Stent,editors,Proceedings
ofthe2018ConferenceoftheNorthAmericanChapteroftheAssociationforComputational
Linguistics: HumanLanguageTechnologies,Volume1(LongPapers),pages809–819,New
12

Orleans,Louisiana,June2018.AssociationforComputationalLinguistics. doi: 10.18653/v1/
N18-1074. URLhttps://aclanthology.org/N18-1074.
[36] Trulens,2023. https://www.trulens.org/.
[37] L. L. Wang, K. Lo, Y. Chandrasekhar, R. Reas, J. Yang, D. Burdick, D. Eide, K. Funk,
Y. Katsis, R. M. Kinney, Y. Li, Z. Liu, W. Merrill, P. Mooney, D. A. Murdick, D. Rishi,
J.Sheehan,Z.Shen,B.Stilson,A.D.Wade,K.Wang,N.X.R.Wang,C.Wilhelm,B.Xie,
D.M.Raymond,D.S.Weld,O.Etzioni,andS.Kohlmeier. CORD-19: TheCOVID-19open
research dataset. In K. Verspoor, K. B. Cohen, M. Dredze, E. Ferrara, J. May, R. Munro,
C. Paris, and B. Wallace, editors, Proceedings of the 1st Workshop on NLP for COVID-19
at ACL 2020, Online, July 2020. Association for Computational Linguistics. URL https:
//aclanthology.org/2020.nlpcovid19-acl.1.
[38] S.Wang,J.Liu,S.Song,J.Cheng,Y.Fu,P.Guo,K.Fang,Y.Zhu,andZ.Dou. Domainrag: A
chinesebenchmarkforevaluatingdomain-specificretrieval-augmentedgeneration,2024. URL
https://arxiv.org/abs/2406.05654.
[39] J. Wei, X. Wang, D. Schuurmans, M. Bosma, b. ichter, F. Xia, E. Chi, Q. V. Le, and
D.Zhou. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. InS.Koyejo,
S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, editors, Advances in Neu-
ral Information Processing Systems, volume 35, pages 24824–24837. Curran Associates,
Inc.,2022. URLhttps://proceedings.neurips.cc/paper_files/paper/2022/file/
9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf.
[40] Y. Wu, J. Zhu, S. Xu, K. Shum, C. Niu, R. Zhong, J. Song, and T. Zhang. Ragtruth: A
hallucinationcorpusfordevelopingtrustworthyretrieval-augmentedlanguagemodels,2023.
[41] X.Yang,K.Sun,H.Xin,Y.Sun,N.Bhalla,X.Chen,S.Choudhary,R.D.Gui,Z.W.Jiang,
Z.Jiang,L.Kong,B.Moran,J.Wang,Y.E.Xu,A.Yan,C.Yang,E.Yuan,H.Zha,N.Tang,
L.Chen,N.Scheffer,Y.Liu,N.Shah,R.Wanga,A.Kumar,W.tauYih,andX.L.Dong. Crag–
comprehensiveragbenchmark,2024. URLhttps://arxiv.org/abs/2406.04744.
[42] Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. W. Cohen, R. Salakhutdinov, and C. D. Manning.
HotpotQA:Adatasetfordiverse,explainablemulti-hopquestionanswering. InConferenceon
EmpiricalMethodsinNaturalLanguageProcessing(EMNLP),2018.
[43] S.Ye,D.Kim,S.Kim,H.Hwang,S.Kim,Y.Jo,J.Thorne,J.Kim,andM.Seo. FLASK:Fine-
grainedlanguagemodelevaluationbasedonalignmentskillsets. InTheTwelfthInternational
ConferenceonLearningRepresentations,2024. URLhttps://openreview.net/forum?
id=CYmF38ysDa.
[44] X.Yue,B.Wang,Z.Chen,K.Zhang,Y.Su,andH.Sun. Automaticevaluationofattribution
by large language models. In H. Bouamor, J. Pino, and K. Bali, editors, Findings of the
AssociationforComputationalLinguistics: EMNLP2023,pages4615–4635,Singapore,Dec.
2023.AssociationforComputationalLinguistics. doi: 10.18653/v1/2023.findings-emnlp.307.
URLhttps://aclanthology.org/2023.findings-emnlp.307.
[45] X.Zhang,N.Thakur,O.Ogundepo,E.Kamalloo,D.Alfonso-Hermelo,X.Li,Q.Liu,M.Reza-
gholizadeh,andJ.Lin. Makingamiracl: Multilingualinformationretrievalacrossacontinuum
oflanguages,2022.
[46] L.Zheng,W.-L.Chiang,Y.Sheng,S.Zhuang,Z.Wu,Y.Zhuang,Z.Lin,Z.Li,D.Li,E.Xing,
H.Zhang,J.E.Gonzalez,andI.Stoica. JudgingLLM-as-a-judgewithMT-benchandchatbot
arena. InThirty-seventhConferenceonNeuralInformationProcessingSystemsDatasetsand
BenchmarksTrack,2023. URLhttps://openreview.net/forum?id=uccHPGDlao.
[47] F. Zhu, W. Lei, Y. Huang, C. Wang, S. Zhang, J. Lv, F. Feng, and T.-S. Chua. TAT-QA:
A question answering benchmark on a hybrid of tabular and textual content in finance. In
C.Zong, F.Xia, W.Li, andR.Navigli, editors, Proceedingsofthe59thAnnualMeetingof
the Association for Computational Linguistics and the 11th International Joint Conference
onNaturalLanguageProcessing(Volume1: LongPapers),pages3277–3287,Online,Aug.
2021.AssociationforComputationalLinguistics. doi: 10.18653/v1/2021.acl-long.254. URL
https://aclanthology.org/2021.acl-long.254.
13

7 Appendix
7.1 RAGBenchCodeandData
We release RAGBench data on Hugginggface: https://huggingface.co/datasets/
rungalileo/ragbench. Refertomodelcardanddocumentationthere.
We publish our inferfence and evaluation code on Gihub: https://github.com/rungalileo/
ragbench/tree/main/ragbench.
7.2 RAGBenchDatasetDetails
RAGBenchissourcedfrompubliclyreleasedacadmicandindustrydatasets. Asfarasweknow,none
ofthecomponentdatasetscontainpersonallyidentifiableinformationoroffensivecontent.
PubMedQA[14] PubMedQAisacollectionofPubMedresearchabstractswithcorresponding
yes/no/maybequestionspairedwitheachabstract. Theoriginaldatasetcomprises3subsets: PQA-L,
PQA-U,andPQA-A,with1k,60k,and210kabstracts,respectively. Forallsubsets,thequestion
is derived from the title of the PubMed article using rule-based heuristics. Long answers are
automatically derived from the last sentence of the abstract for PQA-L and PQA-U, and QA-L
answersarefurtherreviewedbyexpertannotatorsandannotatedasyes/no/maybe. PQA-Acomprises
exclusivelyautomaticallygeneratedquestionsandshortanswers.
ForRAGBenchweutilizethePQA-Usubsetandre-frameitfromQAintoaRAGtask. Tosimulate
RAG,weleveragealreadysegmentedPQA-Uabstractscontextchunksandweencodethemintoa
vectorDBwithOpenAIembeddings. ThesizeoftheresultingDBis200k. Weretrieve4chunksfor
eachPQA-UquestionusingFAISSwitheuclediandistanceasthesimilarityfunction. Weignorethe
responsesandlabelsintheoriginaldatasetandgeneratenewresponseswithanLLM.
CovidQA-RAG CovidQA-RAGisacombinationof2kexpert-annotatedquestionssourcedfrom
COVID-QA[26]andavectordatabaseof250,000100-wordpassagesbuiltbySiriwardhanaetal.
[34]. BothquestionsandanswersaresourcedfromCORD-19[37]collectionofresearcharticles
aboutCOVID-19.
We embed the questions and database passages with OpenAI embeddings and retrieve up to N
passagesforeachCOVID-QAquestionfromthevectordatabaseusingFAISSwitheuclediandistance
asthesimilarityfunctionandmax_distance=0.25. WegenerateresponsesforeachresultingRAG
(context,question)instancewithanLLM.
HotpotQA[42] HotpotQAcomprises113Kcrowd-sourcedquestion-answerpairssourcedfrom
Wikipedia. Each pair is associated with a set of related context passages from one or multiple
Wikipediapages. Thedatasetisconstructedinawaythatrequiresmulti-hopreasoningovermultiple
contextdocumentstoarriveattheanswer,whichrendersitavaluablecandidateforourbenchmark.
Wesampledatafromthedev-distractorsplit,whichcontainsupto8distractorcontextdocuments
persample. Wedownsamplethecontextdocumentsto4perexample,makingsuretoincludethe
document containing the response. We treat the context passages in HotpotQA as RAG context
documents,andgenerateresponsesforeach(context,question)instancewithanLLM.
MS Marco [28] MS Marco is an open-domain question answering dataset sourced from Bing
searchengineuserquerylogs. Eachquestionisassociatedwith10contextpassagesretrievedvia
Bingwebsearch. Humanannotatorscomposearesponsebasedontheprovidedcontextdocuments,
andlabelthedocumentsutilizedintheresponseasrelevant. Wesampledatafromtheoriginalversion
ofthedataset,comprising80ktrain,10kvalidation,and10ktestsamples. Aswithotherdatasets,we
ignorethehumanannotatedanswersandgenerateresponseswithanLLMinRAGsetting.
CUAD[12] CUADisacollectionofcommerciallegalcontractswithexpertannotatedquestions
andresponses. Thecontractsaresourcedfromapubliclegalcontractlibrary(EDGAR)andrange
from1-100pagesinlength. Expertsinthelegaldomaincomposemultiplequestionspercontract
andlabeltherelevantpartsofthecontractthatareusefulforansweringthequestions. Thereare
21kquestionspertainingto510documentsintotal. Thequestionsareveryspecifictoeachcontract,
14

thuswedon’tperformadditionalretrievaloverthecontractcorpus,andformRAGexampleswith1
contextcontracteachforourbenchmark. Duetohighanntoationcostsassociatedwithlong-context
RAG,wesample5questionperdoc. Aswithotherdatasets,wegenerateresponseswithanLLMin
RAGsetting.
DelucionQA[33] DelucionQAisadomain-specificRAGdatasetleveragingJeep’s2023Gladiator
modelmanualasthesourceofknowledge. Thequestionsandanswersareautomaticallygeneratedby
largelanguagemodels. RAGcontextpassagesareretrievedfromtheJeepcarmanualviabothsparse
and dense retrieval methods to add variance in the sample distribution. Further, MTurk workers
annotatewhetherornotresponsesaresupportedbythecontext.
Upon closer inspection, we found only 1 relevant passage associated with each question in the
DelucionQA dataset. To make the dataset more challenging for RAGBench, we build a vector
databasefromthe1,046contextpassagesinDelucionQAandandretrieveupto3contextdocuments
perquestionfromit. Weusetext-embedding-ada-002embeddingsfromOpenAItobuildthe
database. Thereare913uniquequestionsinDelucionQA.Foreachresulting(context, question)
sample,wegenerateresponseswithanLLM.
EManual [27] EManual is a question answer dataset comprising consumer electronic device
manuals and realistic questions about them composed by human annotators. The subset made
availableatthetimeofwritingamountsto659uniquequestionsabouttheSamsungSmartTV/remote
andtheaccompanyingusermanual,segmentedinto261chunks. ToformaRAGdataset,weembed
themanualsegmentsintoavectordatabasewithOpenAIembeddingandretrieveupto3context
documentsperquestionfromit. Foreachresulting(context,question)sample,wegenerateresponses
withanLLM.
TechQA[3] TechQAisacollectionofreal-worlduserquestionspostedonIBMDeveloperand
DeveloperWorksforums,alongwith50technicalsupportdocumentsrelatingtoeachquestion. The
documentsaresourcedfromdatabaseof800ktechnicaldocumentsthatsupportacceptedanswers
onthetechforums. Theauthorsrelease1.4kquestions,splitbetweentrain,validation,andtestsets.
Thedataarecuratedsuchthatfractionsontheeachsplitunanswerablegiventheinformationinthe
linkeddocuments, whichmakesitagoodcandidateforRAGBench. Toreduceannotationcosts,
wesub-samplethedatadownto10documentsperquestion,makingsuretoincludethedocument
containingtheanswer,whenapplicable. Weusetheprovidedsplitswith(contextdocument,question)
examplesandgenerateresponsesforeachwithanLLM.
FinQA[6] FinQAisaQAdatasetoffinancialreportpassagesandassociatedquestions. Questions
arecuratedsuchthatnumericalreasoningovermultipleunstructuredandtabularinputsisrequiredto
arriveattheanswer. FinQAtotals8,281financialQApairs,splitbetweentrain,validation,andtest
splits. Weretaintheoriginalsplitsandgenerate2LLMresponsespereachcontext-queryexamplein
FinQA.
TAT-QA [47] TAT-QA is another financial QA dataset that requires numerical reasoning over
tables and text. The data are sourced from 500 financial reports released on https://www.
annualreports.com/. Expert annotators with background in finance annotate question-answer
pairsbasedontheavailabledocuments. Weleveragethefulldataset(13ktrain,1.6kvalidationand
test)butgeneratenewresponseswithLLMsforRAGBench.
HAGRID[15] HAGRIDisaQAdatasetbuiltontopofMIRACL[45],amulti-lingualinformation-
retrievaldataset. HAGRIDpassesquestionsandrelevantcontextdocumentsfromMIRACLEthrough
an LLM to produce a response for each example in the dataset. Annotors then rate the response
oninformativenessandattributiondimensions. Theoriginalcontextdocumentsaresourcedfrom
Wikipedia and associated questions are generated by expert annotators. Since HAGRID already
containsLLM-generatedresponses,wedirectlyusethemanddon’tgenerateadditionalresponsesfor
RAGBench.
ExpertQA [25] ExpertQA is a collection of curated questions from domain-experts in various
fieldsofsicence,arts,andlaw. Thedatasetalsocontainsexpertcuratedpasssagesrelevanttoeach
15

question,alongsideLLM-generatedresponses. AswithHAGRID,weleveragetheLLM-generated
responsesinExpertQAdirectlyforourRAGdataset.
7.3 ResponseGenerationPrompt
WeusethefollowingprompttemplatetogenerateLLMresponsesforeachsampleinRAGBench.
Contextdocuments,separatedbylinebreaks,alongwiththequestionareslottedinforeachgeneration
sample.
| Use the | following | pieces | of context | to answer the | question. |
| ------- | --------- | ------ | ---------- | ------------- | --------- |
{documents}
| Question: | {question} |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- |
7.4 GPTLabelingPrompt
WeusethefollowingprompttemplatetogenerateannotationswithGPT-4
I asked someone to answer a question based on one or more documents.
Your task is to review their response and assess whether or not each sentence
in that response is supported by text in the documents. And if so, which
sentences in the documents provide that support. You will also tell me which
of the documents contain useful information for answering the question, and
| which of the | documents | the | answer was sourced | from. |     |
| ------------ | --------- | --- | ------------------ | ----- | --- |
Here are the documents, each of which is split into sentences. Alongside each
sentence is associated key, such as ’0a.’ or ’0b.’ that you can use to refer
to it:
‘‘‘
{documents}
‘‘‘
| The question | was: |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- |
‘‘‘
{question}
‘‘‘
Here is their response, split into sentences. Alongside each sentence is
associated key, such as ’a.’ or ’b.’ that you can use to refer to it. Note
that these keys are unique to the response, and are not related to the keys
in the documents:
‘‘‘
{answer}
‘‘‘
| You must respond | with | a JSON | object matching | this schema: |     |
| ---------------- | ---- | ------ | --------------- | ------------ | --- |
‘‘‘
{{
| "relevance_explanation":         |     |          | string,   |     |     |
| -------------------------------- | --- | -------- | --------- | --- | --- |
| "all_relevant_sentence_keys":    |     |          | [string], |     |     |
| "overall_supported_explanation": |     |          | string,   |     |     |
| "overall_supported":             |     | boolean, |           |     |     |
| "sentence_support_information":  |     |          | [         |     |     |
{{
| "response_sentence_key": |     |         | string, |     |     |
| ------------------------ | --- | ------- | ------- | --- | --- |
| "explanation":           |     | string, |         |     |     |
16

| "supporting_sentence_keys": |     |     |         | [string], |     |
| --------------------------- | --- | --- | ------- | --------- | --- |
| "fully_supported":          |     |     | boolean |           |     |
}},
],
| "all_utilized_sentence_keys": |     |     | [string] |     |     |
| ----------------------------- | --- | --- | -------- | --- | --- |
}}
‘‘‘
The relevance_explanation field is a string explaining which documents
contain useful information for answering the question. Provide a step-by-step
breakdown of information provided in the documents and how it is useful for
| answering | the question. |     |     |     |     |
| --------- | ------------- | --- | --- | --- | --- |
The all_relevant_sentence_keys field is a list of all document sentences keys
(e.g. ’0a’) that are revant to the question. Include every sentence that is
useful and relevant to the question, even if it was not used in the response,
or if only parts of the sentence are useful. Ignore the provided response when
making this judgement and base your judgement solely on the provided documents
and question. Omit sentences that, if removed from the document, would not
| impact | someone’s | ability | to answer | the question. |     |
| ------ | --------- | ------- | --------- | ------------- | --- |
The overall_supported_explanation field is a string explaining why the response
*as a whole* is or is not supported by the documents. In this field, provide a
step-by-step breakdown of the claims made in the response and the support (or
lack thereof) for those claims in the documents. Begin by assessing each claim
separately, one by one; don’t make any remarks about the response as a whole
| until you | have assessed | all | the claims | in isolation. |     |
| --------- | ------------- | --- | ---------- | ------------- | --- |
The overall_supported field is a boolean indicating whether the response as a
whole is supported by the documents. This value should reflect the conclusion
you drew at the end of your step-by-step breakdown in overall_supported_explanation.
In the sentence_support_information field, provide information about the support
| *for each | sentence* | in the | response. |     |     |
| --------- | --------- | ------ | --------- | --- | --- |
The sentence_support_information field is a list of objects, one for each sentence
| in the | response. | Each object | MUST | have the following | fields: |
| ------ | --------- | ----------- | ---- | ------------------ | ------- |
- response_sentence_key: a string identifying the sentence in the response.
| This key | is the same | as the | one used | in the response | above. |
| -------- | ----------- | ------ | -------- | --------------- | ------ |
- explanation: a string explaining why the sentence is or is not supported by the
documents.
- supporting_sentence_keys: keys (e.g. ’0a’) of sentences from the documents that
support the response sentence. If the sentence is not supported, this list MUST
be empty. If the sentence is supported, this list MUST contain one or more keys.
In special cases where the sentence is supported, but not by any specific sentence,
you can use the string "supported_without_sentence" to indicate that the sentence
is generally supported by the documents. Consider cases where the sentence is
expressing inability to answer the question due to lack of relevant information in
the provided contex as "supported_without_sentence". In cases where the sentence
is making a general statement (e.g. outlining the steps to produce an answer, or
summarizing previously stated sentences, or a transition sentence), use the
sting "general".In cases where the sentence is correctly stating a well-known fact,
like a mathematical formula, use the string "well_known_fact". In cases where the
sentence is performing numerical reasoning (e.g. addition, multiplication), use
| the string | "numerical_reasoning". |     |     |     |     |
| ---------- | ---------------------- | --- | --- | --- | --- |
- fully_supported: a boolean indicating whether the sentence is fully supported by
the documents.
- This value should reflect the conclusion you drew at the end of your step-by-step
| breakdown | in explanation. |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- |
- If supporting_sentence_keys is an empty list, then fully_supported must be false.
17

- Otherwise, use fully_supported to clarify whether everything in the response
sentence is fully supported by the document text indicated in supporting_sentence_keys
(fully_supported = true), or whether the sentence is only partially or incompletely
supported by that document text (fully_supported = false).
The all_utilized_sentence_keys field is a list of all sentences keys (e.g. ’0a’) that
were used to construct the answer. Include every sentence that either directly supported
the answer, or was implicitly used to construct the answer, even if it was not used
in its entirety. Omit sentences that were not used, and could have been removed from
the documents without affecting the answer.
You must respond with a valid JSON string. Use escapes for quotes, e.g. ‘\\"‘, and
newlines, e.g. ‘\\n‘. Do not write anything before or after the JSON string. Do not
wrap the JSON string in backticks like ‘‘‘ or ‘‘‘json.
As a reminder: your task is to review the response and assess which documents contain
useful information pertaining to the question, and how each sentence in the response
is supported by the text in the documents.\
7.5 AnnotationPost-ProcessingSteps
AsshowninAppendix7.4,werequestverydetailedannotationswithexplanationsfromGPT-4-turbo.
Wepivotonchain-of-thought[39]andredundancytoencouragehighqualitylabelsfromtheannotator
model.
ForAdherence,werequestbothresponse-levelandsentence-levelannotationsthatwecomparein
post-processingtoidentifyinconsistencieswhereGPT-4disagreeswithitsownjudgements. For
example, if GPT-4 claims a response as supported by the context as a whole, but identifies no
supportinginformationforoneormoreclaimsintheresponse,wesendtheexampleforre-annotation.
Were-annotatealldataupto3times,afterwhichafraction(<2%)ofthedataarestillconflicting.
Aftermanualinspection,wefindthatthemajorityoftheconflictsarisefrompartiallyhallucinated
sentencesthataresomewhat,butnotfully,groundedinthecontext. Weleverageasentence-level
"fully_supported"booleanannotationtoidentifyandresolvesuchcases. Accordingtoourannotation
schema,wetreatallpartiallysupportedsentencesashallucinations.
Since all TRACe metrics are related, we qualitatively observe that taking the extra measures for
Adherencealsopositivelyimpactsthequalityandstabilityoftherelevanceandutilizationlabels.
In the final post-processing step, we remove any off-schema keys that GPT-4-turbo sometimes
injectsintotheresponse. Forexample, itwilloccasionallymisspell"supporting_sentence_keys"
as "supported_sentence_keys" and/or introduce completely new fields into the output json. We
algorithmicallyfindandremove/replacesuchannotationerrors.
7.6 AnnotationAlignmentwithHumanJudgements
7.6.1 AdherenceAlignmentwithDelucionQA
We validate our metric formulations and labeling approach on a human annotated benchmark.
DelucionQA[33]isacuratedcollectionofuserqueriesontheoperationofJeep’s2023Gladiator
model. NaturallanguagequeriesarefirstgeneratedbyanLLM,thenreviewedandfilteredbyhuman
annotators. ContextdocumentsaresourcedfromJeep’sGladiatorUserManual,andresponsesare
generatedbyvariousLLMs. Humanannotatorslabeleachresponsesentenceas"Supported"bythe
contextdocuments,"Conflicted",or"Neither". Example-levellabelsarederivedfromthespan-level
annotationasfollows: ifatleastoneresponsesentenceisannotatedas"Conflicted"or"Neither",the
wholeresponsereceivesaHallucinatedlabel.
Inourinitialinvestigation,wefoundthatsentencesthatDelucionQAlabelsas"Neither"oftenfallinto
oneoftwocategories: (1)generalfillerstatements(e.g. "Herearethesteps:"),(2)claimsofmissing
information (e.g. "There is no mention of any problem with engine start-up in freezing weather
related to DEF."). According to our annotation schema, these types of statements are generally
grounded in the context and not hallucinations. Thus, we remove examples with any "Neither"
18

Table4: AnnotationAlignmentwithDelucionQA.WereportF1andAccuracymetricsonhuman
annotatedsubsetsofDelucionQA.DelucionQA(40)isasubsetof40examplesrandomlysampled
fromtheDelucionQAtestsetandannotatedforRelevanceandUtilizationbytheauthors.
| TestSet                                 |     |     | Metric      | F1   | Accuracy |
| --------------------------------------- | --- | --- | ----------- | ---- | -------- |
| DelucionQA-examplelevel                 |     |     | Adherence   | 0.83 | 0.76     |
| DelucionQA-examplelevel-remove"Neither" |     |     | Adherence   | 0.96 | 0.93     |
| DelucionQA-spanlevel-remove"Neither"    |     |     | Adherence   | 0.97 | 0.95     |
| DelucionQA(40)-sapenlevel               |     |     | Utilization | 0.92 | 0.94     |
| DelucionQA(40)-spanlevel                |     |     | Relevance   | 0.76 | 0.78     |
Table5: RankingofSimulatedRAGSystems. WeevaluateGPT-4-turboannotationsonsimulated
RAGdatasetsfromSaad-Falconetal.[32]. Thedatafromeachsourcearesyntheticallyaugmented
tocreatesetswithincreasingdegreesofcontextrelevance(Rel)andansweradherence(Adh). We
annotate500samplesfromeachsetandrankthemaccordingtotheaveragecontextrelevanceand
answeradherencemetrics. WereportKendall’stautoevaluatetheagreementbetweenGPT-4-turbo
rankingsandgroundtruth(higherisbetter).
|                        | NQ       | HotpotQA |     | WoW      | FEVER    |
| ---------------------- | -------- | -------- | --- | -------- | -------- |
|                        | Rel Adh  | Rel      | Adh | Rel Adh  | Rel Adh  |
| Kendall’sTaubinary     | 1.0 0.83 | 0.87     | 1.0 | 1.0 0.89 | 1.0 0.78 |
| Kendall’sTaucontinuous | 0.94 -   | 0.73     | -   | 1.0      | - 0.77 - |
sentence annotations for our analysis. We annotate the remaining 421 examples with our LLM
annotatorandreportalignmentwithhumanannotationsinTable4.
7.6.2 RelevanceandUtilizationAlignmentwithDelucionQA
TovalidateRelevanceandUtilizationannotations,theauthorsannotateasmallsetof40randomly
samplesexamplesfromtheDelucionQAtestset. Wefollowthesameinstructionsasinoutannotation
prompt7.4tolabelrelevantandutilizedcontextsentences,giventhecontext,query,andresponse.
Wereportsentence-levelF1andoverallalignment(Accuracy)scoresinTable4.
7.6.3 Rank-basedAlignmentforAdherenceandRelevance
We use mock RAG datasets generated by Saad-Falcon et al. [32] for this analysis. Their RAG
validationsetissampledfromKILT[29],includingNaturalQuestions(NQ)[17],HotpotQA[42],
FEVER[35], and Wizards of Wikipedia (WoW) [8] datasets. The authors synthetically generate
systemsofvaryingqualitybyadjustingtheratioofrelevantdocumentsandresponsesinthedata. We
sample500examplesfromeachsimulatedRAGdatasetandannotatedthemasdescribedinsection
3.4. Next,wecalculateaverageannotatedcontextrelevanceandadherencescoresforeachdataset
andusethosetorankthemocksystems. WecompareourrankingstogroundtruthwiththeKendall
rankcorrelation(Kendall’sτ)metric,whichevaluatestheagreementbetweentwosetsofranksona
scalefrom0(noagreement)to1(perfectagreement).
AsshowninTable5,theGPT-4annotationsachievehighKendall’sτ rangingfrom0.78to1. Fora
faircomparisonwiththegroundtruthlabels,wederivebinarycontextrelevanceandlabelsfromthe
GPT-4annotationsbythresholdingtheexampleRelevancescore(equation2)at0. Forcomparison,
wealsoreportrankingresultswithourmoregranularexample-levelRelevancescoresthatrange
from0-1. Wefindthatthesemetricsproduceadifferentranking(seelowerKendall’sτ inTable5),
whichweattributetothemetricscapturingdifferencesinretrievedcontextlengthacrossthedifferent
examples.
7.7 RAGCaseStudy
WeusethefollowingprompttemplatesfortheRAGCaseStudy:
19

NOCONTEXT:
{question}
SHORT:
| Answer the | question | using the | provided | context. |     |
| ---------- | -------- | --------- | -------- | -------- | --- |
Context:
{documents}
| Question: | {question} |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- |
LONG:
You are a chatbot providing answers to user queries. You will be given one or more context documents, and a question. \
| Use the | information | in the documents |     | to answer | the question. |
| ------- | ----------- | ---------------- | --- | --------- | ------------- |
If the documents do not provide enough information for you to answer the question, then say \
"The documents are missing some of the information required to answer the question." Don’t quote any external knowledge that is \
| not in the | documents. | Don’t try | to make | up an | answer. |
| ---------- | ---------- | --------- | ------- | ----- | ------- |
| Context    | Documents: |           |         |       |         |
{documents}
| Question: | {question} |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- |
LONG+CoT:
You are a chatbot providing answers to user queries. You will be given one or more context documents, and a question. \
| Use the | information | in the documents |     | to answer | the question. |
| ------- | ----------- | ---------------- | --- | --------- | ------------- |
If the documents do not provide enough information for you to answer the question, then say \
"The documents are missing some of the information required to answer the question." Don’t quote any external knowledge that is \
| not in the | documents. | Don’t try | to make | up an | answer. |
| ---------- | ---------- | --------- | ------- | ----- | ------- |
Think step by step and explain your reasoning, quoting the documents when necessary.
| Context | Documents: |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- |
{documents}
| Question: | {question} |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- |
Table6reportscomprehensiveresultsfromtheRAGCaseStudy.
7.8 DeBERTamodeltraining
WetrainthemodelonaGoogleCloudPlatformA-100GPUinstancefor3epochswithinitiallearning
rate5−6forthebasemodellayersand2−5fortheheads,withwarmupandalineardecayrate.
20

|                           | Table6:            | RAGCaseStudyResults.        |                 |                |
| ------------------------- | ------------------ | --------------------------- | --------------- | -------------- |
| retriever k promptversion | generationmodel    | averelevance aveutilization | avecompleteness | pchallucinated |
| tfidf 2 nocontext         | gpt-3.5-turbo-0125 | 0.65 0.30                   | 0.53            | 0.94           |
| tfidf 2 nocontext         | gpt-4o             | 0.66 0.45                   | 0.70            | 0.95           |
| tfidf 2 short             | gpt-3.5-turbo-0125 | 0.62 0.43                   | 0.72            | 0.19           |
| tfidf 2 short             | gpt-4o             | 0.66 0.54                   | 0.81            | 0.29           |
| tfidf 2 long              | gpt-3.5-turbo-0125 | 0.62 0.43                   | 0.71            | 0.04           |
| tfidf 2 long              | gpt-4o             | 0.66 0.35                   | 0.57            | 0.08           |
| tfidf 2 long+CoT          | gpt-3.5-turbo-0125 | 0.65 0.53                   | 0.82            | 0.13           |
| tfidf 2 long+CoT          | gpt-4o             | 0.63 0.50                   | 0.78            | 0.04           |
| tfidf 4 nocontext         | gpt-3.5-turbo-0125 | 0.46 0.22                   | 0.53            | 0.86           |
| tfidf 4 nocontext         | gpt-4o             | 0.45 0.29                   | 0.65            | 0.86           |
| tfidf 4 short             | gpt-3.5-turbo-0125 | 0.43 0.29                   | 0.67            | 0.18           |
| tfidf 4 short             | gpt-4o             | 0.47 0.38                   | 0.78            | 0.13           |
| tfidf 4 long              | gpt-3.5-turbo-0125 | 0.45 0.28                   | 0.64            | 0.05           |
| tfidf 4 long              | gpt-4o             | 0.48 0.28                   | 0.60            | 0.05           |
| tfidf 4 long+CoT          | gpt-3.5-turbo-0125 | 0.44 0.33                   | 0.72            | 0.10           |
| tfidf 4 long+CoT          | gpt-4o             | 0.49 0.36                   | 0.73            | 0.02           |
| faiss 2 nocontext         | gpt-3.5-turbo-0125 | 0.81 0.40                   | 0.50            | 0.94           |
| faiss 2 nocontext         | gpt-4o             | 0.81 0.53                   | 0.66            | 0.87           |
| faiss 2 short             | gpt-3.5-turbo-0125 | 0.75 0.55                   | 0.72            | 0.07           |
| faiss 2 short             | gpt-4o             | 0.82 0.72                   | 0.86            | 0.11           |
| faiss 2 long              | gpt-3.5-turbo-0125 | 0.78 0.58                   | 0.71            | 0.04           |
| faiss 2 long              | gpt-4o             | 0.82 0.52                   | 0.62            | 0.10           |
| faiss 2 long+CoT          | gpt-3.5-turbo-0125 | 0.81 0.64                   | 0.76            | 0.07           |
| faiss 2 long+CoT          | gpt-4o             | 0.83 0.69                   | 0.82            | 0.04           |
| faiss 4 nocontext         | gpt-3.5-turbo-0125 | 0.58 0.27                   | 0.47            | 0.88           |
| faiss 4 nocontext         | gpt-4o             | 0.58 0.36                   | 0.60            | 0.79           |
| faiss 4 short             | gpt-3.5-turbo-0125 | 0.53 0.31                   | 0.59            | 0.14           |
| faiss 4 short             | gpt-4o             | 0.58 0.47                   | 0.78            | 0.07           |
| faiss 4 long              | gpt-3.5-turbo-0125 | 0.54 0.33                   | 0.61            | 0.08           |
| faiss 4 long              | gpt-4o             | 0.61 0.32                   | 0.52            | 0.09           |
| faiss 4 long+CoT          | gpt-3.5-turbo-0125 | 0.58 0.42                   | 0.71            | 0.09           |
| faiss 4 long+CoT          | gpt-4o             | 0.60 0.47                   | 0.76            | 0.05           |
21