Evaluation of Retrieval-Augmented Generation:
A Survey
HaoYu1,2,AoranGan3,KaiZhang3,ShiweiTong1†,QiLiu3,andZhaofengLiu1
1 TencentCompany
2 McGillUniversity
3 StateKeyLaboratoryofCognitiveIntelligence,
UniversityofScienceandTechnologyofChina
hao.yu2@mail.mcgill.ca
gar@mail.ustc.edu.cn
{shiweitong†,zhaofengliu}@tencent.com
{kkzhang08,qiliuql}@ustc.edu.cn
Abstract. Retrieval-AugmentedGeneration(RAG)hasrecentlygainedtraction
in natural language processing. Numerous studies and real-world applications
areleveragingitsabilitytoenhancegenerativemodelsthroughexternalinforma-
tionretrieval.EvaluatingtheseRAGsystems,however,posesuniquechallenges
due to their hybrid structure and reliance on dynamic knowledge sources. To
betterunderstandthesechallenges,weconductAUnifiedEvaluationProcessof
RAG(Auepora)andaimtoprovideacomprehensiveoverviewoftheevaluation
andbenchmarksofRAGsystems.Specifically,weexamineandcompareseveral
quantifiable metrics of the Retrieval and Generation components, such as rele-
vance,accuracy,andfaithfulness,withinthecurrentRAGbenchmarks,encom-
passingthepossibleoutputandgroundtruthpairs.Wethenanalyzethevarious
datasetsandmetrics,discussthelimitationsofcurrentbenchmarks,andsuggest
potentialdirectionstoadvancethefieldofRAGbenchmarks.
1 Introduction
Retrieval-Augmented Generation (RAG) [34] efficiently enhances the performance of
generativelanguagemodelsthroughintegratinginformationretrievaltechniques.Itad-
dresses a critical challenge faced by standalone generative language models: the ten-
dency to produce responses that, while plausible, may not be grounded in facts. By
retrieving relevant information from external sources, RAG significantly reduces the
incidence of hallucinations [23] or factually incorrect outputs, thereby improving the
content’sreliabilityandrichness.[73]Thisfusionofretrievalandgenerationcapabil-
ities enables the creation of responses that are not only contextually appropriate but
alsoinformedbythemostcurrentandaccurateinformationavailable,makingRAGa
developmentinthepursuitofmoreintelligentandversatilelanguagemodels[73,64].
†CorrespondingAuthor
PaperHomepage:https://github.com/YHPeter/Awesome-RAG-Evaluation
4202
luJ
3
]LC.sc[
2v73470.5042:viXra

2 HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
Numerous studies of RAG systems have emerged from various perspectives since
theadventofLargeLanguageModels(LLMs)[55,45,59,42,41,69,16].TheRAGsys-
temcomprisestwoprimarycomponents:RetrievalandGeneration.Theretrievalcom-
ponent aims to extract relevant information from various external knowledge sources.
Itinvolvestwomainphases,indexingandsearching.Indexingorganizesdocumentsto
facilitate efficient retrieval, using either inverted indexes for sparse retrieval or dense
vectorencodingfordenseretrieval[16,12,28].Thesearchingcomponentutilizesthese
indexes to fetch relevant documents on the user’s query, often incorporating the op-
tionalrerankers[4,39,6,52]torefinetherankingoftheretrieveddocuments.Thegener-
ationcomponentutilizestheretrievedcontentandquestionquerytoformulatecoherent
andcontextuallyrelevantresponseswiththepromptingandinferencingphases.Asthe
“Emerging”ability[59]ofLLMsandthebreakthroughinaligninghumancommands
[42],LLMsarethebestperformancechoicesmodelforthegenerationstage.Prompt-
ing methods like Chain of Thought (CoT) [60], Tree of Thgouht [65], Rephrase and
Respond(RaR)[8]guidebettergenerationresults.Intheinferencingstep,LLMsinter-
pretthepromptedinputtogenerateaccurateandin-depthresponsesthatalignwiththe
query’sintentandintegratetheextractedinformation[35,9]withoutfurtherfinetuning,
such as fully finetuning [16,1,67,68] or LoRA [21]. Appendix A details the complete
RAGstructure.Figure1illustratesthestructureoftheRAGsystemsasmentioned.
Fig.1:ThestructureoftheRAGsystemwithretrievalandgenerationcomponentsand
correspondingfourphrases:indexing,search,promptingandinferencing.Thepairsof
“Evaluable Outputs” (EOs) and “Ground Truths” (GTs) are highlighted in read frame
andgreenframe,withbrowndashedarrows.
The importance of evaluating RAG is increasing in parallel with the advancement
ofRAG-specificmethodologies.Ontheonehand,RAGisacomplexsystemintricately
tiedtospecificrequirementsandlanguagemodels,resultinginvariousevaluationmeth-
ods,indicators,andtools,particularlygiventheblack-boxLLMgeneration.Evaluating
RAG systems involves specific components and the complexity of the overall system
assessment.Ontheotherhand,thecomplexityofRAGsystemsisfurthercompounded

EvaluationofRetrieval-AugmentedGeneration:ASurvey 3
by the external dynamic database and the various downstream tasks, such as content
creationoropendomainquestionanswering[16,70].Thesechallengesnecessitatethe
development of comprehensive evaluation metrics that can effectively capture the in-
terplaybetweenretrievalaccuracyandgenerativequality[2,7].Toclarifytheelements
further,wetrytoaddressthecurrentgapsinthearea,whichdiffersfromthepriorRAG
surveys[74,16,24]thatpredominantlycollectedspecificRAGmethodsordata.Wehave
compiled 12 distinct evaluation frameworks, encompassing a range of aspects of the
RAGsystem.Followingtheprocedureofmakingbenchmarks,weanalyzethroughtar-
gets,datasetsandmetricsmentionedinthesebenchmarksandsummarizethemintoA
UnifiedEvaluationProcessofRAG(Auepora)asthreecorrespondingphases.
Forthispaper,wecontributeinthefollowingaspects:
1. Challenge of Evaluation: This is the first work that summarizes and classifies
thechallengesinevaluatingRAGsystemsthroughthestructureofRAGsystems,
includingthreepartsretrieval,generation,andthewholesystem.
2. AnalysisFramework:InlightofthechallengesposedbyRAGsystems,weintro-
duceananalyticalframework,referredtoasAUnifiedEvaluationProcessofRAG
(Auepora),whichaimstoelucidatetheuniquecomplexitiesinherenttoRAGsys-
tems and guide for readers to comprehend the effectiveness of RAG benchmarks
acrossvariousdimensions
3. RAG Benchmark Analysis: With the help of Auepora, we comprehensively an-
alyze existing RAG benchmarks, highlighting their strengths and limitations and
proposingrecommendationsforfuturedevelopmentsinRAGsystemevaluation.
2 ChallengesinEvaluatingRAGSystems
Evaluating hybrid RAG systems entails evaluating retrieval, generation and the RAG
systemasawhole.Theseevaluationsaremultifaceted,requiringcarefulconsideration
andanalysis.Eachofthemencompassesspecificdifficultiesthatcomplicatethedevel-
opmentofacomprehensiveevaluationframeworkandbenchmarksforRAGsystems.
Retrieval Theretrievalcomponentiscriticalforfetchingrelevantinformationthatin-
formsthegenerationprocess.Oneprimarychallengeisthedynamicandvastnatureof
potential knowledge bases, ranging from structured databases to the entire web. This
vastness requires evaluation metrics that can effectively measure the precision, recall,
and relevance of retrieved documents in the context of a given query [52,32]. More-
over,thetemporalaspectofinformation,wheretherelevanceandaccuracyofdatacan
changeovertime,addsanotherlayerofcomplexitytotheevaluationprocess[6].Addi-
tionally,thediversityofinformationsourcesandthepossibilityofretrievingmisleading
orlow-qualityinformationposesignificantchallengesinassessingtheeffectivenessof
filtering and selecting the most pertinent information [39]. The traditional evaluation
indicatorsforretrieval,suchasRecallandPrecision,cannotfullycapturethenuances
of RAG retrieval systems, necessitating the development of more nuanced and task-
specificevaluationmetrics[49].

4 HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
Generation The generation component, powered by LLMs, produces coherent and
contextually appropriate responses based on the retrieved content. The challenge here
lies in evaluating the faithfulness and accuracy of the generated content to the input
data.Thisinvolvesnotonlyassessingthefactualcorrectnessofresponsesbutalsotheir
relevance to the original query and the coherence of the generated text [75,49]. The
subjective nature of certain tasks, such as creative content generation or open-ended
question answering, further complicates the evaluation, as it introduces variability in
whatconstitutesa“correct”or“high-quality”response[48].
RAGSystemasaWhole EvaluatingthewholeRAGsystemintroducesadditionalcom-
plexities. The interplay between the retrieval and generation components means that
the entire system’s performance cannot be fully understood by evaluating each com-
ponent in isolation [49,14]. The system needs to be assessed on its ability to leverage
retrieved information effectively to improve response quality, which involves measur-
ingtheaddedvalueoftheretrievalcomponenttothegenerativeprocess.Furthermore,
practical considerations such as response latency and the ability to handle ambiguous
orcomplexqueriesarealsocrucialforevaluatingthesystem’soveralleffectivenessand
usability[39,6].
Conclusion Evaluating the target shift from traditional absolute numeric metrics to
multi-source and multi-target generation evaluation, along with the intricate interplay
betweenretrievalandgenerationcomponents,posessignificantchallenges.[5,50]Searches
inadynamicdatabasemayleadtomisleadingresultsorcontradictthefacts.Diverseand
comprehensive datasets that accurately reflect real-world scenarios are crucial. Chal-
lenges also arise in the realm of metrics, encompassing generative evaluation criteria
fordistinctdownstreamtasks,humanpreferences,andpracticalconsiderationswithin
the RAG system. Most prior benchmarks predominantly tackle one or several aspects
oftheRAGassessmentbutlackacomprehensive,holisticanalysis.
3 AUnifiedEvaluationProcessofRAG(Auepora)
TofacilitateadeeperunderstandingofRAGbenchmarks,weintroduceAUnifiedEval-
uationProcessofRAG(Auepora),whichfocusesonthreekeyquestionsofbenchmarks:
What to Evaluate? How to Evaluate? How to Measure? which correlated to Target,
Dataset, and Metric respectively. We aim to provide a clear and accessible way for
readerstocomprehendthecomplexitiesandnuancesofRAGbenchmarking.
The Target module is intended to determine the evaluation direction. The Dataset
module facilitates the comparison of various data constructions in RAG benchmarks.
Thefinalmodule,Metrics,introducesthemetricsthatcorrespondtospecifictargetsand
datasetsusedduringevaluation.Overall,itisdesignedtoprovideasystematicmethod-
ologyforassessingtheeffectivenessofRAGsystemsacrossvariousaspectsbycovering
allpossiblepairsatthebeginningbetweenthe“EvaluableOutputs”(EOs)and“Ground
Truths”(GTs).Inthefollowingsection,wewillexplainthoroughlyAueporaandutilize
itforintroducingandcomparingtheRAGbenchmarks.

EvaluationofRetrieval-AugmentedGeneration:ASurvey 5
Fig.2:TheTargetmodularoftheAuepora.
3.1 EvaluationTarget(WhattoEvaluate?)
ThecombinationofEOsandGTsintheRAGsystemcangenerateallpossibletargets,
which is the fundamental concept of the Auepora (as shown in Figure 1). Once iden-
tified, these targets can be defined based on a specific pair of EOs or EO with GT, as
illustratedinFigure2,andusedtoanalyzeallaspectsofcurrentRAGbenchmarks.
Retrieval TheEOsaretherelevantdocumentsforevaluatingtheretrievalcomponent
depending on the query. Then we can construct two pairwise relationships for the re-
trieval component, which are Relevant Documents ↔ Query, Relevant Documents ↔
DocumentsCandidates.
- Relevance(RelevantDocuments↔Query)evaluateshowwelltheretrieveddocu-
mentsmatchtheinformationneededexpressedinthequery.Itmeasuresthepreci-
sionandspecificityoftheretrievalprocess.
- Accuracy(RelevantDocuments↔DocumentsCandidates)assesseshowaccurate
the retrieved documents are in comparison to a set of candidate documents. It is
a measure of the system’s ability to identify and score relevant documents higher
thanlessrelevantorirrelevantones.
Generation The similar pairwise relations for the generation components are listed
below.TheEOsarethegeneratedtextandphrasedstructuredcontent.Thenweneedto
comparetheseEOswiththeprovidedGTsandlabels.
- Relevance(Response↔Query)measureshowwellthegeneratedresponsealigns
withtheintentandcontentoftheinitialquery.Itensuresthattheresponseisrelated
tothequerytopicandmeetsthequery’sspecificrequirements.
- Faithfulness (Response ↔ Relevant Documents) evaluates if the generated re-
sponseaccuratelyreflectstheinformationcontainedwithintherelevantdocuments
andmeasurestheconsistencybetweengeneratedcontentandthesourcedocuments.
- Correctness (Response ↔ Sample Response) Similar to the accuracy in the re-
trievalcomponent,thismeasurestheaccuracyofthegeneratedresponseagainsta
sampleresponse,whichservesasagroundtruth.Itchecksiftheresponseiscorrect
intermsoffactualinformationandappropriateinthecontextofthequery.

HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
6
| The targets | of Retrieval | and | Generation components | are introduced. | Table 1 lists |
| ----------- | ------------ | --- | --------------------- | --------------- | ------------- |
therelativeworkonimprovingandevaluatingRAGanditsbenchmarkscutoffinJune
Table 1: The evaluating targets and corresponding metrics across various frameworks
forevaluatingRAGsystems.Thepresentationdistinguishesbetweenthecoreareasof
RetrievalandGenerationconsideredintheevaluation.Thedifferentaspectsoftheeval-
uation are set as different colours in the table: Relevance, Accuracy of Retrieval and
Faithfulness,CorrectnessandRelevanceofGeneration.TheconsiderationoftheAddi-
tional Requirements beyond the retrieval and generation component is also collected.
Notedthatquiteafewoftheworksemployedmultiplemethodsorevaluatedmultiple
aspectssimultaneously.
| Category | Framework | Time | RawTargets | Retrieval | Generation |
| -------- | --------- | ---- | ---------- | --------- | ---------- |
ContextRelevance
| Tool | TruEraRAGTriad[54]2023.10 |     | AnswerRelevance | LLMasaJudge | LLMasaJudge |
| ---- | ------------------------- | --- | --------------- | ----------- | ----------- |
Groundedness
Accuracy
Faithfulness
| Tool | LangChainBench.[32]2023.11 |     |     | Accuracy | LLMasaJudge |
| ---- | -------------------------- | --- | --- | -------- | ----------- |
ExecutionTime
Embed.CosDistance
Correctness
| Tool | DatabricksEval[33] | 2023.12 | Readability | -   | LLMasaJudge |
| ---- | ------------------ | ------- | ----------- | --- | ----------- |
Comprehensiveness
ContextRelevance
LLMGen+CosSim
| Benchmark | RAGAs[14] | 2023.09 | AnswerRelevance | LLMasaJudge |     |
| --------- | --------- | ------- | --------------- | ----------- | --- |
LLMasaJudge
Faithfulness
ResponseQuality
| Benchmark | RECALL[38] | 2023.11 |     | -   | BLEU,ROUGE-L |
| --------- | ---------- | ------- | --- | --- | ------------ |
Robustness
ContextRelevance
LLM+Classifier
| Benchmark | ARES[49] | 2023.11 | AnswerFaithfulness | LLM+Classifier |     |
| --------- | -------- | ------- | ------------------ | -------------- | --- |
LLM+Classifier
AnswerRelevance
InformationIntegration
NoiseRobustness
| Benchmark | RGB[6] | 2023.12 |     | -   | Accuracy |
| --------- | ------ | ------- | --- | --- | -------- |
NegativeRejection
CounterfactualRobustness
| Benchmark | MultiHop-RAG[52] | 2024.01 | RetrievalQuality | MAP,MRR,Hit@K | LLMasaJudge |
| --------- | ---------------- | ------- | ---------------- | ------------- | ----------- |
ResponseCorrectness
|           |              |         | CREATE,READ   |     | ROUGE,BLEU   |
| --------- | ------------ | ------- | ------------- | --- | ------------ |
| Benchmark | CRUD-RAG[39] | 2024.02 |               | -   |              |
|           |              |         | UPDATE,DELETE |     | RAGQuestEval |
| Benchmark | MedRAG[61]   | 2024.02 | Accuracy      | -   | Accuracy     |
Consistency
|           |             |         | Correctness |     | HumanEvaluation |
| --------- | ----------- | ------- | ----------- | --- | --------------- |
| Benchmark | FeB4RAG[57] | 2024.02 |             | -   |                 |
|           |             |         | Clarity     |     | HumanEvaluation |
Coverage
| Benchmark | CDQA[62] | 2024.03 | Accuracy | -   | F1  |
| --------- | -------- | ------- | -------- | --- | --- |
Correctness
F1,Exact-Match
Faithfulness
| Benchmark | DomainRAG[58] | 2024.06 |     | -   | Rouge-L |
| --------- | ------------- | ------- | --- | --- | ------- |
NoiseRobustness
LLMasaJudge
StructuralOutput
F1,Exacct-Match
| Benchmark | ReEval[66] | 2024.06 | Hallucination | -   | LLMasaJudge |
| --------- | ---------- | ------- | ------------- | --- | ----------- |
HumanEvaluation
Latency
| Research | FiD-Light[20]        | 2023.07 |           | -              | -   |
| -------- | -------------------- | ------- | --------- | -------------- | --- |
| Research | DiversityReranker[4] | 2023.08 | Diversity | CosineDistance | -   |

EvaluationofRetrieval-AugmentedGeneration:ASurvey 7
2024.Table1portraysthisinformation,whereeachevaluationcriterionisrepresented
byadifferentcolour.Forexample,FeB4RAG[57],thefourthfromthelast,hasposited
fourstandardsbasedon[17]thatcompriseConsistency,Correctness,Clarity,andCov-
erage.Correctnessisequivalenttoaccuracyinretrieval,andConsistencyistantamount
to faithfulness in the generation component. While accuracy in retrieval gauges the
correctnessoftheretrievedinformation,wepositthatCoveragepertainstothecover-
agerateandismoreassociatedwithdiversity.Therefore,weconsiderCoveragetobe
linkedwithdiversityandanadditionalrequirementinourproposedevaluationframe-
work,whichwillbeintroducedsubsequently.Theremainingstandard,Clarity,isalso
classifiedasanadditionalrequirementinourproposedframework.Theothertoolsand
benchmarksareprocessedsimilarly.
Toolsandbenchmarksoffervaryingdegreesofflexibilityinevaluatingdatasetsfor
RAGsystems.Tools,whichspecifyonlyevaluationtargets,provideaversatileframe-
workcapable ofconstructingcompleteRAGapplications andevaluationpipelines,as
seen in works like [54,32,33]. Benchmarks, on the other hand, focus on different as-
pects of RAG evaluation with specific emphasis on either retrieval outputs or genera-
tiontargets.Forinstance,RAGAs[14]andARES[49]assesstherelevanceofretrieval
documents, while RGB and MultiHop-RAG [6,52] prioritize accuracy, necessitating
comparisonwithGTs.The[66]focusesontheHallucination,whichisacombination
offaithfulnessandcorrectness.Allbenchmarksconsidergenerationtargetsduetotheir
criticalroleinRAGsystems,thoughtheirfocusareasvary.
AdditionalRequirement Inadditiontoevaluatingthetwoprimarycomponentsout-
lined, a portion of the works also addressed some additional requirements of RAG
(BlackandItalicstargetsinTable2).Therequirementsareasfollows:
- Latency [20,32] measures how quickly the system can find information and re-
spond,crucialforuserexperience.
- Diversity[4,32]checksifthesystemretrievesavarietyofrelevantdocumentsand
generatesdiverseresponses.
- NoiseRobustness[6]assesseshowwellthesystemhandlesirrelevantinformation
withoutaffectingresponsequality.
- Negative Rejection [6] gauges the system’s ability to refrain from providing a
responsewhentheavailableinformationisinsufficient.
- Counterfactual Robustness [6] evaluates the system’s capacity to identify and
disregardincorrectinformation,evenwhenalertedaboutpotentialmisinformation.
- More: For more human preferences considerations, there can be more additional
requirements,suchasreadability[57,33],toxicity,perplexity[33],etc.
For the exception, CRUD-RAG [39] introduces a comprehensive benchmark ad-
dressing the broader spectrum of RAG applications beyond question-answering, cat-
egorized into Create, Read, Update, and Delete scenarios. This benchmark evaluates
RAG systems across diverse tasks, including text continuation, question answering,
hallucination modification, and multi-document summarization. It offers insights for
optimizingRAGtechnologyacrossdifferentscenarios.DomainRAG[58]identifiessix
complexabilitiesforRAGsystems:conversational,structuralinformation,faithfulness,

HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
8
denoising, time-sensitive problem solving, and multi-doc understanding. ReEval [66]
specificallytargetshallucinationevaluationbyemployingacost-effectiveLLM-based
frameworkthatutilizespromptchainingtocreatedynamictestcases.
Table 2:
| The evaluation | datasets | used for each benchmark. | The dataset | without citation was |
| -------------- | -------- | ------------------------ | ----------- | -------------------- |
constructedbythebenchmarkitself.
|            | Benchmark | Dataset            |     |     |
| ---------- | --------- | ------------------ | --- | --- |
|            | RAGAs[14] | WikiEval           |     |     |
| RECALL[38] |           | EventKG[19],UJ[22] |     |     |
NQ[29],Hotpot[63],
|     | ARES[49] | FEVER[53],WoW[11], |     |     |
| --- | -------- | ------------------ | --- | --- |
MultiRC[10],ReCoRD[71]
|                  | RGB[6] | Generated(Source:News) |     |     |
| ---------------- | ------ | ---------------------- | --- | --- |
| MultiHop-RAG[52] |        | Generated(Source:News) |     |     |
Generated(Source:News)
CRUD-RAG[39]
UHGEval[36]
| MedRAG[61]    |                                                | MIRAGE                           |     |     |
| ------------- | ---------------------------------------------- | -------------------------------- | --- | --- |
| FeB4RAG[57]   |                                                | FeB4RAG,BEIR[26]                 |     |     |
|               | CDQA[62]                                       | Generation(Source:News),Labeller |     |     |
| DomainRAG[58] | Generation(Source:CollegeAdmissionInformation) |                                  |     |     |
|               | ReEval[66]                                     | RealTimeQA[27],NQ[15,29])        |     |     |
3.2 EvaluationDataset(Howtoevaluate?)
InTable2,distinctbenchmarksemployvaryingstrategiesfordatasetconstruction,rang-
ingfromleveragingexistingresourcestogeneratingentirelynewdatatailoredforspe-
cificevaluationaspects.SeveralbenchmarksdrawuponthepartofKILT(Knowledge
Intensive Language Tasks) benchmark [44] (Natural Questions [29], HotpotQA [63],
and FEVER [53]) and other established datasets such as SuperGLUE [56] (MultiRC
[10],andReCoRD[71])[49].However,thedrawbackofusingsuchdatasetscan’tsolve
thechallengesindynamicreal-worldscenarios.Asimilarsituationcanbeobservedin
WikiEval,fromWikipediapagespost2022,constructedbyRAGAs[14].
| The advent | of powerful LLMs | has revolutionized | the process | of dataset construc- |
| ---------- | ---------------- | ------------------ | ----------- | -------------------- |
tion.Withtheabilitytodesignqueriesandgroundtruthsforspecificevaluationtargets
usingtheseframeworks,authorscannowcreatedatasetsinthedesiredformatwithease.
Benchmarks like RGB, MultiHop-RAG, CRUD-RAG, and CDQA [6,52,39,62] have
taken this approach further by building their own datasets using online news articles
totestRAGsystems’abilitytohandlereal-worldinformationbeyondthetrainingdata
of LM frameworks. Most recently, DomainRAG [58] combines various types of QA
datasetswithsingle-doc,multi-doc,single-round,andmulti-round.Thesedatasetsare
generatedfromtheyearlychangedinformationfromthecollegewebsiteforadmission
andenrollment,whichforcestheLLMstousetheprovidedandupdatedinformation.

EvaluationofRetrieval-AugmentedGeneration:ASurvey 9
In summary, the creation and selection of datasets are crucial for evaluating RAG
systems.Datasetstailoredforspecificmetricsortasksimproveevaluationaccuracyand
guidethedevelopmentofadaptableRAGsystemsforreal-worldinformationneeds.
3.3 EvaluationMetric(Howtoquantify?)
NavigatingtheintricateterrainofevaluatingRAGsystemsnecessitatesanuancedun-
derstandingofthemetricsthatcanpreciselyquantifytheevaluationtargets.However,
creatingevaluativecriteriathatalignwithhumanpreferencesandaddresspracticalcon-
siderationsischallenging.EachcomponentwithintheRAGsystemsrequiresatailored
evaluativeapproachthatreflectsitsdistinctfunctionalitiesandobjectives.
Retrieval Metrics Various targets can be evaluated with various metrics that corre-
spondtothegivendatasets.Thissectionwillintroduceseveralcommonlyusedmetrics
forretrievalandgenerationtargets.Themetricsforadditionalrequirementscanalsobe
foundinthesecommonlyusedmetrics.Themorespecificallydesignedmetricscanbe
exploredintheoriginalpaperviaTable1asareference.
Fortheretrievalevaluation,thefocusisonmetricsthatcanaccuratelycapturethe
relevance,accuracy,diversity,androbustnessoftheinformationretrievedinresponseto
queries.Thesemetricsmustnotonlyreflectthesystem’sprecisioninfetchingpertinent
informationbutalsoitsresilienceinnavigatingthedynamic,vast,andsometimesmis-
leading landscape of available data. The deployment of metrics like Misleading Rate,
MistakeReappearanceRate,andErrorDetectionRatewithinthe[38]benchmarkun-
derscoresaheightenedawarenessofRAGsystems’inherentintricacies.Theintegration
ofMAP@K,MRR@K,andTokenizationwithF1intobenchmarkslike[52,62]mirrors
adeepeningcomprehensionoftraditionalretrieval’smultifacetedevaluation.Whilethe
[17]alsoemphasizesthatthisranking-basedevaluationmethodologyisnotunsuitable
fortheRAGsystem,andshouldhavemoreRAG-specificretrievalevaluationmetrics.
Thesemetricsnotonlycapturetheprecisionandrecallofretrievalsystemsbutalsoac-
countforthediversityandrelevanceofretrieveddocuments,aligningwiththecomplex
anddynamicnatureofinformationneedsinRAGsystems.TheintroductionofLLMs
asevaluativejudges,asseenin[14],furtherunderscorestheadaptabilityandversatility
ofretrievalevaluation,offeringacomprehensiveandcontext-awareapproachtoassess-
ingretrievalquality.
Non-Rank Based Metrics often assess binary outcomes—whether an item is relevant
or not—without considering the position of the item in a ranked list. Notice, that the
followingformulaisjustoneformatofthesemetrics,thedefinitionofeachmetricmay
varybythedifferentevaluatingtasks.
- Accuracy isthe proportionof trueresults (bothtrue positivesand truenegatives)
amongthetotalnumberofcasesexamined.
- Precisionisthefractionofrelevantinstancesamongtheretrievedinstances,
TP
Precision=
TP +FP
whereTP representstruepositivesandFP representsfalsepositives.

HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
10
- Recallatk(Recall@k)isthefractionofrelevantinstancesthathavebeenretrieved
overthetotalamountofrelevantcases,consideringonlythetopkresults.
|     |     |            | |RD∩Top | |   |     |
| --- | --- | ---------- | ------- | --- | --- |
|     |     | Recall@k = | kd      |     |     |
|RD|
| whereRDistherelevantdocuments,andTop |     |     | kd isthetop-kretrieveddocuments. |     |     |
| ------------------------------------ | --- | --- | -------------------------------- | --- | --- |
Rank-Based Metrics evaluate the order in which relevant items are presented, with
higherimportanceplacedonthepositioningofrelevantitemsattherankinglist.
MeanReciprocalRank(MRR)istheaverageofthereciprocalranksofthefirst
-
correctanswerforasetofqueries.
|Q|
1 (cid:88) 1
MRR=
|     |     |     | |Q| rank i |     |     |
| --- | --- | --- | ---------- | --- | --- |
i=1
| where|Q|isthenumberofqueriesandrank |     |     | istherankpositionofthefirstrele- |     |     |
| ----------------------------------- | --- | --- | -------------------------------- | --- | --- |
i
vantdocumentforthei-thquery.
- Mean Average Precision (MAP) is the mean of the average precision scores for
eachquery.
|Q| (cid:80)n
|     |     | 1 (cid:88) | (P(k)×rel(k))      |     |     |
| --- | --- | ---------- | ------------------ | --- | --- |
|     | MAP | =          | k=1                |     |     |
|     |     | |Q|        | |relevantdocuments | |   |     |
q
q=1
| where P(k) | is the precision | at cutoff            | k in the list, rel(k) | is an indicator | function     |
| ---------- | ---------------- | -------------------- | --------------------- | --------------- | ------------ |
| equaling   | 1 if the item at | rank k is a relevant | document,             | 0 otherwise,    | and n is the |
numberofretrieveddocuments.
GenerationMetrics Intherealmofgeneration,evaluationtranscendsthemereaccu-
racy of generated responses, venturing into the quality of text in terms of coherence,
relevance,fluency,andalignmentwithhumanjudgment.Thisnecessitatesmetricsthat
can assess the nuanced aspects of language production, including factual correctness,
readability,andusersatisfactionwiththegeneratedcontent.Thetraditionalmetricslike
BLEU,ROUGE,andF1Scorecontinuetoplayacrucialrole,emphasizingthesignifi-
canceofprecisionandrecallindeterminingresponsequality.Yet,theadventofmetrics
suchasMisleadingRate,MistakeReappearanceRate,andErrorDetectionRatehigh-
lightsanevolvingunderstandingofRAGsystems’distinctchallenges[38].
| The evaluation | done by | humans is still | a very significant | standard to | compare the |
| -------------- | ------- | --------------- | ------------------ | ----------- | ----------- |
performance of generation models with one another or with the ground truth. The
approach of employing LLMs as evaluative judges [75] is a versatile and automatic
method for quality assessment, catering to instances where traditional ground truths
may be elusive [14]. This methodology benefits from employing prediction-powered
inference (PPI) and context relevance scoring, offering a nuanced lens through which
LLM output can be assessed. [49] The strategic use of detailed prompt templates en-
sures a guided assessment aligned with human preferences, effectively standardizing
evaluationsacrossvariouscontentdimensions[1].ThisshifttowardsleveragingLLMs

EvaluationofRetrieval-AugmentedGeneration:ASurvey 11
as arbiters mark a significant progression towards automated and context-responsive
evaluation frameworks, enriching the evaluation landscape with minimal reliance on
referencecomparisons.
- ROUGE Recall-Oriented Understudy for Gisting Evaluation (ROUGE) [37] is a
set of metrics designed to evaluate the quality of summaries by comparing them
tohuman-generatedreferencesummaries.ROUGEcanbeindicativeofthecontent
overlapbetweenthegeneratedtextandthereferencetext.ThevariantsofROUGEs
measure the overlap of n-grams (ROUGE-N, ROUGGE-W), word subsequences
(ROUGE-L,ROUGGE-S),andwordpairsbetweenthesystem-generatedsummary
andthereferencesummaries.
- BLEUBilingualEvaluationUnderstudy(BLEU)[43]isametricforevaluatingthe
qualityofmachine-translatedtextagainstoneormorereferencetranslations.BLEU
calculates the precision of n-grams in the generated text compared to the refer-
encetextandthenappliesabrevitypenaltytodiscourageoverlyshorttranslations.
BLEUhaslimitations,suchasnotaccountingforthefluencyorgrammaticalityof
thegeneratedtext.
- BertScore BertScore [72] leverages the contextual embedding from pre-trained
transformerslikeBERTtoevaluatethesemanticsimilaritybetweengeneratedtext
andreferencetext.BertScorecomputestoken-levelsimilarityusingcontextualem-
bedding and produces precision, recall, and F1 scores. Unlike n-gram-based met-
rics,BertScorecapturesthemeaningofwordsincontext,makingitmorerobustto
paraphrasingandmoresensitivetosemanticequivalence.
- LLMasaJudgeUsing“LLMasaJudge”forevaluatinggeneratedtextisamore
recent approach. [75] In this method, LLMs are used to score the generated text
based on criteria such as coherence, relevance, and fluency. The LLM can be op-
tionallyfinetunedonhumanjudgmentstopredictthequalityofunseentextorused
togenerateevaluationsinazero-shotorfew-shotsetting.Thisapproachleverages
theLLM’sunderstandingoflanguageandcontexttoprovideamorenuancedtext
qualityassessment.Forinstance,[1]illustrateshowprovidingLLMjudgeswithde-
tailedscoringguidelines,suchasascalefrom1to5,canstandardizetheevaluation
process.Thismethodologyencompassescriticalaspectsofcontentassessment,in-
cludingcoherence,relevance, fluency,coverage,diversity,and detail-bothin the
contextofanswerevaluationandqueryformulation.
Additional Requirements These additional requirements, such as latency, diversity,
noise robustness, negative rejection, and counterfactual robustness, are used to ensure
thepracticalapplicabilityofRAGsystemsinreal-worldscenariosalignedwithhuman
preference. This section delves into the metrics used for evaluating these additional
requirements,highlightingtheirsignificanceinthecomprehensiveassessmentofRAG
systems.
LatencymeasuresthetimetakenbytheRAGsystemtofinishtheresponseofone
query. It is a critical factor for user experience, especially in interactive applications
suchaschatbotsorsearchengines[20].SingleQueryLatency:Themeantimeistaken
toprocessasinglequery,includingbothretrievalandgeneratingphases.

12 HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
Diversityevaluatesthevarietyandbreadthofinformationretrievedandgenerated
by the RAG system. It ensures that the system can provide a wide range of perspec-
tivesandavoidredundancyinresponses[4].CosineSimilarity/CosineDistance:The
cosine similarity/distance calculates embeddings of retrieved documents or generated
responses.[30]Lowercosinesimilarityscoresindicatehigherdiversity,suggestingthat
thesystemcanretrieveorgenerateabroaderspectrumofinformation.
NoiseRobustnessmeasurestheRAGsystem’sabilitytohandleirrelevantormis-
leadinginformationwithoutcompromisingthequalityoftheresponse[38].Themetrics
MisleadingRateandMistakeReappearanceRatearedescribedin[38],providingde-
taileddescriptionstailoredtothespecificdatasetandexperimentalsetup.[58]
Negative Rejection evaluates the system’s capability to withhold responses when
theavailableinformationisinsufficientortooambiguoustoprovideanaccurateanswer
[6].RejectionRate:Therateatwhichthesystemrefrainsfromgeneratingaresponse.
CounterfactualRobustnessCounterfactualrobustnessassessesthesystem’sabil-
itytoidentifyanddisregardincorrectorcounterfactualinformationwithintheretrieved
documents[39].ErrorDetectionRate:Theratioofcounterfactualstatementsdetected
inretrievedinformation.
4 Discussion
For RAG systems, traditional Question Answering (QA) datasets and metrics remain
a common format for interaction. [14,49,38,6,61,62,58,66] While these provide a ba-
sicverificationofRAG’scapabilities,itbecomeschallengingtodistinguishtheimpact
ofretrievalcomponentswhenfacedwithstrongLanguageModels(LLMs)capableof
excelling in QA benchmarks. To comprehensively evaluate the performance of entire
RAGsystems,thereisaneedfordiverseandRAG-specificbenchmarks.Severalpapers
offerguidanceonimprovingQAformatbenchmarks,includingvariationsinquestion
types:fromsimpleWikipediafillingquestionstomulti-hop[52],multi-documentques-
tions[66]andsingle-roundtomulti-rounddialogue[39,58].Foranswers,aspectssuch
asstructuraloutput[58],contentmoderation[6,54],andhallucination[66]canbecon-
sidered when evaluating relevance, faithfulness, and correctness. In addition to these,
RAG systems require additional requirements such as robustness to noisy documents,
language expression, latency, and result diversity. [32,33,38,6,39,57,58,20,4] Further-
more, research is needed on performance changes involving intermediate outputs and
retrieveddocuments,aswellastherelationshipandanalysisbetweenretrievalmetrics
andfinalgenerationoutputs.
Regardingdatasets,creatingauniversaldatasetwaschallengingduetothetarget-
specific nature of different RAG benchmarks. Tailored datasets [14,38,49,39,57] are
necessary for a thorough evaluation, but this approach increases the effort and re-
sources required. Moreover, the diversity of datasets, from news articles to structured
databases[66],reflectstheadaptabilityrequiredofRAGsystemsbutalsoposesabar-
rier to streamlined evaluation. Recently, with the cutting-edge performance of LLMs,
complexdataprocessingandautomaticQApairgenerationcanbeautomatedtoachieve
daily or finer-grained time resolution, preventing LLMs from cheating and evaluating
therobustnessofRAGsystemsinrapidlychangingdata.[6,52,39,62,58,66]

EvaluationofRetrieval-AugmentedGeneration:ASurvey 13
Whenitcomestometrics,theuseofLLMsasautomaticevaluativejudgessignifies
aburgeoningtrend,promisingversatilityanddepthingenerativeoutputswithreason-
ingonalargescalecomparedtohumanevaluation.However,using“LLMsasaJudge”
[75] for responses presents challenges in aligning with human judgment, establishing
effective grading scales, and applying consistent evaluation across varied use cases.
Determining correctness, clarity, and richness can differ between automated and hu-
manassessments.Moreover,theeffectivenessofexample-basedscoringcanvary,and
there’s no universally applicable grading scale and prompting text, complicating the
standardizationof“LLMasaJudge”.[33]
Inadditiontothechallengesmentionedabove,itisimportanttoconsidertheresource-
intensivenature[76]ofusingLargeLanguageModels(LLMs)fordatagenerationand
validation. RAG benchmarks must balance the need for thorough evaluation with the
practicalconstraintsoflimitedcomputationalresources.Assuch,itisdesirabletode-
velopevaluationmethodologiesthatcaneffectivelyassessRAGsystemsusingsmaller
amountsofdatawhilemaintainingthevalidityandreliabilityoftheresults.
5 Conclusion
ThissurveysystematicallyexploresthecomplexitiesofevaluatingRAGsystems,high-
lightingthechallengesinassessingtheirperformance.ThroughtheproposedAUnified
EvaluationProcessofRAG,weoutlineastructuredapproachtoanalyzingRAGevalua-
tions,focusingontargets,datasetsandmeasures.Ouranalysisemphasizestheneedfor
targetedbenchmarksthatreflectthedynamicinterplaybetweenretrievalaccuracyand
generativequalityandpracticalconsiderationsforreal-worldapplications.Byidentify-
inggapsincurrentmethodologiesandsuggestingfutureresearchdirections,weaimto
contributetomoreeffective,anduser-alignedbenchmarksofRAGsystems.

HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
14
References
1. Balaguer,A.,Benara,V.,Cunha,R.L.d.F.,Filho,R.d.M.E.,Hendry,T.,Holstein,D.,Mars-
| man, J., | Mecklenburg, | N.,          | Malvar, | S., Nunes, | L.O.,        | Padilha,   | R., Sharp, | M., | Silva, B., |
| -------- | ------------ | ------------ | ------- | ---------- | ------------ | ---------- | ---------- | --- | ---------- |
| Sharma,  | S., Aski,    | V., Chandra, | R.:     | RAG vs     | Fine-tuning: | Pipelines, | Tradeoffs, |     | and a Case |
StudyonAgriculture.Tech.rep.(Jan2024),http://arxiv.org/abs/2401.08406,
arXiv:2401.08406[cs]type:article
2. Barnett,S.,Kurniawan,S.,Thudumu,S.,Brannelly,Z.,Abdelrazek,M.:Sevenfailurepoints
| when engineering |     | a retrieval | augmented | generation |     | system (Jan | 2024). | https://doi. |     |
| ---------------- | --- | ----------- | --------- | ---------- | --- | ----------- | ------ | ------------ | --- |
org/10.48550/ARXIV.2401.05856
3. Besta,M.,Blach,N.,Kubicek,A.,Gerstenberger,R.,Podstawski,M.,Gianinazzi,L.,Gajda,
| J., Lehmann, | T.,          | Niewiadomski, | H.,       | Nyczyk, | P.,         | Hoefler, T.: Graph        | of       | thoughts:  | Solving |
| ------------ | ------------ | ------------- | --------- | ------- | ----------- | ------------------------- | -------- | ---------- | ------- |
| elaborate    | problems     | with large    | language  | models. | Proceedings | of                        | the AAAI | Conference | on      |
| Artificial   | Intelligence | 2024          | (AAAI’24) | (Aug    | 2023).      | https://doi.org/10.48550/ |          |            |         |
ARXIV.2308.09687
4. Blagojevic, V.: Enhancing RAG Pipelines in Haystack: Introducing DiversityRanker
| and LostInTheMiddleRanker |     |     | (Aug | 2023), | https://towardsdatascience.com/ |     |     |     |     |
| ------------------------- | --- | --- | ---- | ------ | ------------------------------- | --- | --- | --- | --- |
enhancing-rag-pipelines-in-haystack-45f14e2bc9f5
5. Chang,Y.,Wang,X.,Wang,J.,Wu,Y.,Yang,L.,Zhu,K.,Chen,H.,Yi,X.,Wang,C.,Wang,
Y.,etal.:Asurveyonevaluationoflargelanguagemodels.ACMTransactionsonIntelligent
SystemsandTechnology15(3),1–45(2024)
6. Chen, J., Lin, H., Han, X., Sun, L.: Benchmarking large language models in retrieval-
| augmented | generation | (Sep | 2023). | https://doi.org/10.48550/ARXIV.2309. |     |     |     |     |     |
| --------- | ---------- | ---- | ------ | ------------------------------------ | --- | --- | --- | --- | --- |
01431
7. Cuconasu,F.,Trappolini,G.,Siciliano,F.,Filice,S.,Campagnano,C.,Maarek,Y.,Tonel-
lotto,N.,Silvestri,F.:Thepowerofnoise:Redefiningretrievalforragsystems(Jan2024).
https://doi.org/10.48550/ARXIV.2401.14887
8. Deng,Y.,Zhang,W.,Chen,Z.,Gu,Q.:Rephraseandrespond:Letlargelanguagemodelsask
betterquestionsforthemselves(Nov2023).https://doi.org/10.48550/ARXIV.
2311.04205
9. Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: BERT: Pre-training of Deep Bidirec-
| tional Transformers |               | for Language |                 | Understanding. |          | In: Burstein,  | J., Doran, | C.,    | Solorio, T. |
| ------------------- | ------------- | ------------ | --------------- | -------------- | -------- | -------------- | ---------- | ------ | ----------- |
| (eds.) Proceedings  |               | of the       | 2019 Conference |                | of the   | North American | Chapter    | of     | the Asso-   |
| ciation for         | Computational |              | Linguistics:    | Human          | Language | Technologies,  |            | Volume | 1 (Long     |
andShortPapers).pp.4171–4186.AssociationforComputationalLinguistics,Minneapo-
lis,Minnesota(Jun2019).https://doi.org/10.18653/v1/N19-1423,https:
//aclanthology.org/N19-1423
10. DeYoung,J.,Jain,S.,Rajani,N.F.,Lehman,E.,Xiong,C.,Socher,R.,Wallace,B.C.:Eraser:
Abenchmarktoevaluaterationalizednlpmodels
11. Dinan, E., Roller, S., Shuster, K., Fan, A., Auli, M., Weston, J.: Wizard of Wikipedia:
Knowledge-poweredconversationalagents.In:ProceedingsoftheInternationalConference
onLearningRepresentations(ICLR)(2019)
12. Douze,M.,Guzhva,A.,Deng,C.,Johnson,J.,Szilvasy,G.,Mazaré,P.E.,Lomeli,M.,Hos-
seini,L.,Jégou,H.:Thefaisslibrary(2024)
13. DuckDuckGo: DuckDuckGo — Privacy, simplified. (2024), https://duckduckgo.
com//home
14. Es, S., James, J., Espinosa-Anke, L., Schockaert, S.: Ragas: Automated evaluation of
| retrieval | augmented | generation | (Sep | 2023). | https://doi.org/10.48550/ARXIV. |     |     |     |     |
| --------- | --------- | ---------- | ---- | ------ | ------------------------------- | --- | --- | --- | --- |
2309.15217

|     |     | EvaluationofRetrieval-AugmentedGeneration:ASurvey |     |     |     |     |     |     | 15  |
| --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
15. Fisch, A., Talmor, A., Jia, R., Seo, M., Choi, E., Chen, D.: MRQA 2019 shared task:
| Evaluating       | generalization |            | in reading                            | comprehension. |        | In: Fisch,        | A., Talmor,  | A.,     | Jia, R., |
| ---------------- | -------------- | ---------- | ------------------------------------- | -------------- | ------ | ----------------- | ------------ | ------- | -------- |
| Seo, M.,         | Choi, E.,      | Chen,      | D. (eds.)                             | Proceedings    | of the | 2nd Workshop      | on           | Machine | Read-    |
| ing for Question |                | Answering. | pp. 1–13.                             | Association    |        | for Computational | Linguistics, |         | Hong     |
|                  |                |            | https://doi.org/10.18653/v1/D19-5801, |                |        |                   |              |         | https:   |
| Kong, China      | (Nov           | 2019).     |                                       |                |        |                   |              |         |          |
//aclanthology.org/D19-5801
16. Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Guo, Q., Wang, M.,
Wang,H.:Retrieval-AugmentedGenerationforLargeLanguageModels:ASurvey.Tech.
rep.(Jan2024),http://arxiv.org/abs/2312.10997,arXiv:2312.10997[cs]type:
article
17. Gienapp,L.,Scells,H.,Deckers,N.,Bevendorff,J.,Wang,S.,Kiesel,J.,Syed,S.,Fröbe,
| M., Zuccon, | G., | Stein, | B., Hagen, | M., Potthast, | M.: | Evaluating | Generative | Ad  | Hoc In- |
| ----------- | --- | ------ | ---------- | ------------- | --- | ---------- | ---------- | --- | ------- |
formationRetrieval.Tech.rep.(Nov2023),http://arxiv.org/abs/2311.04694,
arXiv:2311.04694[cs]type:article
18. Google: Programmable Search Engine | Google for Developers (2024), https://
developers.google.com/custom-search
19. Gottschalk, S., Demidova, E.: Eventkg: A multilingual event-centric temporal knowledge
graph(Apr2018).https://doi.org/10.48550/ARXIV.1804.04526
20. Hofstätter, S., Chen, J., Raman, K., Zamani, H.: FiD-Light: Efficient and Effective
| Retrieval-Augmented                             |      | Text        | Generation. | In:         | Proceedings | of             | the 46th International |         | ACM   |
| ----------------------------------------------- | ---- | ----------- | ----------- | ----------- | ----------- | -------------- | ---------------------- | ------- | ----- |
| SIGIR Conference                                |      | on Research | and         | Development |             | in Information | Retrieval.             | pp.     | 1437– |
| 1447. SIGIR                                     | ’23, | Association | for         | Computing   | Machinery,  |                | New York,              | NY, USA | (Jul  |
| 2023). https://doi.org/10.1145/3539618.3591687, |      |             |             |             |             |                | https://doi.org/       |         |       |
10.1145/3539618.3591687
21. Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,S.,Wang,L.,Chen,W.:LoRA:
Low-RankAdaptationofLargeLanguageModels.Tech.rep.(Oct2021).https://doi.
org/10.48550/arXiv.2106.09685,http://arxiv.org/abs/2106.09685,
arXiv:2106.09685[cs]type:article
22. Huang,J.,Shao,H.,Chang,K.C.C.,Xiong,J.,Hwu,W.m.:Understandingjargon:Combin-
ingextractionandgenerationfordefinitionmodeling.In:ProceedingsofEMNLP(2022)
23. Huang,L.,Yu,W.,Ma,W.,Zhong,W.,Feng,Z.,Wang,H.,Chen,Q.,Peng,W.,Feng,X.,
Qin,B.,Liu,T.:Asurveyonhallucinationinlargelanguagemodels:Principles,taxonomy,
challenges,andopenquestions(Nov2023).https://doi.org/10.48550/ARXIV.
2311.05232
24. Huang, Y., Huang, J.: A survey on retrieval-augmented text generation for large language
models(Apr2024).https://doi.org/10.48550/ARXIV.2404.10981
25. Johnson,J.,Douze,M.,Jégou,H.:Billion-scalesimilaritysearchwithGPUs.IEEETrans-
actionsonBigData7(3),535–547(2019)
26. Kamalloo,E.,Thakur,N.,Lassance,C.,Ma,X.,Yang,J.H.,Lin,J.:Resourcesforbrewing
beir:Reproduciblereferencemodelsandanofficialleaderboard(2023)
27. Kasai, J., Sakaguchi, K., Takahashi, Y., Bras, R.L., Asai, A., Yu, X., Radev, D., Smith,
N.A.,Choi,Y.,Inui,K.:Realtimeqa:What’stheanswerrightnow?(Jul2022).https://
| doi.org/10.48550/ARXIV.2207.13332, |     |     |     |     | https://arxiv.org/abs/2207. |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- |
13332
28. Khattab,O.,Zaharia,M.:Colbert:Efficientandeffectivepassagesearchviacontextualized
lateinteractionoverbert(Apr2020).https://doi.org/10.48550/ARXIV.2004.
12832
29. Kwiatkowski, T., Palomaki, J., Redfield, O., Collins, M., Parikh, A., Alberti, C., Epstein,
D.,Polosukhin,I.,Devlin,J.,Lee,K.,Toutanova,K.,Jones,L.,Kelcey,M.,Chang,M.W.,
| Dai, A.M., | Uszkoreit, | J., | Le, Q., Petrov, | S.: | Natural | questions: | A benchmark | for | question |
| ---------- | ---------- | --- | --------------- | --- | ------- | ---------- | ----------- | --- | -------- |

16 HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
answeringresearch.TransactionsoftheAssociationforComputationalLinguistics7,453–
466(2019).https://doi.org/10.1162/tacl_a_00276,https://doi.org/
10.1162/tacl_a_00276
30. Lahitani,A.R.,Permanasari,A.E.,Setiawan,N.A.:Cosinesimilaritytodeterminesimilar-
itymeasure:Studycaseinonlineessayassessment.In:20164thInternationalConference
onCyberandITServiceManagement.pp.1–6(2016).https://doi.org/10.1109/
CITSM.2016.7577578
31. Lanchantin, J., Toshniwal, S., Weston, J., Szlam, A., Sukhbaatar, S.: Learning to reason
and memorize with self-notes (May 2023). https://doi.org/10.48550/ARXIV.
2305.00833
32. LangChain: Evaluating rag architectures on benchmark tasks (Nov 2023), https:
//langchain-ai.github.io/langchain-benchmarks/notebooks/
retrieval/langchain_docs_qa.html
33. Leng, Q., Uhlenhuth, K., Polyzotis, A.: Best Practices for LLM Evaluation of
RAG Applications (Dec 2023), https://www.databricks.com/blog/
LLM-auto-eval-best-practices-RAG
34. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis,
M., Yih, W.t., Rocktäschel, T., Riedel, S., Kiela, D.: Retrieval-augmented generation for
knowledge-intensive NLP tasks. In: Proceedings of the 34th International Conference on
NeuralInformationProcessingSystems.pp.9459–9474.NIPS’20,CurranAssociatesInc.,
RedHook,NY,USA(Dec2020)
35. Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis,
M., Yih, W.t., Rocktäschel, T., Riedel, S., Kiela, D.: Retrieval-Augmented Generation for
Knowledge-Intensive NLP Tasks. Tech. rep. (Apr 2021), http://arxiv.org/abs/
2005.11401,arXiv:2005.11401[cs]type:article
36. Liang,X.,Song,S.,Niu,S.,Li,Z.,Xiong,F.,Tang,B.,Wy,Z.,He,D.,Cheng,P.,Wang,Z.,
Deng,H.:Uhgeval:Benchmarkingthehallucinationofchineselargelanguagemodelsvia
unconstrainedgeneration.arXivpreprintarXiv:2311.15296(2023)
37. Lin,C.Y.:ROUGE:Apackageforautomaticevaluationofsummaries.In:TextSummariza-
tionBranchesOut.pp.74–81.AssociationforComputationalLinguistics,Barcelona,Spain
(Jul2004),https://aclanthology.org/W04-1013
38. Liu,Y.,Huang,L.,Li,S.,Chen,S.,Zhou,H.,Meng,F.,Zhou,J.,Sun,X.:Recall:Abench-
markforllmsrobustnessagainstexternalcounterfactualknowledge(Nov2023).https:
//doi.org/10.48550/ARXIV.2311.08147
39. Lyu,Y.,Li,Z.,Niu,S.,Xiong,F.,Tang,B.,Wang,W.,Wu,H.,Liu,H.,Xu,T.,Chen,E.,Luo,
Y.,Cheng,P.,Deng,H.,Wang,Z.,Lu,Z.:Crud-rag:Acomprehensivechinesebenchmark
forretrieval-augmentedgenerationoflargelanguagemodels(Jan2024).https://doi.
org/10.48550/ARXIV.2401.17043
40. Microsoft: Web Search API | Microsoft Bing, https://www.microsoft.com/
en-us/bing/apis/bing-web-search-api
41. OpenAI,Achiam,J.,Adler,S.,Agarwal,S.,Ahmad,L.,Akkaya,I.,Aleman,F.L.,Almeida,
D., Altenschmidt, J., Altman, S., Anadkat, S., Avila, R., Babuschkin, I., Balaji, S., Bal-
com, V., Baltescu, P., Bao, H., Bavarian, M., Belgum, J., Bello, I., Berdine, J., Bernadett-
Shapiro, G., Berner, C., Bogdonoff, L., Boiko, O., Boyd, M., Brakman, A.L., Brockman,
G.,Brooks,T.,Brundage,M.,Button,K.,Cai,T.,Campbell,R.,Cann,A.,Carey,B.,Carl-
son, C., Carmichael, R., Chan, B., Chang, C., Chantzis, F., Chen, D., Chen, S., Chen, R.,
Chen,J.,Chen,M.,Chess,B.,Cho,C.,Chu,C.,Chung,H.W.,Cummings,D.,Currier,J.,
Dai,Y.,Decareaux,C.,Degry,T.,Deutsch,N.,Deville,D.,Dhar,A.,Dohan,D.,Dowling,
S., Dunning, S., Ecoffet, A., Eleti, A., Eloundou, T., Farhi, D., Fedus, L., Felix, N., Fish-
man, S.P., Forte, J., Fulford, I., Gao, L., Georges, E., Gibson, C., Goel, V., Gogineni, T.,

EvaluationofRetrieval-AugmentedGeneration:ASurvey 17
Goh,G.,Gontijo-Lopes,R.,Gordon,J.,Grafstein,M.,Gray,S.,Greene,R.,Gross,J.,Gu,
S.S.,Guo,Y.,Hallacy,C.,Han,J.,Harris,J.,He,Y.,Heaton,M.,Heidecke,J.,Hesse,C.,
Hickey,A.,Hickey,W.,Hoeschele,P.,Houghton,B.,Hsu,K.,Hu,S.,Hu,X.,Huizinga,J.,
Jain, S., Jain, S., Jang, J., Jiang, A., Jiang, R., Jin, H., Jin, D., Jomoto, S., Jonn, B., Jun,
H., Kaftan, T., Kamali, A., Kanitscheider, I., Keskar, N.S., Khan, T., Kilpatrick, L., Kim,
J.W.,Kim,C.,Kim,Y.,Kirchner,J.H.,Kiros,J.,Knight,M.,Kokotajlo,D.,Kondraciuk,A.,
Konstantinidis,A.,Kosic,K.,Krueger,G.,Kuo,V.,Lampe,M.,Lan,I.,Lee,T.,Leike,J.,
Leung,J.,Levy,D.,Li,C.M.,Lim,R.,Lin,M.,Lin,S.,Litwin,M.,Lopez,T.,Lowe,R.,
Lue, P., Makanju, A., Malfacini, K., Manning, S., Markov, T., Markovski, Y., Martin, B.,
Mayer,K.,Mayne,A.,McGrew,B.,McKinney,S.M.,McLeavey,C.,McMillan,P.,McNeil,
J.,Medina,D.,Mehta,A.,Menick,J.,Metz,L.,Mishchenko,A.,Mishkin,P.,Monaco,V.,
Morikawa,E.,Mossing,D.,Mu,T.,Murati,M.,Murk,O.,Mély,D.,Nair,A.,Nakano,R.,
Nayak,R.,Neelakantan,A.,Ngo,R.,Noh,H.,Ouyang,L.,O’Keefe,C.,Pachocki,J.,Paino,
A.,Palermo,J.,Pantuliano,A.,Parascandolo,G.,Parish,J.,Parparita,E.,Passos,A.,Pavlov,
M.,Peng,A.,Perelman,A.,Peres,F.d.A.B.,Petrov,M.,Pinto,H.P.d.O.,Michael,Pokorny,
Pokrass,M.,Pong,V.H.,Powell,T.,Power,A.,Power,B.,Proehl,E.,Puri,R.,Radford,A.,
Rae,J.,Ramesh,A.,Raymond,C.,Real,F.,Rimbach,K.,Ross,C.,Rotsted,B.,Roussez,
H., Ryder, N., Saltarelli, M., Sanders, T., Santurkar, S., Sastry, G., Schmidt, H., Schnurr,
D., Schulman, J., Selsam, D., Sheppard, K., Sherbakov, T., Shieh, J., Shoker, S., Shyam,
P., Sidor, S., Sigler, E., Simens, M., Sitkin, J., Slama, K., Sohl, I., Sokolowsky, B., Song,
Y.,Staudacher,N.,Such,F.P.,Summers,N.,Sutskever,I.,Tang,J.,Tezak,N.,Thompson,
M.B.,Tillet,P.,Tootoonchian,A.,Tseng,E.,Tuggle,P.,Turley,N.,Tworek,J.,Uribe,J.F.C.,
Vallone, A., Vijayvergiya, A., Voss, C., Wainwright, C., Wang, J.J., Wang, A., Wang, B.,
Ward,J.,Wei,J.,Weinmann,C.,Welihinda,A.,Welinder,P.,Weng,J.,Weng,L.,Wiethoff,
M.,Willner,D.,Winter,C.,Wolrich,S.,Wong,H.,Workman,L.,Wu,S.,Wu,J.,Wu,M.,
Xiao,K.,Xu,T.,Yoo,S.,Yu,K.,Yuan,Q.,Zaremba,W.,Zellers,R.,Zhang,C.,Zhang,M.,
Zhao,S.,Zheng,T.,Zhuang,J.,Zhuk,W.,Zoph,B.:GPT-4TechnicalReport(Mar2023).
https://doi.org/10.48550/ARXIV.2303.08774
42. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C.L., Mishkin, P., Zhang, C.,
Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens,
M., Askell, A., Welinder, P., Christiano, P., Leike, J., Lowe, R.: Training language mod-
els to follow instructions with human feedback. Tech. rep. (Mar 2022). https://doi.
org/10.48550/arXiv.2203.02155,http://arxiv.org/abs/2203.02155,
arXiv:2203.02155[cs]type:article
43. Papineni,K.,Roukos,S.,Ward,T.,Zhu,W.J.:Bleu:amethodforautomaticevaluationof
machinetranslation.In:Isabelle,P.,Charniak,E.,Lin,D.(eds.)Proceedingsofthe40thAn-
nualMeetingoftheAssociationforComputationalLinguistics.pp.311–318.Associationfor
ComputationalLinguistics,Philadelphia,Pennsylvania,USA(Jul2002).https://doi.
org/10.3115/1073083.1073135,https://aclanthology.org/P02-1040
44. Petroni,F.,Piktus,A.,Fan,A.,Lewis,P.,Yazdani,M.,DeCao,N.,Thorne,J.,Jernite,Y.,
Karpukhin, V., Maillard, J., Plachouras, V., Rocktäschel, T., Riedel, S.: KILT: a bench-
mark for knowledge intensive language tasks. In: Proceedings of the 2021 Conference
of the North American Chapter of the Association for Computational Linguistics: Hu-
man Language Technologies. pp. 2523–2544. Association for Computational Linguistics,
Online (Jun 2021). https://doi.org/10.18653/v1/2021.naacl-main.200,
https://aclanthology.org/2021.naacl-main.200
45. Radford,A.,Wu,J.,Child,R.,Luan,D.,Amodei,D.,Sutskever,I.,etal.:Languagemodels
areunsupervisedmultitasklearners.OpenAIblog1(8), 9(2019)
46. Ramos,J.,etal.:Usingtf-idftodeterminewordrelevanceindocumentqueries.In:Proceed-
ingsofthefirstinstructionalconferenceonmachinelearning.vol.242,pp.29–48.Citeseer

18 HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
(2003)
47. Robertson, S., Zaragoza, H., et al.: The probabilistic relevance framework: Bm25 and be-
yond.FoundationsandTrends®inInformationRetrieval3(4),333–389(2009)
48. Rosset,C.,Chung,H.L.,Qin,G.,Chau,E.C.,Feng,Z.,Awadallah,A.,Neville,J.,Rao,N.:
Researchyquestions:Adatasetofmulti-perspective,decompositionalquestionsforllmweb
agents(Feb2024).https://doi.org/10.48550/ARXIV.2402.17896
49. Saad-Falcon,J.,Khattab,O.,Potts,C.,Zaharia,M.:Ares:Anautomatedevaluationframe-
workforretrieval-augmentedgenerationsystems(Nov2023).https://doi.org/10.
48550/ARXIV.2311.09476
50. Sai,A.B.,Mohankumar,A.K.,Khapra,M.M.:Asurveyofevaluationmetricsusedfornlg
systems.ACMComputingSurveys(CSUR)55(2),1–39(2022)
51. Shahabi, C., Kolahdouzan, M.R., Sharifzadeh, M.: A road network embedding technique
fork-nearestneighborsearchinmovingobjectdatabases.In:Proceedingsofthe10thACM
internationalsymposiumonadvancesingeographicinformationsystems.pp.94–100(2002)
52. Tang,Y.,Yang,Y.:Multihop-rag:Benchmarkingretrieval-augmentedgenerationformulti-
hopqueries(Jan2024).https://doi.org/10.48550/ARXIV.2401.15391
53. Thorne,J.,Vlachos,A.,Christodoulopoulos,C.,Mittal,A.:FEVER:alarge-scaledatasetfor
factextractionandVERification.In:NAACL-HLT(2018)
54. TruLens: TruLens (2023), https://www.trulens.org/trulens_eval/
getting_started/quickstarts/quickstart/
55. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L.,
Polosukhin, I.: Attention isall you need (Jun 2017). https://doi.org/10.48550/
ARXIV.1706.03762
56. Wang, A., Pruksachatkun, Y., Nangia, N., Singh, A., Michael, J., Hill, F., Levy, O., Bow-
man,S.R.:SuperGLUE:Astickierbenchmarkforgeneral-purposelanguageunderstanding
systems.arXivpreprint1905.00537(2019)
57. Wang, S., Khramtsova, E., Zhuang, S., Zuccon, G.: Feb4rag: Evaluating federated search
in the context of retrieval augmented generation (Feb 2024). https://doi.org/10.
48550/ARXIV.2402.11891
58. Wang,S.,Liu,J.,Song,S.,Cheng,J.,Fu,Y.,Guo,P.,Fang,K.,Zhu,Y.,Dou,Z.:Domainrag:
A chinese benchmark for evaluating domain-specific retrieval-augmented generation (Jun
2024).https://doi.org/10.48550/ARXIV.2406.05654
59. Wei,J.,Tay,Y.,Bommasani,R.,Raffel,C.,Zoph,B.,Borgeaud,S.,Yogatama,D.,Bosma,
M.,Zhou,D.,Metzler,D.,Chi,E.H.,Hashimoto,T.,Vinyals,O.,Liang,P.,Dean,J.,Fedus,
W.: Emergent abilities of large language models (Jun 2022). https://doi.org/10.
48550/ARXIV.2206.07682
60. Wei,J.,Wang,X.,Schuurmans,D.,Bosma,M.,Ichter,B.,Xia,F.,Chi,E.,Le,Q.,Zhou,D.:
Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels(Jan2022).https:
//doi.org/10.48550/ARXIV.2201.11903
61. Xiong, G., Jin, Q., Lu, Z., Zhang, A.: Benchmarking retrieval-augmented generation for
medicine(Feb2024).https://doi.org/10.48550/ARXIV.2402.13178
62. Xu,Z.,Li,Y.,Ding,R.,Wang,X.,Chen,B.,Jiang,Y.,Zheng,H.T.,Lu,W.,Xie,P.,Huang,
F.:Letllmstakeonthelatestchallenges!achinesedynamicquestionansweringbenchmark
(Feb2024).https://doi.org/10.48550/ARXIV.2402.19248
63. Yang, Z., Qi, P., Zhang, S., Bengio, Y., Cohen, W.W., Salakhutdinov, R., Manning, C.D.:
HotpotQA:Adatasetfordiverse,explainablemulti-hopquestionanswering.In:Conference
onEmpiricalMethodsinNaturalLanguageProcessing(EMNLP)(2018)
64. Yao,J.Y.,Ning,K.P.,Liu,Z.H.,Ning,M.N.,Yuan,L.:Llmlies:Hallucinationsarenotbugs,
butfeaturesasadversarialexamples.arXivpreprintarXiv:2310.01469(2023)
65. Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T.L., Cao, Y., Narasimhan, K.: Tree of
Thoughts:Deliberateproblemsolvingwithlargelanguagemodels(2023)

|     | EvaluationofRetrieval-AugmentedGeneration:ASurvey |     |     |     |     |     |     | 19  |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
66. Yu,X.,Cheng,H.,Liu,X.,Roth,D.,Gao,J.:ReEval:Automatichallucinationevaluation
forretrieval-augmentedlargelanguagemodelsviatransferableadversarialattacks.In:Duh,
K.,Gomez,H.,Bethard,S.(eds.)FindingsoftheAssociationforComputationalLinguis-
tics:NAACL2024.pp.1333–1351.AssociationforComputationalLinguistics,MexicoCity,
Mexico(Jun2024),https://aclanthology.org/2024.findings-naacl.85
67. Zhang,K.,Liu,Q.,Qian,H.,Xiang,B.,Cui,Q.,Zhou,J.,Chen,E.:Eatn:Anefficientadap-
tivetransfernetworkforaspect-levelsentimentanalysis.IEEETransactionsonKnowledge
andDataEngineering35(1),377–389(2021)
68. Zhang, K., Zhang, H., Liu, Q., Zhao, H., Zhu, H., Chen, E.: Interactive attention transfer
networkforcross-domainsentimentclassification.In:ProceedingsoftheAAAIConference
onArtificialIntelligence.vol.33,pp.5773–5780(2019)
69. Zhang,K.,Zhang,K.,Zhang,M.,Zhao,H.,Liu,Q.,Wu,W.,Chen,E.:Incorporatingdy-
namicsemanticsintopre-trainedlanguagemodelforaspect-basedsentimentanalysis.arXiv
preprintarXiv:2203.16369(2022)
70. Zhang, Q., Chen, S., Xu, D., Cao, Q., Chen, X., Cohn, T., Fang, M.: A Survey for Ef-
| ficient Open | Domain Question | Answering. | In: | Rogers, | A., Boyd-Graber, |     | J., Okazaki, | N.  |
| ------------ | --------------- | ---------- | --- | ------- | ---------------- | --- | ------------ | --- |
(eds.)Proceedingsofthe61stAnnualMeetingoftheAssociationforComputationalLinguis-
tics(Volume1:LongPapers).pp.14447–14465.AssociationforComputationalLinguistics,
Toronto,Canada(Jul2023).https://doi.org/10.18653/v1/2023.acl-long.
808,https://aclanthology.org/2023.acl-long.808
71. Zhang, S., Liu, X., Liu, J., Gao, J., Duh, K., Van Durme, B.: Record: Bridging the gap
| between human | and machine | commonsense |     | reading | comprehension |     | (Oct 2018). | https: |
| ------------- | ----------- | ----------- | --- | ------- | ------------- | --- | ----------- | ------ |
//doi.org/10.48550/ARXIV.1810.12885
72. Zhang, T., Kishore, V., Wu, F., Weinberger, K.Q., Artzi, Y.: BERTScore: Evaluating Text
| Generation | with BERT. In: | 8th International |     | Conference | on  | Learning | Representations, |     |
| ---------- | -------------- | ----------------- | --- | ---------- | --- | -------- | ---------------- | --- |
ICLR2020,AddisAbaba,Ethiopia,April26-30,2020.OpenReview.net(2020),https:
//openreview.net/forum?id=SkeHuCVFDr
73. Zhang, Y., Khalifa, M., Logeswaran, L., Lee, M., Lee, H., Wang, L.: Merging Gener-
| ated and Retrieved                                      | Knowledge      | for Open-Domain |     | QA.           | In: Bouamor, |              | H., Pino,  | J., Bali, K. |
| ------------------------------------------------------- | -------------- | --------------- | --- | ------------- | ------------ | ------------ | ---------- | ------------ |
| (eds.) Proceedings                                      | of the 2023    | Conference      |     | on Empirical  | Methods      |              | in Natural | Language     |
| Processing.                                             | pp. 4710–4728. | Association     | for | Computational |              | Linguistics, | Singapore  | (Dec         |
| 2023). https://doi.org/10.18653/v1/2023.emnlp-main.286, |                |                 |     |               |              |              |            | https://     |
aclanthology.org/2023.emnlp-main.286
74. Zhao, P., Zhang, H., Yu, Q., Wang, Z., Geng, Y., Fu, F., Yang, L., Zhang, W., Cui, B.:
| Retrieval-augmented | generation | for ai-generated |     | content: | A   | survey | (Feb 2024). | https: |
| ------------------- | ---------- | ---------------- | --- | -------- | --- | ------ | ----------- | ------ |
//doi.org/10.48550/ARXIV.2402.19473
75. Zheng,L.,Chiang,W.L.,Sheng,Y.,Zhuang,S.,Wu,Z.,Zhuang,Y.,Lin,Z.,Li,Z.,Li,D.,
Xing,E.P.,Zhang,H.,Gonzalez,J.E.,Stoica,I.:Judgingllm-as-a-judgewithmt-benchand
chatbotarena(Jun2023).https://doi.org/10.48550/ARXIV.2306.05685
76. Zhou, Y., Lin, X., Zhang, X., Wang, M., Jiang, G., Lu, H., Wu, Y., Zhang, K., Yang, Z.,
Wang,K.,Sui,Y.,Jia,F.,Tang,Z.,Zhao,Y.,Zhang,H.,Yang,T.,Chen,W.,Mao,Y.,Li,
Y.,Bao,D.,Li,Y.,Liao,H.,Liu,T.,Liu,J.,Guo,J.,Zhao,X.,WEI,Y.,Qian,H.,Liu,Q.,
Wang,X.,Kin,W.,Chan,Li,C.,Li,Y.,Yang,S.,Yan,J.,Mou,C.,Han,S.,Jin,W.,Zhang,
G.,Zeng,X.:Ontheopportunitiesofgreencomputing:Asurvey(Nov2023)
77. Zhu, F., Lei, W., Wang, C., Zheng, J., Poria, S., Chua, T.S.: Retrieving and Reading:
| A Comprehensive | Survey on | Open-domain | Question |     | Answering. | Tech. | rep. (May | 2021), |
| --------------- | --------- | ----------- | -------- | --- | ---------- | ----- | --------- | ------ |
http://arxiv.org/abs/2101.00774,arXiv:2101.00774[cs]type:article

20 HaoYu,AoranGan,KaiZhang,ShiweiTong†,QiLiu,andZhaofengLiu
A StructureofRAGSystem
A.1 RetrievalComponent
The retrieval component of RAG systems in Figure 1 can be categorized into three
types: sparse retrieval, dense retrieval [77], and web search engine. The standard for
evaluationistheoutputofrelevantdocumentswithnumericalscoresorrankings.
Beforetheintroductionofneuralnetworks,sparseretrievalsarewidelyusedforre-
trievingrelativetextcontent.MethodslikeTF-IDF[46]andBM25[47]relyonkeyword
matching and word frequency but may miss semantically relevant documents without
keywordoverlap.
ByleveragingdeeplearningmodelssuchasBERT[9],denseretrievalcancapture
thesemanticmeaningoftexts,whichallowsthemtofindrelevantdocumentsevenwhen
keywordoverlapisminimal.Thisiscrucialforcomplexqueriesthatrequireacontex-
tualunderstandingtoretrieveaccurateinformation.Withadvancedfusionstructurefor
queriesanddocuments[28]andthemoreefficientimplementationofK-NearestNeigh-
bors (KNN) [51], Approximate Nearest Neighbor (ANN) [12,25] search techniques,
denseretrievalmethodshavebecomepracticalforlarge-scaleuse.
Web search engine employs the complex online search engine to provide relevant
documents, such as Google Search [18], Bing Search [40], DuckDuckGo [13]. RAG
systemscantraversetheweb’sextensiveinformation,potentiallyreturningamoredi-
verseandsemanticallyrelevantsetofdocumentsviatheAPIofthesearchprovider.The
blackboxofthesearchengineandtheexpenseoflarge-scalesearcharenotaffordable
sometimes.
Itisobservedthatdenseretrievaltechniques,particularlythoseleveragingembed-
dings, stand out as the preferred choice within the RAG ecosystem. These methods
are frequently employed in tandem with sparse retrieval strategies, creating a hybrid
approach that balances precision and breadth in information retrieval. Moreover, the
adoption of sophisticated web search engines for benchmark assessment underscores
theirgrowingsignificanceinenhancingtherobustnessandcomprehensivenessofeval-
uations.
Indexing Theindexingcomponentprocessesandindexesdocumentcollections,such
as HuggingFace datasets or Wikipedia pages. Chunking before indexing can improve
retrieval by limiting similarity scores to individual chunks, as semantic embedding is
less accurate for long articles, and desired content is often brief [32]. Index creation
is designed for fast and efficient search. For example, the inverted index for sparse
retrievalandtheANNindexfordenseretrieval.
Sparse Retrieval involves calculating IDF for each term and storing values in a
databaseforquicklook-upandscoringwhenqueried.
DenseRetrievalencodesdocumentsintodensevectorsusingapre-trainedlanguage
modellikeBERT.ThesevectorsarethenindexedusinganApproximateNearestNeigh-
bor (ANN) search technique, like graph-based Hierarchical Navigable Small World
(HNSW) or Inverted File Index (IVF) [12]. This process allows for the efficient re-
trievalof“closed”itemsbygivenpredefineddistancemetrics.

EvaluationofRetrieval-AugmentedGeneration:ASurvey 21
Search This step is responsible for retrieving relevant documents based on a given
query. Queries are submitted using the respective API to retrieve relevant documents
forwebsearchengineretrieval.Forlocalresources,thequerycomponentisresponsible
for formatting the query in the format required by different sparse or dense retrieval
methods. Then, the query is submitted to the retrieval system, which returns a set of
relevantdocumentsalongwiththeirscores.
In both local and web-based scenarios, an optional reranker can be employed to
refine the ranking of retrieved documents further. The reranker usually comprises a
more complex and larger model that considers additional features of the documents
and the given query. These additional features often include the semantic relationship
betweenthequeryandthedocumentcontent,documentimportanceorpopularity,and
othercustommeasuresspecifictotheinformationneedathand.
A.2 GenerationComponent
The evaluable output for the generation component is the response of LLMs and the
structuredorformattedoutputfromthephrasedresponse.
Prompting Thegenerationprocesscriticallyhingesonprompting,whereaquery,re-
trievaloutcomes,andinstructionsconvergeintoasingleinputforthelanguagemodel.
Research showcases various strategic prompting tactics such as the Chain of Thought
(CoT)[60],TreeofThought(ToT)[3],andSelf-Note[31],eachsignificantlyshaping
themodel’soutput.Thesemethods,especiallythestep-by-stepapproach,arepivotalin
augmentingLLMsforintricatetasks.
PromptinginnovationshaveintroducedmethodslikeRephraseandRespond(RaR)
[8],enhancingLLMsbyrefiningquerieswithinpromptsforbettercomprehensionand
response. This technique has proven to boost performance across diverse tasks. The
latestRAGbenchmarks[61,62]inthespecificdomainsstarttoevaluatetherobustness
ofvariouspromptingengineeringskills,includingCoT,RaR,etc.
Inference The final input string prepared in the prompting step is then passed on to
theLLMsasinput,whichgeneratestheoutput.TheinferencestageiswheretheLLM
operatesontheinputderivedfromtheretrievalandthepromptingstagesinthepipeline
togeneratethefinaloutput.Thisisusuallytheanswertotheinitialqueryandisused
fordownstreamtasks.
Dependingonthespecificsofthetaskorexpectedoutputstructure,apost-processing
step may be implemented here to format the generated output suitably or extract spe-
cific information from the response. For example, the classification problems (multi-
choicequestions)orifthetaskrequirestheextractionofspecificinformationfromthe
generated text, this step could involve additional named entity recognition or parsing
operations.