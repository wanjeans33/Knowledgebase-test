Front.Comput.Sci.,2025,0(0):1–18
https://doi.org/10.1007/sxxxxx-yyy-zzzz-1
| REVIEW |           | ARTICLE |           |     |            |     |                 |     |     |     |         |     |     |
| ------ | --------- | ------- | --------- | --- | ---------- | --- | --------------- | --- | --- | --- | ------- | --- | --- |
|        | Retrieval |         | Augmented |     | Generation |     | Evaluation      |     |     | in  | the Era | of  |     |
|        |           | Large   | Language  |     | Models:    |     | A Comprehensive |     |     |     | Survey  |     |     |
(cid:66)
|     | AoranGAN1,HaoYU2,KaiZHANG1,QiLIU( |     |     |     |     |     | )1,WenyuYAN1,ZhenyaHUANG1, |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
ShiweiTONG3,EnhongCHEN1,GuopingHU1,4
5202 rpA 12  ]LC.sc[  1v19841.4052:viXra
1 StateKeyLaboratoryofCognitiveIntelligence,UniversityofScienceandTechnologyofChina,Hefei,China
2 McGillUniversity,Montreal,Canada
3 TencentCompany,Shenzhen,China
|     |     |     | 4 ArtificialIntelligenceResearchInstitute,iFLYTEKCo.,Ltd,Hefei,China |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
©HigherEducationPress2025
Abstract RecentadvancementsinRetrieval-AugmentedGen- ThisapproachsignificantlyimprovesLargeLanguageMod-
eration(RAG)haverevolutionizednaturallanguageprocess- elsthroughnon-parametriclearning,multi-sourceknowledge
ingbyintegratingLargeLanguageModels(LLMs)withex- integration, and specialized domain adaptation [1,2]. By
ternalinformationretrieval,enablingaccurate,up-to-date,and connectingLLMswithexternaldatabases,RAGproducesre-
verifiable text generation across diverse applications. How- sponsesthatarebothcontextuallyappropriateandgrounded
ever,evaluatingRAGsystemspresentsuniquechallengesdue in authoritative, up-to-date information, marking a substan-
to their hybrid architecture that combines retrieval and gen- tial advancement in developing more sophisticated natural
erationcomponents,aswellastheirdependenceondynamic languageprocessing(NLP)systems[3,4].
knowledge sources in the LLM era. In response, this paper Asasophisticatedandexpansivesystemthatencompasses
| provides | a   | comprehensive | survey of | RAG evaluation |     | meth- |     |     |     |     |     |     |     |
| -------- | --- | ------------- | --------- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
numerouselementsfromboththeLLMandretrievaldomains,
odsandframeworks,systematicallyreviewingtraditionaland RAGcanbeapproximatelysegmentedintotwoprincipalsec-
emergingevaluationapproaches,forsystemperformance,fac- tions from a macroscopic viewpoint: retrieval and genera-
tualaccuracy,safety,andcomputationalefficiencyintheLLM
|     |     |     |     |     |     |     | tion. Theretrievalsectiontypicallyentailsdiverseoperations |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
era.WealsocompileandcategorizetheRAG-specificdatasets including preprocessing, dense or sparse retrieval, rerank-
| and | evaluation | frameworks, | conducting | a meta-analysis |     | of  |         |          |            |     |                |         |      |
| --- | ---------- | ----------- | ---------- | --------------- | --- | --- | ------- | -------- | ---------- | --- | -------------- | ------- | ---- |
|     |            |             |            |                 |     |     | ing and | pruning, | etc [5,6]. |     | The generation | section | com- |
evaluation practices in high-impact RAG research. To the prisescomponentssuchasretrievalplanning,theintegration
best of our knowledge, this work represents the most com- ofmulti-sourceknowledge,andlogicalreasoning[7,8]. Ad-
| prehensive |     | survey for | RAG evaluation, | bridging | traditional |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --------------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ditionally,RAGsystemsincorporateinterconnectedupstream
and LLM-driven methods, and serves as a critical resource and downstream elements such as document chunking, em-
foradvancingRAGdevelopment.
|     |     |     |     |     |     |     | bedding | generation, | and | mechanisms | for | ensuring | security |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ---------- | --- | -------- | -------- |
Keywords RetrievalAugmentedGeneration,SystemEval- andcredibility[9]. TheoverallperformanceofRAGsystems
|     |     |     |     |     |     |     | depends | not only | on each | individual | component | but | also on |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | ---------- | --------- | --- | ------- |
uation,LargeLanguageModel
theirinteractionsandintegratedfunctionality.
|     |     |     |     |     |     |     | When | faced with | such | complex | systems, | a fundamental |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ---- | ------- | -------- | ------------- | --- |
1 Introduction andpracticalquestionarisesregardingtheevaluationframe-
workforassessingtheefficacyofarchitecturalmethodologies
Retrieval Augmented Generation (RAG) has emerged as a governingboththeholisticsystemanditsconstituentcompo-
powerfulmethodologythatenhancesnaturallanguagegener- nents.ThischallengeprovesparticularlypronouncedinRAG
ationbyincorporatinginformationfromexternalknowledge.
|     |     |     |     |     |     |     | systems,     | where    | three factors | -                 | the expansive | scope    | of im- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------------- | ----------------- | ------------- | -------- | ------ |
|     |     |     |     |     |     |     | plementation | domains, |               | the heterogeneity | of            | internal | compo- |
Receivedmonthdd,yyyy;acceptedmonthdd,yyyy nents,andthedynamicprogressionofcurrentdevelopments
E-mail:qiliuql@ustc.edu.cn - collectively render the establishment of a unified system-

| 2   |     |     |     | Front.Comput.Sci.,2025,0(0):1–18 |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
aticevaluationparadigmanongoingresearchfrontier. Inre- or fine-tuning on specific datasets, these methods encounter
sponsetothis,weconductedthissurveyonRAGEvaluation challengesrelatedtoarithmetic,timeliness,flexibility,orus-
to gather methods for multi-scale assessment of RAG in re- ability (on close models). Optimization techniques during
centyears. Thecomprehensivenessofthissurveyisdemon- the LLM inference phase have thus garnered significant at-
stratedinfouraspects: 1)Systematiccompleteness, encom- tention. One of the representative techniques is Prompt En-
passing both the evaluation of RAG’s internal components gineering, in which artificially constructed task descriptions
and the system as a whole; 2) Methodological variety, in- and commands are used to enhance LLMs’ understanding
cludingbothtraditionalstatistically-basedevaluationmetrics of task objectives. In-context learning is designed to enable
and the innovative methods characteristic of the LLM era; LLMstoanalyzepatternsandgeneralizefromtasksamples,
offeringsubstantialadvantagesinfew-shotscenarios[17,18].
| 3)Sourcediversity, |     | incorporatingbothstructuredevaluation |     |     |     |     |     |     |     |
| ------------------ | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
frameworks,aswellascutting-edgemethodsscatteredacross Unlike these approaches, RAG aims to address the issue of
variouspapers; and4)Practicality,bothintermsofmetrics’ knowledgelimitationsinherentinLLMbyincorporatingex-
definition to be evaluated and their subsequent application. ternalknowledge. BothLLMandRAGpossesscomplemen-
Throughthismulti-dimensionalapproach,weaimtoprovide tarystrengths:RAGcaneffectivelyleveragethesuperiorrea-
researchersandpractitionerswithacomprehensivetoolkitfor soningcapabilitiesofLLMs,combinedwiththebroadknowl-
evaluatingandimprovingRAGsystems. edgescopeofexternaldata,toexplorethepotentialapplica-
Theremainderofthispaperisorganizedasfollows: Sec- tions of LLMs more extensively [19]. On the other hand,
tion2offersaconcisereviewoftheexistingLLM-basedRAG LLMscanserveascrucialcomponentsinRAG,functioning
systemtoprovidethereaderwithrelevantbackgroundknowl- asthedecisionmaker,reasoner,generator,orevenevaluating
edge. Ourcomprehensiveevaluationisdividedintotwodis- certainaspectsofRAG[20,21].
tinctsections:InternalEvaluation(Section3)andExternal
Evaluation (Section 4). Internal Evaluation assesses com- 2.2 RetrievalAugmentedGeneration(RAG)
| ponent level | performance |     | and methodology-specific |     | metrics |     |     |     |     |
| ------------ | ----------- | --- | ------------------------ | --- | ------- | --- | --- | --- | --- |
RAGisatechnicalframeworkthatenhancesNLPsystemsby
| within basic | RAG | systems, | focusing | on technical | advance- |     |     |     |     |
| ------------ | --- | -------- | -------- | ------------ | -------- | --- | --- | --- | --- |
integratingexternalknowledgeretrieval,whosecoreinnova-
ment. Externalevaluationexaminessystem-widefactorslike
tionenablesextranon-parametricoptimizationofparameter-
| safety and | efficiency, | emphasizing | practical | viability. | We  |              |                 |                 |                 |
| ---------- | ----------- | ----------- | --------- | ---------- | --- | ------------ | --------------- | --------------- | --------------- |
|            |             |             |           |            |     | fixed neural | language models | after training, | effectively ex- |
payparticularattentiontotheemergingtrendofLLM-based panding their operational domains while maintaining archi-
| evaluationmethods, |     | whichrepresentanovelassessmentap- |              |            |        |          |                       |                   |             |
| ------------------ | --- | --------------------------------- | ------------ | ---------- | ------ | -------- | --------------------- | ----------------- | ----------- |
|                    |     |                                   |              |            |        | tectural | stability [22]. Prior | to the widespread | adoption of |
| proach unique      | to  | the current                       | era. Section | 5 presents | exist- |          |                       |                   |             |
LLM,scholarlyinvestigationshadalreadyestablishedmeth-
ingRAGevaluationframeworks,datasets,andmethods,pro-
odsforenhancingNLPtasksthroughexternalknowledgein-
| vidingapracticalresourceforresearchers. |     |     |     | Furthermore,we |     |              |                    |        |                    |
| --------------------------------------- | --- | --- | --- | -------------- | --- | ------------ | ------------------ | ------ | ------------------ |
|                                         |     |     |     |                |     | fusion [23]. | Initial researches | on RAG | adhered to an ele- |
compiledacomprehensivecollectionofhigh-levelRAGstud-
|              |             |            |                |               |               | mentary                               | indexing and reading | paradigm | [24,25]. Later for- |
| ------------ | ----------- | ---------- | -------------- | ------------- | ------------- | ------------------------------------- | -------------------- | -------- | ------------------- |
| ies spanning | multiple    | dimensions | in             | recent years, | and con-      |                                       |                      |          |                     |
|              |             |            |                |               |               | mulationsdelineatedtwocorecomponents: |                      |          | (1)theretriever,    |
| ducted a     | preliminary | analysis   | and discussion |               | from the per- |                                       |                      |          |                     |
whichidentifies,indexes,filters,andstructuresrelevantknowl-
spectiveofevaluation(Section6).
edgefragmentsfromexternaldatasources;(2)thegenerator,
whichsynthesizesthecuratedsegmentsthroughanalysisand
|     |     |     |     |     |     | logicalreasoningtoproduceoutputs[9]. |     |     | Figure1showsthe |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --------------- |
2 Background
workflowofanRAGsystemwithrecommendationsofcom-
|     |     |     |     |     |     | ponentsimplementationusingLLMsatpresent. |     |     | Weprovide |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --------- |
2.1 LargeLanguageModel(LLM)
aconcisedescriptionofeachmodule’sprocessbelow.
Large Language Models, with billions of parameters, are a The retrieval component of RAG systems is inspired by
classofgenerativeneurallanguagemodelstrainedonexten- theretrievaltechnologiesinmultipledomains,suchasinfor-
sive natural language data [10,11]. Due to the wide cover- mationretrieval[26],open-domainquestionanswering[27],
ageofthetrainingcorpus,LLMsareconsideredtoimplicitly andrecommendersystems[28,29]. Beforetheretrieval,itis
integrate world knowledge [12]. LLMs are capable of ad- necessarytoconstructasuitablecorpusfortheretrievalcom-
hering to human instructions or requests though instruction ponentatthebeginning.Thesourcesofdataarediverse,such
tuning, thus being able to effectively understand and gener- as domain-specific datasets like Wikipedia, specialized cor-
ate human-like text [13]. Its generalization open up a wide pora (e.g., scientific articles, financial reports) [30], or real-
range of applications, such as NLP, signal processing, and timedatagatheredfromwebscrapingorsearchengines[31].
recommender systems [14,15]. However, LLM’s capabil- Thecorpusissubsequentlyfilteredandpreprocessedtocon-
offline
ityremainscircumscribedbytheirtrainingdata. Itissome- form to the retrieval-friendly structure via chunking
times predisposed to generating factually inconsistent out- and embedding. Chunking involves segmenting large doc-
puts(hallucinations), particularlywhenprocessingnovelin- uments into smaller, more manageable units guided by the
formationbeyondtrainingdata[16]. Despitetheadaptability original structure or context information [32–34]. Embed-
of LLMs to diverse downstream tasks through post-training ding(ortextvectorization)aimstorepresentthetextualcon-

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 3
in-context-ralm
Retrieval Augmented Generation System 🤖 Components Impl. </>
Retrieval Pipeline Generation Workflow
Stage 2.0. Indexing and Storing Stage 0. LLM Provider
API Provider Hugging Face
Source Transform Indexing VLLM SGLang
e n ilffO
H W F i k D ip at e a d s i e a t QA P E
C
a m
F
i
h i
r b
l u t
G e
e n
d e
r k i
n d
i n n
e i
g
n r
g
a g tion
H
N
B N M
eo
S 2
4
W 5
j
Sta
R
g
o
e
u
1
te
.
r
Intent Rec
L
o
o
g
c
N .
a l
o &
K
S
n
R e
o
a o
w
r u c
l
h
e
t
d
in
ge
g
Input
Human Interaction 🧑
KB a , n I d m e a t g c. es, G R r e a la p t h io C n o E n x s t t r ru ac c t t i i o o n n ES/Database Open Web Search User Msg AppleInc.revenue?🧑
… Custom
Stage 2. Retrieval Knowledge User Profile
Stage 2.1. Query Understanding Query 1 User Input Reference History 🤖I I n nc f . i s r c e a p l o y r e te a d r t 2 o 0 t 2 a 4 l , Apple
Query E D R n e a e r c n w i o c d m r h i e m t p t t c o e e . n s n e t Q Q Q u u u e e e .. r r r . y y y N 2 3 Sta S g e e a r 3 c . h R C e o s n p fi o g nse Ge D ne o r c a u t m io e n nts C K u M n s o e B t w s o a s m l s e a e i d g z g e e e d r b e il v li e o n n u .[ e 1] s [2 ][ o [ 3 1 ] f ] $ s 3 e 9 cs 1 e . n 0 s 3 e 5 .a i
Stage 2.2. Recall [2] elpais.com
Web Search Engine Documents Query T {system} [3] reuters.com
e n iln O Queries KN B N M /A 25 NN D D o o c c u u m m e e n n t t s s S R P y e r s l o t e e m v m a p n t P t S r D o k m o ill c s p s t et al p m e { { { u q d s u o e e c r r s } y } } Output Red Team
… Documents All Information
Stage 2.3. Fusion Response How to make bomb? 🧑
❄️Large Language Model References
Reranker
S
M
o
u
u
l
r
t
c
i-
e R
S
a
c
n
o
k
r
e
e
d
F
F
u
u
si
s
o
io
n
n D
R
o
e
c
f
u
e
m
re
e
n
n
ce
ts
🤖Rejected
Documents … Content Moderation
Fig.1 TheworkflowoftheRAGsystemandcomponentimplementationintheLLMera.
tentinahigh-dimensional,densesemanticspaceforefficient 2.3 RelatedSurveys
retrievalcomputation[5,35].
Lietal.[23]summerrizedandformalizedthekeydefinitions
Typically, RAG assessments convert the task into a con-
of RAG while providing a synthesis of early-stage method-
versational format of Question Answering (QA) comprising
ologies and practical applications. Expanding the scope be-
question and the ground-true answers with doc candidates
yond NLP, Zhao et al. [45] traced the developmental trajec-
[36,37]. IntheonlineRAGworkflow,someadditionalcom-
toryofmultimodalRAGacrossthebroaderAIGClandscape.
ponents are introduced before the retrieval, such like intent
The emergence of LLM has since triggered an accelerated
recognition, query rewriting and routing [38]. The retriever
developmentofRAGmethods,withnumeroussurveypapers
then indexes document collections from the data source. In
emergingtodocumentthisgrowingresearchdomain[1,9,19,
thiscorestep, multipleretrievalstrategiescanbeemployed,
20,46]. Currentresearchesmainlyfocusoncollectingmeth-
including sparse retrieval, dense retrieval, graph retrieval or
odsorapplications,butlacksubstantivediscussionaboutsys-
hybrid methods [6,39]. Certain systems conduct additional
tematic evaluation mechanisms. While Yu et al. [21] pro-
dynamicsearchesthroughsearchengines,typicallyfoundin
vided an initial review outlining conceptual approaches for
commercialized products. Some systems may introduce an
RAG evaluation, their analysis was predominantly confined
extra post-retrieval step to rerank the documents or fuse the
datascrossdifferentsources[7,40].Inthegenerationpipeline,
tomainstreamtheframeworks,offeringlimitedinsightsinto
emergingassessmentmethodsapplicabletodiversecontexts.
the responding progress based on the relevant documents is
Building upon previois foundational work, this comprehen-
assigned to the LLM, which serves primarily as a decision-
sivesurveyextendsbeyondtheselimitations,offeringdeeper
maker or reasoner [8]. Instead of generating knowledge in-
insightsintoemergingevaluationmethods.
dependently, the LLM synthesizes retrieved information to
form coherent responses, thereby reducing the risk of inter- This study extends the research [21] by incorporating a
nalhallucination.Additionally,arangeofmethodsofprompt broader array of RAG evaluation methods within a systems
engineeringareavailable,includingCoT[18],ToT[41],Self- theory context. We differentiate between internal and exter-
Note[42]andRaR[43],etc. Dependingonthespecifictask nal evaluations: the former examines the RAG component
andexpectedoutput,apost-processingstepmayberequired assessmentsandtheirinteractiveprocesseswithinthesystem
aftertheknowledge-orientedresponse,suchasEntityRecog- architecture,whilethelatterfocusesonholisticsystemeval-
nition for multi-choice questions or classification task, and uationandenvironmentalconsiderations,whereenvironment
the translation component for multilingual task. Moreover, specificallydenotestheexternaltasksorparticularevaluation
the utility of the model’s application is a point of concern, contexts. Weextendourhorizonsbeyondcollectingconcep-
particularlyregardingsafetyandefficiency[44]. tual definitions of evaluation methods to exploring and ana-

4 Front.Comput.Sci.,2025,0(0):1–18
lyzing their practical application in the actual RAG studies. Correctness (Relevant Documents ↔ Documents Candi-
Simultaneously,wefocusesonRAGevaluationinLLMcon- dates) assesses how accurate the retrieved documents are in
texts, prioritizing unstructured text retrieval as the prevail- comparisontoasetofcandidatedocuments.Itisameasureof
ing paradigm. Domain-specific variants of RAG evaluation thesystem’sabilitytoidentifyandscorerelevantdocuments
(e.g., knowledge graph, multimodal retrieval) are excluded higherthanlessrelevantorirrelevantones.
due to fundamental architectural gaps. Unless otherwise in- Thesimilarpairwiserelationsandtargetsforthegenera-
dicated,allthe‘RAG’hereafterpertaintothenarrowopera- tioncomponentareoutlinedbelow.
tionaltraining-freeframeworkemployingunstructureddocu- Relevance (Response ↔ Query) measures how well the
mentsasexternalknowledgeresources. generated response aligns with the intent and content of the
initial query. It ensures that the response is related to the
querytopicandmeetsthequery’sspecificrequirements.
3 InternalEvaluation Faithfulness (Response ↔ Relevant Documents) evalu-
ateshowthegeneratedresponseaccuratelyreflectstheinfor-
Inthissection,wesummarizeandorganizetheevaluationsof
mationcontainedintherelevantdocumentsandmeasuresthe
theinternalcomponentswiththeirinteractionswithinaRAG
consistencybetweenthegeneratedandsourcedocuments.
systemfrompriorstudies. Wedeconstructtheevaluationofa
Correctness (Response ↔ Sample Response) Similar to
wholeRAGsystem,focusingoninternalcomponentinterac-
theaccuracyintheretrievalcomponent,thismeasurestheac-
tions. Arangeofevaluationapproachesarethenintroduced,
curacyofthegeneratedresponseagainstasampleresponse,
from traditional to new ones. The elements mentioned and
which serves as a ground truth. It checks if the response is
the implication of internal evaluation point to a framework
correctintermsoffactualinformationandappropriateinthe
for evaluating the strengths of the RAG system’s core func-
contextofthequery.
tionality,thatis,generatingaccurateandcredibleoutput.
3.2 ConventionalEvaluationMethods
3.1 EvaluationTarget
RAGisacross-disciplinarysystemfoundedontraditionalre-
The diverse components of the RAG system can be boiled
search fields including information retrieval (IR) and natu-
downtosolvingtwocoreproblems:theretrievaloftheground
rallanguagegeneration(NLG).Adheringtotheconventional
truth, and the generation of the response that closely aligns
methodsofthem,numeroustraditionalmetricsareemployed
withthegoldanswer.Theycorrespondtotherespectiveeval-
toevaluatetheretrievalandgenerationofRAGasfollows.
uationobjectivesoftheretrievalandgenerationmodules.
Figure2summarizestheevaluationtargetsoftheretrieval
3.2.1 IR-relatedMetrics
andgenerationcomponent.Theretrievalcomponentincludes
two main stages, recall and ranking. The outputs, relevant TheIR-relatedmetricsrefertotheindicatorsassociatedwith
documents,forbotharesimilartoevaluate.Thenwecancon- conventionalretrievalsystems.Thesemetricsarecategorized
structseveralpairwiserelationshipsfortheretrievalcompo- intotwogroupsbasedontheircorrelationtoranking:
nentbydefiningthetargetasfollows: • Non-rank-basedMetrics
Relevance(RelevantDocuments↔Query)evaluateshow Thenon-rank-basedmetricstypicallyevaluatebinaryoutcomes,
well the retrieved documents match the information needed thatis,whetheranitemisrelevantornot,withouttakinginto
expressed in the query. It measures the precision and speci- accounttheitem’spositioninarankedlist.
ficityoftheretrievalprocess. Accuracy/Hit@K is the proportion of true results (both
Comprehensiveness(RelevantDocuments↔RelevantDoc- truepositivesandtruenegatives)amongthecasesexamined.
uments)evaluatesthediversityandcoverageoftheretrieved
TP+TN
documents. This metric assesses how well the system cap- Accuracy=
TotalNumber
turesawiderangeofrelevantinformation, ensuringthatthe
retrieved documents provide a comprehensive view of the whereTPisthenumberoftruepositives,TN isthenumber
topicaccordingtothequery. oftruenegativesintheresponse.
Fig.2 TheevaluationtargetoftheRetrievalandGenerationcomponentinRAG.

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 5
Recall@K is the portion of relevant instances that have 3.2.2 NLG-relatedMetrics
| been retrieved | over | the | total amount |     | of relevant | cases, | con- |     |     |     |     |     |     |     |
| -------------- | ---- | --- | ------------ | --- | ----------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
TheNLG-relatedmetricsfocusonthecontentofthetextout-
sideringonlythetopkresults.
put,dedicatedtotheevaluationonthecharorsemanticlevel.
|     |     |     | |RD∩Top |     | kd | |     |     | EM(ExactMatch)isasimple,stringentandwidely-used |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ---- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
Recall=
|RD| evaluationmetricthatassessestheaccuracyofmodel-generated
|                                |     |     |     |     |        |            |     | answerscomparedtothegroundtruth.                      |     |     |     | Itscoresas1ifagen- |     |     |
| ------------------------------ | --- | --- | --- | --- | ------ | ---------- | --- | ----------------------------------------------------- | --- | --- | --- | ------------------ | --- | --- |
| whereRDistherelevantdocuments, |     |     |     |     | andTop | isthetop-k |     |                                                       |     |     |     |                    |     |     |
|                                |     |     |     |     |        | kd         |     | eratedanswerpreciselyalignswiththestandardotherwise0. |     |     |     |                    |     |     |
retrieveddocuments.
Typically,theresponsesneedstandardizationandpreprocess-
| Precision@K |     | is the | fraction | of relevant | instances |     | among |            |            |     |            |         |     |              |
| ----------- | --- | ------ | -------- | ----------- | --------- | --- | ----- | ---------- | ---------- | --- | ---------- | ------- | --- | ------------ |
|             |     |        |          |             |           |     |       | ing (e.g., | conversion | to  | lowercase, | removal | of  | punctuation, |
theretrievedinstances,consideringonlythetopkresults.
|     |     |     |     |     |     |     |     | elimination            | of articles, |     | and standardization          |     | of  | number for- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | ------------ | --- | ---------------------------- | --- | --- | ----------- |
|     |     |     |     | TP  |     |     |     | mats)beforecomparison. |              |     | Ageneralapproachinvolvescom- |     |     |             |
Precision= biningEMandPrecision/Recall/F1oreditdistance[48,49].
TP+FP
ROUGE(Recall-OrientedUnderstudyforGistingEvalu-
| where TP | represents | true | positives |     | and FP | represents | false |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | --------- | --- | ------ | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
ation)[50]isasetofmetricsdesignedtoevaluatethequality
positives,respectively.
ofsummariesbycomparingthemtohuman-generatedrefer-
F1Scoremeasuresthebalancebetweenprecisionandre-
|     |     |     |     |     |     |     |     | ence summaries. |     | ROUGE | can | be indicative | of  | the content |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | --- | ------------- | --- | ----------- |
call,definedastheHarmonicMeanofthetwo.
|     |     |     |     |     |     |     |     | overlap between |     | the generated |     | text and | the reference | text. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | -------- | ------------- | ----- |
2×Precision×Recall The variants of ROUGEs measure the overlap of n-grams
F1=
Precison+Recall
(ROUGE-N,ROUGGE-W),wordsubsequences(ROUGE-L,
ROUGGE-S),andwordpairsbetweenthesystem-generated
• Rank-BasedMetrics
summaryandthereferencesummaries.
Therank-basedmetricsfocuseonthesequentialpresentation
BLEU(BilingualEvaluationUnderstudy)[51]isametric
| of relevant | items, | assigning | greater |     | significance | to  | the posi- |                |     |         |                       |     |     |              |
| ----------- | ------ | --------- | ------- | --- | ------------ | --- | --------- | -------------- | --- | ------- | --------------------- | --- | --- | ------------ |
|             |        |           |         |     |              |     |           | for evaluating | the | quality | of machine-translated |     |     | text against |
tioningoftheseitemswithintherankinglist.
|     |     |     |     |     |     |     |     | oneormorereferencetranslations. |     |     |     | BLEUcalculatesthepre- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --------------------- | --- | --- |
MRR(MeanReciprocalRank)istheaverageoftherecip-
|     |     |     |     |     |     |     |     | cision of n-grams |     | in the | generated | text compared |     | to the ref- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | --------- | ------------- | --- | ----------- |
rocalranksofthefirstcorrectanswerforasetofqueries.
|     |     |     |     |     |     |     |     | erence text | and then | applies | a   | brevity penalty |     | to discourage |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------- | --- | --------------- | --- | ------------- |
(cid:88)|Q| overlyshorttranslations.Beyondmachinetranslationevalua-
|     |     |      | 1   |     | 1   |     |     |                                                    |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | MRR= |     |     |     |     |     | tion,BLEUcanalsobeusedforsupervisedcomparisoneval- |     |     |     |     |     |     |
|Q|
|                                     |     |     |     | rank | i   |                |     |                               |         |         |            |             |         |          |
| ----------------------------------- | --- | --- | --- | ---- | --- | -------------- | --- | ----------------------------- | ------- | ------- | ---------- | ----------- | ------- | -------- |
|                                     |     |     |     | i=1  |     |                |     | uation for                    | general | natural | language   | generation. |         | BLEU has |
|                                     |     |     |     |      |     |                |     | limitations,                  | such    | as not  | accounting | for the     | fluency | or gram- |
| where|Q|isthenumberofqueriesandrank |     |     |     |      |     | istherankposi- |     |                               |         |         |            |             |         |          |
|                                     |     |     |     |      | i   |                |     | maticalityofthegeneratedtext. |         |         |            |             |         |          |
tionofthefirstrelevantdocumentforthei-thquery.
METEOR[52]isametricdesignedtoassessthequality
NDCG(NormalizedDiscountedCumulativeGain)accounts
|     |     |     |     |     |     |     |     | ofmachinetranslationortextgeneration. |     |     |     |     | ItenhancesBLEU |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | -------------- | --- |
forthepositionoftherelevantdocumentsbypenalizingrele-
vantdocumentsthatappearlowerinthesearchresults[47]. byincorporatingmechanismslikesynonymization,stemming
matching,andwordorderpenalties,demonstratingastronger
DCG@k correlation with results obtained from manual evaluations.
NDCG@k=
|     |     |     |     | IDCG@k |     |     |     | METEORisdefinedas: |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
whereDCG@kistheDiscountedCumulativeGainatrankk (α2+1)Precision×Recall
|     |     |     |     |     |     |     |     | METEOR=(1−p) |     |     |     |     |     | ,   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
and IDCG@k is the Ideal Discounted Cumulative Gain at Recall+αPrecision
| rank k, which | represents |     | the | maximum | possible |     | DCG@k. |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | --- | ------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
whereαisthebalancedfactor,andpisthepenalizationfactor
DCG@kisdefinedas:
forwordorder.
(cid:88)k
|     |     |     |     | 2reli | −1  |     |     | BertScore[53]leveragesthecontextualembeddingfrom |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
DCG@k=
|     |     |     |     |     | (i+1) |     |     | pre-trainedtransformerslikeBERTtoevaluatethesemantic |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
log
|     |     |     | i=1 | 2   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
similaritybetweengeneratedtextandreferencetext.BertScore
withrel beingthegradedrelevanceoftheresultatpositioni. computestoken-levelsimilarityusingcontextualembedding
i
MAP(MeanAveragePrecision)isthemeanoftheaverage andproducesprecision,recall,andF1scores.Unliken-gram-
precisionscoresforeachquery. based metrics, BertScore captures the meaning of words in
context,makingitmorerobusttoparaphrasingandmoresen-
(cid:80)n
1 (cid:88)|Q| (P(k)×rel(k)) sitive to semantic equivalence. It has multiple variants, in-
|     | MAP= |     |     | k=1 |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|Q| |relevantdocuments | cluding backbone advanced pre-trained models (e.g. BERT,
|     |     |     | q=1 |     |     | q   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RoBERTaandBART)andsupervisedevaluationbasedonex-
P(k)istheprecisionatcutoffk
| where |     |     |     |     | inthelist,rel(k)isan |     |     | ternalclassifierdesign. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | -------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
indicatorfunctionequaling1iftheitematrankkisarelevant Textual Similarity measures the semantic variety in re-
documentinthenretrieveddocuments,0otherwise. trieved documents. It can be calculated using metrics like

| 6   |     |     |     |     | Front.Comput.Sci.,2025,0(0):1–18 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Intra-DocumentSimilarityorInter-DocumentSimilarity,which Theevaluation ofchunkingmethodscan beconductedat
assessthesimilaritybetweendocumentswithinaset. two levels. First, chunk-specific evaluation focuses on in-
trinsicmetricssuchasAccuracy,measuredbyFullKeyword
|     |     |     | 1 (cid:88)|D| | (cid:88)|D| |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Similarity= Coverage—thepercentageofrequiredkeywordspresentinat
|     |     |     |     | sim(d,d | )   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|D|2 i j least one retrieved chunk—and the Tokens To Answer met-
|     |     |     | i=1 | j=1 |     |     |            |        |           |        |             |               |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --------- | ------ | ----------- | ------------- | --- |
|     |     |     |     |     |     |     | ric, which | tracks | the index | of the | first fully | comprehensive |     |
where Disthesetofretrieveddocuments,d andd areem- chunk and cumulative token count needed for full context
|     |     |     |     |     | i   | j   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
beddings of individual documents, and sim(d,d ) is a simi- coverage[57].Second,extrinsicevaluationanalyzeshowdif-
|     |     |     |     |     | i j |     |                 |     |            |           |           |             |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --------- | --------- | ----------- | --- |
|     |     |     |     |     |     |     | ferent chunking |     | approaches | influence | retrieval | performance |     |
laritymeasure(e.g.,themostcommonlyusedcosinesimilar-
ity)betweenthetwodocuments. on downstream tasks. For example, [34] and [58] evaluate
|     |     |     |     |     |     |     | chunking | methods | by comparing |     | retrieval | recall, | precision, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------------ | --- | --------- | ------- | ---------- |
Coveragemeasurestheproportionofrelevantdocuments
retrievedfromthetotalnumberofrelevantdocumentsavail- andresponsequalityusingmetricslikeROUGE,BLEU,and
able in the dataset. It quantifies how comprehensively the F1 scores against ground truth evidence paragraphs, while
consideringcomputationaloverhead.Otherworksextendthis
| system captures |     | all pertinent | information |     | across | the corpus, |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | ----------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
acrosstopics,categories,orentitiesdefinedbyhumansorin evaluation using domain-specific datasets, such as financial
|     |     |     |     |     |     |     | reports [57], | to  | observe | how structure-based |     | and | semantic |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | ------------------- | --- | --- | -------- |
theknowledgebase.
chunkingimprovesretrievalaccuracywhilereducinglatency
|RD∩Retrieved|
|           | Coverage=     |                  |           |            |           |          | andtokenusageduringinference.                     |      |      |                       |      |           |         |
| --------- | ------------- | ---------------- | --------- | ---------- | --------- | -------- | ------------------------------------------------- | ---- | ---- | --------------------- | ---- | --------- | ------- |
|           |               |                  |           | |RD|       |           |          | Beforeretrieval,theembeddingmodeldeterminestheac- |      |      |                       |      |           |         |
|           |               |                  |           |            |           |          | tualperformanceofretrievingrelevantdocuments.     |      |      |                       |      |           | Compre- |
| where RD  | is the        | set of relevant  |           | documents  | and the   | notation |                                                   |      |      |                       |      |           |         |
|           |               |                  |           |            |           |          | hensive benchmarks                                |      | like | Massive               | Text | Embedding | Bench-  |
| Retrieved | is the        | set of retrieved |           | documents. | The       | coverage |                                                   |      |      |                       |      |           |         |
|           |               |                  |           |            |           |          | mark (MTEB)                                       | [59] | and  | Massive Multicultural |      | Text      | Embed-  |
| can also  | be calculated | at               | the group | level,     | where the | relevant |                                                   |      |      |                       |      |           |         |
documentsaregroupedintodifferentcategoriesortopics. ding Benchmark (MMTEB) [60] have become standard for
|     |     |     |     |     |     |     | the evaluation | of  | embedding | models. | MTEB | introduced | the |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ------- | ---- | ---------- | --- |
|RelevantGroups∩RetrievedGroups| firstlarge-scalebenchmarkcovering8embeddingtasksacross
Coverage=
|RelevantGroups| 58 datasets and 112 languages, establishing that no single
|            |       |        |            |     |         |            | embedding  | method   | excels | across       | all tasks. | MMTEB            | sig- |
| ---------- | ----- | ------ | ---------- | --- | ------- | ---------- | ---------- | -------- | ------ | ------------ | ---------- | ---------------- | ---- |
| Perplexity | (PPL) | gauges | a language |     | model’s | predictive |            |          |        |              |            |                  |      |
|            |       |        |            |     |         |            | nificantly | expanded | this   | work through | a          | community-driven |      |
prowess, illustrating its level of uncertainty concerning test effort, encompassing over 500 evaluation tasks across 250+
data.Essentially,itisanexponentialvariationofcross-entropy,
|             |             |     |            |             |              |     | languages | and introducing |     | novel | challenges | like | instruction |
| ----------- | ----------- | --- | ---------- | ----------- | ------------ | --- | --------- | --------------- | --- | ----- | ---------- | ---- | ----------- |
| quantifying | the model’s |     | fit to the | probability | distribution | of  |           |                 |     |       |            |      |             |
following,long-documentretrieval,andcoderetrieval.
thetext. ItisdefinedbaseonthegenerativeLMoutputas Although the models of chunking and embedding have
|     |     |    |     |     |     |    | broadapplications,theyprimarilyserveasanupstreamcom- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
(cid:88)N
Perplexity=exp  1  p o ne n t o f th e r et r i e v e ri n R A G . T h e pr i m a ry b e n e fi t t o t h e e n -
|     |     | −   | logp(w | |w ,w | ,...,w | ) . |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | N   |        | i 1   | 2      | i−1 |     |     |     |     |     |     |     |
i=1 ti re s y st e m , in v o l v i n g c h un k in g a n d e m b e dd i n g , i s r e fl e c te d
intheenhancementoftheretriever’sevaluationmetrics.
It’simportanttonotethattheIR-relatedandNLG-related
methodsarenotdirectlyequivalenttoretrievalandgeneration
|                    |     |               |     |                     |     |     | 3.3 EvaluationMethodsviaLLMs |     |     |     |     |     |     |
| ------------------ | --- | ------------- | --- | ------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
| assessmentmethods. |     | InRAGsystems, |     | retrievalandgenera- |     |     |                              |     |     |     |     |     |     |
tionoperationstypicallyalternate.Forinstance,thequeryun- The advancement of LLM has catalyzed refined investiga-
derstandinganddocumentfusioncomponentareconsidered tions into RAG system architectures. Contemporary studies
as pre- and post-retrieval operations in the retriever, respec- increasinglyemployLLM-drivenassessmentmetrics,which
tively,yettheevaluationissometimesbasedontheNLG-like establishquantifiablebenchmarksforiterativeimprovements
methods. SCARF[54]usedBLEU/ROUGEtoevaluatethe acrossdifferentRAGmodules. Theycanbebroadlycatego-
query relevance of the retriever. Blagojevic et al. [40] uti- rizedintotheoutputandrepresentationbasedmethods.
| lizedcosinesimilaritytoassesstheretrievaldiversity. |     |     |     |     |     | Addi- |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
tionally,themetricscanbeadaptedintovariousdesignswith 3.3.1 LLMOutputbasedMethods
newlabelbasedonthespecificsubjectofstudy,suchasEd-
itDist[55],Fresheval[56],etc. The LLM-output based evaluation methods perform content
|     |     |     |     |     |     |     | identification | or  | statistical | analysis | of the | text-format | output |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | -------- | ------ | ----------- | ------ |
oftheRAGcomponentsassumedbytheLLM.Thesemeth-
3.2.3 UpstreamEvaluation
odsfeatureaconciseandeasilyunderstandableprocesswith-
Given the rapid advancement of RAG systems, it is crucial outrestrictionsregardingwhethertheLLMisopenorclosed.
toemphasizethesignificanceofofflinepreprocessingofthe
ThemoststraightforwardapproachistoinstructtheLLM
corpus. Wesupplementtheevaluationmethodofpreprocess- toexplicitlyevaluateorscorethetextualoutputofthecompo-
ingmodules,includingchunkingandembedding. nentbypromptengineering. MethodslikeRAGAS[61]and

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 7
DatabricksEval[62]promptGPT-basedjudgeswithexplicit whichrepresentstheproportionofquestionsansweredincor-
instructions, such as “Check if the response is supported by rectlybyretrieverr j thatwerecorrectlyansweredbyretriever
theretrievedcontext.” or“Assesscompletenesswithrespect r. MRWRandMRLRarecalculatedbyrespectivelyaverag-
i
| to the | user query.” |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhang et al. [63] utilized GPT-4 with a ingRWRacrossrowsandcolumnsamongtheretrievers:
| few-shot | prompt | design | to determine |     | whether | the generated |     |     |     |     |     |          |     |     |
| -------- | ------ | ------ | ------------ | --- | ------- | ------------- | --- | --- | --- | --- | --- | -------- | --- | --- |
|          |        |        |              |     |         |               |     |     |     |     | 1   | (cid:88) |     |     |
answer matches the gold ones comprehensively. Finsås et MRWR(i)=
|     |     |     |     |     |     |     |     |     |     |     |     | RWR(i, | j), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
M−1
| al.[64]implementedamulti-agentLLMframeworktoeval- |     |     |     |     |     |     |     |     |     |     |     | j(cid:44)i |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
uatetheretrievalperformanceandreportedahigherrelevance
(cid:88)
| withthehumanpreferencethanthetraditionalmethods.Patil |     |     |     |     |     |     |     |     |          |     | 1   |           |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --------- | --- | --- |
|                                                       |     |     |     |     |     |     |     |     | MRLR(i)= |     |     | RWR(j,i). |     |     |
M−1
et al. [65] proposed an Abstract Syntax Tree (AST) based j(cid:44)i
methodtomeasurethehallucinationinRAG,whichindicates
|     |     |     |     |     |     |     |     | Especially,MRLR(i)=0impliesthatretrieverr |     |     |     |     | consistently |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ------------ | --- |
i
| the accuracy |     | of calling | external | APIs | in the | RAG | system. |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | -------- | ---- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
outperformsalloftheotherones.
ThesemethodstypicallybenefitfromCoTreasoning.
Minetal.[69]proposedFactScoretomessurewhetherthe
| In                | addition, | numerous            | researchers |         | have     | proposed      | novel |                                        |         |         |           |                 |        |     |
| ----------------- | --------- | ------------------- | ----------- | ------- | -------- | ------------- | ----- | -------------------------------------- | ------- | ------- | --------- | --------------- | ------ | --- |
|                   |           |                     |             |         |          |               |       | generated                              | content | matches | the given | knowledge       | source | by  |
| definitions       | of        | statistical         | metrics     | derived | from     | the LLM       | out-  |                                        |         |         |           |                 |        |     |
|                   |           |                     |             |         |          |               |       | breakingthegenerationsintoatomicfacts. |         |         |           | Chiangetal.[70] |        |     |
| put, facilitating |           | a multi-perspective |             |         | approach | to evaluating |       |                                        |         |         |           |                 |        |     |
furtherconsidederthesynonymexpressionandproposedthe
theRAGcomponents.
|     |     |     |     |     |     |     |     | advanced | D-FAatScore. | FactScore |     | is a simple | statistical | de- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --------- | --- | ----------- | ----------- | --- |
Daietal.[66]proposedanewmetricSemanticPerplexity
terminationwhetherthefactualcontentainthegeneratedtext
| (SePer) | to capture | the | LLM’s | internal | belief | about | the cor- |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ----- | -------- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
ymatchestheexternalknowledgebaseC:
| rectnessofthegeneratedanswer. |     |     |     | Giventhequeryqandthe |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
referenceanswersa∗,SePerisdefinedastheoutputsequence 1 (cid:88)
|                                        |     |     |     |     |     |     |     |     | FS(y)= |      | I                 |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ----------------- | --- | --- | --- |
|                                        |     |     |     |     |     |     |     |     |        |      | [aissupportedbyC] |     | .   |     |
| likelihoodwithclusteredentitytargetas: |     |     |     |     |     |     |     |     |        | |A | |                   |     |     |     |
y a∈A
|       |         |     |        | (cid:88) |          |      |        |     |     |     | y   |     |     |     |
| ----- | ------- | --- | ------ | -------- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
|       | (q,a∗)= |     | (a∗    |          | k(C,a∗)p |      |        |     |     |     |     |     |     |     |
| SePer | M       | P   | M |q)≈ |          | i        | M (C | i |q), |     |     |     |     |     |     |     |
D-FActScorelinkssynonymousentitiesintothesamecluster
Ci ∈C
|     |     |     |     |     |     |     |     | A andconsideracluster-levelevaluation: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
yi
where MisthespecificLLM.Cistheclustersetthatthean-
|     |     |     |     |     |     |     |     |     |     | 1 (cid:88) | (cid:88) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --- | --- |
o th er c l u s t e r in g m o d e l g r o u p e s th e r e s p on s e s i n t o . p ( C | DFS(y)= I
|     |     |     |     |     |     |     | M i |     |     |     |     | [aissupportedbyC | ∗] . |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --- |
q ) m e a n s t h e p r o b a b i l it y th a t a r e s p o n s e g e n er a t e d b y M is |A | i
|           |           |                 |         |             |             |           |               |     |     | y A | ∈A ya ∈A |     |     |     |
| --------- | --------- | --------------- | ------- | ----------- | ----------- | --------- | ------------- | --- | --- | --- | -------- | --- | --- | --- |
|           |           |                 |         | ∗           |             |           |               |     |     | yi  |          | yi  |     |     |
| m a p p e | d t o t h | e c l u s t e r | C i . k | ( C i , a ) | i s a s i m | p l e k e | r n a l f u c | -   |     |     |          |     |     |     |
tiontomeasurethedistancebetweenthemeaningofsemantic To evaluate the risk in the generator’s response, Chen et
clusterC and a∗ by utilizing char-level matching or simply al. [71] introduced the divided cases of the generated an-
i
askingtheLLMtogetaTrue/Falseresponse.
swer,answerable(A)andunanswerble(U),alongwiththedif-
Qi et al. [67] introduced the key point extraction to the ferent prediction process in the RAG system, keep(K) and
RAGevaluationanddesignedKPRmetrictoevaluatetheex- discard(D). Fourrisk-aware evaluationmetrics fromvarious
tenttowhichLLMsincorporatekeypointsextractedfromthe aspectsaredefinedas:
retrieveddocumentsintotheirgeneratedresponses: 1)Riskthatmeasurestheproprotionofriskycasessamong
|     |         |     |            | (cid:80)     |      |     |     | thekeptsamples: |     |     |      |     |     |     |
| --- | ------- | --- | ---------- | ------------ | ---- | --- | --- | --------------- | --- | --- | ---- | --- | --- | --- |
|     |         |     | 1 (cid:88) | I(x,M(q∥dq)) |      |     |     |                 |     |     |      |     |     |     |
|     | KPR(·)= |     |            | x∈xq         |      | ,   |     |                 |     |     |      |     |     |     |
|     |         | |Q| |            |              | |xq| |     |     |                 |     |     | |UK| |     |     |     |
Risk=
q∈Q
|AK|+|UK|
| where | Q is the | global | query | set, and | I(x,M(q∥dq)) |     | is a fuc- |     |     |     |     |     |     |     |
| ----- | -------- | ------ | ----- | -------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tiontojudgewhetherasingleLLMoutputsequenceM(q∥dq) 2)Carefulnessindicatesthepercentageofincorrectanddis-
cardedsamplesthatareequivalenttorecallfortheunanswer-
basedonthequeryqandtherecalleddocumentsdqentailsthe
| predefinedkeypointsxq. |     |     |     |     |     |     |     | ablesamples: |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Toevaluatetheinconsistencyofthedifferentretrieversin
|UD|
Carefulness=
| RAG, | Li et al. | [68] proposed |     | a pair | of naive | metrics | called |     |     |     |     |     |     |     |
| ---- | --------- | ------------- | --- | ------ | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|UK|+|UD|
| Mean                 | Relative | Win/Lose | Ratio | (MRWR/MRLR). |     |     | Given M |     |     |     |     |     |     |     |
| -------------------- | -------- | -------- | ----- | ------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| differentretrieversR |          | =        |       |              |     |     |         |     |     |     |     |     |     |     |
{r ,r ,...,r }andthedatasetwith N 3)Alignmentreferstotheproportionofsamplesinwhichthe
|     |     |     | 1 2 | M   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
query&answerpairs,thecorrectnessofmodelresponsefor system’sjudgmentalignwiththeassignedlabels:
>isfirstcauculated,denotedbyIm(n)=
| eachsample<q |     | n ,a n |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|AK|+|UD|
1iftheretrieverr answerscorrectlyonsamples otherwise Alignment=
|         |     | m        |           |       |     | n         |        |     |     | |AK|+|AD|+|UK|+|UD| |     |     |     |     |
| ------- | --- | -------- | --------- | ----- | --- | --------- | ------ | --- | --- | ------------------- | --- | --- | --- | --- |
| 0. Then | the | Relative | Win Ratio | (RWR) | of  | retriever | r over |     |     |                     |     |     |     |     |
i
| anotherretrieverr |     | j isdefinedas: |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4)Coveragequantifiestheproportionofsamplesretained:
|     |        |     | (cid:80) N | i(      | j(n))  |     |     |     |           |     |     |               |     |     |
| --- | ------ | --- | ---------- | ------- | ------ | --- | --- | --- | --------- | --- | --- | ------------- | --- | --- |
|     |        |     | =1         | I n ) ∗ | (1 − I |     |     |     |           |     | | A | K | + | U K | |     |     |
|     | RWR(i, | j)= | n          |         |        | ,   |     |     | Coverage= |     |     |               |     |     |
(cid:80) N
|     |     |     |     | 1 − | Ij (n ) |     |     |     |     | |AK|+ | | A | D| + | U K | +|UD| |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ----- | --- | ------------------ | --- | --- |
n = 1

| 8   |     |     |     |     |     | Front.Comput.Sci.,2025,0(0):1–18 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
3.3.2 LLMRepresentationbasedMethods of the total dataset, separately. A long-tail instance usually
|     |     |     |     |     |     |     |     | has a smaller | α   | and ▽ ins , | obtaining | a larger | GECE, | which |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --------- | -------- | ----- | ----- |
Therepresentation-basedmethods,conversely,capturesvalu-
implieslargerdegreeoflong-tailness.
| able | metrics | by modeling | vector | representation |     | in  | the inter- |           |     |           |       |          |           |         |
| ---- | ------- | ----------- | ------ | -------------- | --- | --- | ---------- | --------- | --- | --------- | ----- | -------- | --------- | ------- |
|      |         |             |        |                |     |     |            | To assess | the | extent to | which | external | knowledge | is uti- |
mediateorfinallayersoftheLLM.Thesemethodscanmit-
lizedintheRAGresponse,Sunetal.[77]proposedExternal
| igate | overreliance |     | on surface | lexical | patterns, | but | they may |     |     |     |     |     |     |     |
| ----- | ------------ | --- | ---------- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ContextScoreE,whichisdefinedontheresponselevelas:
| lose | interpretability |     | since the | final | numeric | similarity | does |     |     |     |     |     |     |     |
| ---- | ---------------- | --- | --------- | ----- | ------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
notnecessarilyclarifywhichfactualdetailiscorrectornot. 1 (cid:88) 1 (cid:88) e·xL
|     |                                                    |     |     |     |     |     |     |     | El,h | = El,h | =   |         | t   |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --- | ------- | --- | --- |
|     | Certainmethodsareinspiredbytheconventionalmetrics, |     |     |     |     |     |     |     | r    |        | t   |         | ,   |     |
|     |                                                    |     |     |     |     |     |     |     |      | |r|    | |r| | ∥e∥∥xL∥ |     |     |
|     |                                                    |     |     |     |     |     |     |     |      | t∈r    |     | t∈r     | t   |     |
demonstratedasexpansionsofexistingmetricsontheLLM.
For instance, GPTScore [72] is a GPT based LLM-scoring where |r| means the length of the response r, xL is the t-th
t
method inspired by BertScore, which has been widely used token’s vector logit of the last layer L. e is a pooled vector
asaconvincingmetric.ARES[73]combinedaclassifierwith ofthemostrelevantvectorsof xL accordingtotheattention
t
LLMembeddingstocheckwhetheragenerativeanswerisse-
weightsinthemiddlelayer:
| manticallyalignedwithground-truthevidence.         |     |     |     |     |     | RAGAS[61] |     |     |     |     |            |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|                                                    |     |     |     |     |     |           |     |     |     |     | 1 (cid:88) |     |     |     |
| usesacosinesimilarityapproachonLLM-generatedembed- |     |     |     |     |     |           |     |     |     | e=  |            | xL, |     |     |
j
| dingstogaugeanswerrelevance. |     |     |     |     |     |     |     |     |     | |Il | ,h| |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t j∈Il,h
t
Moreover,numerousresearchershavedevelopednovelrep-
resentation based metrics, which serve not only to evaluate where Il,h means the attended times where the token has
t
largerthantop-k%attentionscoreswithxL
thecomponentsbutalsotoguidethefurtherenhancement. inthel-thlayer.
t
Zhao et al. [74] introduced a novel metric, Thrust, which Noted that some of these LLM based evaluation metrics
assessestheLLM’sknowledgeabilitybyleveragingtherepre- representresearchspecializations. Whiletheymaynotbedi-
sentationdistributionoftheinstancesproducedbytheLLM. rectly targeted towards an actual RAG system, their presen-
AhypothesiswasproposedthatifanLLMhasacquiredad- tationisanintegralpartofadvancingresearchesinthefield
effectively
equate knowledge pertaining to a task, it should ofRAG,indicatingsignificantcontributionsaswell.
clustersamplesrelatedtothattaskthroughitshiddenstates.
TheThrustmetricwasdefinedas:
|     |     |     |                    |           |          |           |          | 4 ExternalEvaluation |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --------- | -------- | --------- | -------- | -------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | (cid:13)           |           |          |           | (cid:13) |                      |     |     |     |     |     |     |
|     |     |     | (cid:13) (cid:88)N | (cid:88)K |          |           | (cid:13) |                      |     |     |     |     |     |     |
|     |     |     | (cid:13) 1         |           | |C k l | | d k l (q) | (cid:13) |                      |     |     |     |     |     |     |
s (q)=(cid:13) (cid:13) · (cid:13) (cid:13) , W e h a v e d i s s e ct e d th e c o m p on e n t s o f R A G a n d pr o v i de d a
|     | thrust |     | (cid:13) N·K | ∥d  | ( q )∥2 | ∥d (q)∥ | (cid:13) |     |     |     |     |     |     |     |
| --- | ------ | --- | ------------ | --- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
(cid:13) kl k l (cid:13) co m p re h e n s i v e a c co u nt o f i ts in t e r na l e v al ua ti o n. T h i s s ec -
|     |     |     | l=1 | k=1 |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionshiftsourfocustotheexternalutilitythatRAG,asacom-
| where                          | N is | the number | of classes |     | for the specific       |     | task, K is |               |             |     |              |     |              |         |
| ------------------------------ | ---- | ---------- | ---------- | --- | ---------------------- | --- | ---------- | ------------- | ----------- | --- | ------------ | --- | ------------ | ------- |
|                                |      |            |            |     |                        |     |            | plete system, | encounters. |     | We summarize |     | the external | utility |
| thenumberofclustersperclass,|C |      |            |            |     | |denotesthecardinality |     |            |               |             |     |              |     |              |         |
kl in two areas: safety and efficiency, the evaluation of whom
| oftheset. | d   | (q)isavectorpointingfromtherepresentacion |     |     |     |     |     |                     |     |     |     |     |     |     |
| --------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
|           |     | kl                                        |     |     |     |     |     | areintroducedbelow. |     |     |     |     |     |     |
ofthequerytothecentroid.
Zhuetal.[75]introducedtheinformationbottleneckthe-
|     |     |     |     |     |     |     |     | 4.1 SafetyEvaluation |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
oryintoretrievalcomponenttomessuretherelevanceofthe
recalleddocumentandcandidatedocument.Moreover,anew Safety pertains to the RAG system’s capacity to ensure the
information bottleneck-based loss function was derived and generationofstableandharmlesscontentwithinadynamic,
used to train a better noise filter for the retriever. Given the evennoisyorhazardousenvironment. AsRAGsystemscon-
| sample{q,x,y}fromthedatasetandthenoisefilter |     |     |     |     |     |     | p(x˜|x,q) |                  |     |             |        |          |      |          |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --- | ----------- | ------ | -------- | ---- | -------- |
|                                              |     |     |     |     |     |     |           | tinue widespread |     | deployment, | safety | concerns | have | intensi- |
(needtuning),theinformationbottleneckintheRAGtaskis fiedbeyondthoseofstandaloneLLMs. Theincorporationof
derivedandformulatedas: externalknowledgesourcesintroducesuniquevulnerabilities
requiringspecializedevaluationframeworks[20].
|     | IB(x˜)= |     | (x|[q,x˜,y])−αP |     |     | (y|[q,x˜]), |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
P LLM LLM Robustness evaluations focus on system behavior when
|       |           |     |               |     |            |     |       | processing                                         | misleading | information |     | in retrieval | results. | The |
| ----- | --------- | --- | ------------- | --- | ---------- | --- | ----- | -------------------------------------------------- | ---------- | ----------- | --- | ------------ | -------- | --- |
| where | [·] means | the | concatenation |     | operation. | P   | means |                                                    |            |             |     |              |          |     |
|       |           |     |               |     |            |     | LLM   | RECALLbenchmark[78]testsdiscriminationbetweenreli- |            |             |     |              |          |     |
thefinaloutputprobabilityoftheLLM.
ableandcounterfactualknowledgeusingBLEU,ROUGE-L,
Lietal.[76]proposedanewmetricGECEbasedonME-
|     |     |     |     |     |     |     |     | andspecializedmetricslikeMisleadingRate. |     |     |     |     | Wuetal.[79] |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ----------- | --- |
TEORforassessingtheextentofthelong-tailnessofthegen-
|     |     |     |     |     |     |     |     | quantify | susceptibility | to semantically |     | related | but | irrelevant |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --------------- | --- | ------- | --- | ---------- |
eratedtextinRAG:
|     |     |     |     |     |     |     |     | information | using | Misrepresentation |     | Ratio | and Uncertainty |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----------------- | --- | ----- | --------------- | --- |
(cid:80)n
|METEOR(pred,ref)− 1 P (t)| Ratio.SafeRAG[80]categorizeschallengeslike”inter-context
|     |      | =   |        |     | n   | i=1 LLM | i   |                                                       |     |     |     |     |     |     |
| --- | ---- | --- | ------ | --- | --- | ------- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | GECE |     |        |     |     |         | ,   | conflict”withspecificevaluationmetrics,whileC-RAG[81] |     |     |     |     |     |     |
|     |      |     | α·[E(▽ |     | )·▽ | ]       |     |                                                       |     |     |     |     |     |     |
ins ins
providestheoreticalguaranteesongenerationrisksusingcon-
where α is theaverage wordfrequency, ▽ and E(▽ ) are formalriskanalysisandROUGE-L.Chengetal.[82]intro-
|     |     |     |     |     | ins |     | ins |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thegradientw.r.t. thecurrentinstanceandthemeangradient ducetwometricstoevaluatetheRAGsystem: 1)Resilience

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 9
Rate, aiming to emphases the system’s stability and robust- Transparency/Accountabilityassessestheunderstand-
ness, quantifies the percentage of instances where the sys- ability and traceability of the RAG system’s reasoning pro-
tem’s responses remain accurate, both prior to and follow- cess, enabling verification of sources and justification [95,
2)BoostRatequantifiesthepro-
ingretrievalaugmentation. 96]. Metrics are often qualitative or user-focused, such as
portionofinstancesinitiallyanswerederroneouslythatwere Explanation Quality, based on human ratings of the clarity,
subsequently corrected upon the introduction of a retrieved completeness, andusefulnessofexplanationsorprovenance
document,evaluatingtheeffectivenessofRAG.
|     |     |     |     |     |     |     |     | information | [96]; | Traceability, |     | the ease | of linking | the final |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------------- | --- | -------- | ---------- | --------- |
Factualityfocusesongeneratingaccurateinformationand output back to specific source documents or passages; and
CitationAccuracy(precision/recall)[20].
| avoiding | plausible | but | incorrect | statements |     | (hallucinations), |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | --------- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
especially with noisy or conflicting retrieval results [78,83, Comprehensivesafetybenchmarksstandardizeevaluation
84]. Key metrics include Factual Accuracy, using standard across multiple dimensions. SafeRAG [80] classifies attack
QAmetrics(EM,F1,accuracy,etc.) whenthecontextmight tasksintofourcategorieswithtailoreddatasets.VERAframe-
bemisleading[78];theHallucinationRate,thefrequencyof work[97]usesbootstrapsamplingforconfidenceboundson
generated information not supported by or contradicting re- safetymetrics,whileDeepTeam’sredteamingapproach[93]
trieveddocuments,oftenmeasuredviaLLM-as-judge[85]or identifiesvulnerabilitiesthroughsystematictesting. Inaddi-
humanevaluation;CitationAccuracy,assessingcorrectattri- tion, current research indicates defense mechanisms remain
insufficient
bution to sources using Citation Precision and Citation Re- against sophisticated attacks [86–88]. Evalua-
call[20,85];andFaithfulnessMetrics,evaluatinghowaccu- tions reveal significant vulnerabilities in current RAG sys-
|     |     |     |     |     |     |     |     | tems [87,88], | underscoring |     | the | need for | robust | benchmarks |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --- | --- | -------- | ------ | ---------- |
ratelytheoutputreflectsretrievedinformation[83].
Adversarialattackstargetspecificcomponentswithinthe and metrics addressing the unique safety challenges arising
|     |     |     |     |     |     |     |     | fromtheretrieval-generationinterplay. |     |     |     | Furthereffortsarere- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | -------------------- | --- | --- |
RAGpipeline.Knowledgedatabasepoisoning(PoisonedRAG
[86])targetstheretrievalcorpusbyinjectingmalicioustexts quiredtoevaluatethesafetyofRAG.
| that trigger | predetermined |     | outputs | when | retrieved. |     | This at- |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | ------- | ---- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tack vector is evaluated using Attack Success Rate (ASR) 4.2 EfficiencyEvaluation
| and retrieval-focused |     | Precision/Recall/F1 |     |     | metrics. | Retrieval |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------------------- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
EfficiencyisanothercrucialaspectofRAG’sutility,directly
| hijacking | (HijackRAG |     | [87]) exploits |     | ranking | algorithms | to  |     |     |     |     |     |     |     |
| --------- | ---------- | --- | -------------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
linkedtothereal-worldsignificanceofasystem’spopularity,
| prioritizemaliciouscontentduringretrieval, |     |     |     |     |     | withevaluation |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
cost,andeffectiveness.
focusingonattacktransferabilityacrossmodels.Phantomat-
Latencyevaluationtypicallyfocusesontwocriticalmet-
tacks[88]usetrigger-activateddocumentsevaluatedthrough
RetrievalFailureRate(Ret-FR),whilejammingattacks[89] rics. Timetofirsttoken(TTFT)[98]measuresthetimetaken
bythesystemtoproduceitsinitialoutputtokenafterreceiv-
| insert ‘blocker’ |     | documents | that | force | response | refusal, | as- |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ---- | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingaquery,whichisparticularlycrucialforuserexperience
sessedthroughoracle-basedmetrics.
|         |        |             |     |          |       |                |     | as it directly    | impacts | perceived |                | responsiveness. |              | This met- |
| ------- | ------ | ----------- | --- | -------- | ----- | -------------- | --- | ----------------- | ------- | --------- | -------------- | --------------- | ------------ | --------- |
| Privacy | assess | information |     | exposure | risks | from retrieval |     |                   |         |           |                |                 |              |           |
|         |        |             |     |          |       |                |     | ric is especially |         | important | in interactive |                 | applications | where     |
databasesoruserqueries[90].Evaluationofteninvolvessim-
ulatedattacks[91,92]. Keymetricsaboutprivacyincludethe immediate feedback maintains user engagement. Addition-
ally,completeresponsetime(totallatency)measuresthedu-
ExtractionSuccessRate,thefrequencyorsuccessrateofat-
|     |     |     |     |     |     |     |     | ration from | query | submission | to  | the generation |     | of the entire |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---------- | --- | -------------- | --- | ------------- |
tacksextractingspecificprivateinformation(e.g.,names,PII)
|              |           |       |             |          |             |              |     | response.     | Thisencompassesretrievaltime, |     |     |             | processingtime, |             |
| ------------ | --------- | ----- | ----------- | -------- | ----------- | ------------ | --- | ------------- | ----------------------------- | --- | --- | ----------- | --------------- | ----------- |
| from the     | knowledge | base, | often       | measured |             | by the count | of  |               |                               |     |     |             |                 |             |
|              |           |       |             |          |             |              |     | andgeneration | timeforalltokens.             |     |     | Hofstatteet |                 | al.[99]pro- |
| successfully | extracted |       | items [90]; | the      | PII Leakage | Rate,        | the |               |                               |     |     |             |                 |             |
amountorpercentageofPersonallyIdentifiableInformation posedSingleQueryLatencythatreferstothecompleteend-
|               |          |     |              |          |     |           |       | to-end time | taken | to process | a   | single query, | including | both |
| ------------- | -------- | --- | ------------ | -------- | --- | --------- | ----- | ----------- | ----- | ---------- | --- | ------------- | --------- | ---- |
| inadvertently | revealed |     | in generated | outputs, |     | typically | found |             |       |            |     |               |           |      |
completeretrievalandgenerationphases.
viapatternmatchingorinspection[93];andtheMembership
InferenceAttackSuccess,whichmeasuresanattacker’sabil- ResourcesandMoneyCostevaluationofRAGsystemsis
|     |     |     |     |     |     |     |     | anothercriticalcomponentforassessingtheefficiency. |     |     |     |     |     | Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | ---- |
itytodetermineifaspecificdatarecordwasintheRAGsys-
tem’sknowledgebase. evaluationmethodologiestypicallyfocusonquantifyingboth
directexpendituresandefficiencymetricsthatimpactoverall
| Fairness    | examines |           | if the RAG | system | exhibits     | or      | ampli- |        |            |     |       |             |         |        |
| ----------- | -------- | --------- | ---------- | ------ | ------------ | ------- | ------ | ------ | ---------- | --- | ----- | ----------- | ------- | ------ |
|             |          |           |            |        |              |         |        | system | economics. | The | total | cost of RAG | systems | can be |
| fies biases | from     | retrieved | documents  |        | or training, | leading | to     |        |            |     |       |             |         |        |
categorizedintoseveralkeycomponents[126]:
| inequitable | outputs | [94].        | Bias  | Metrics | are          | used to  | analyze |                  |     |        |           |     |                 |     |
| ----------- | ------- | ------------ | ----- | ------- | ------------ | -------- | ------- | ---------------- | --- | ------ | --------- | --- | --------------- | --- |
|             |         |              |       |         |              |          |         | • Infrastructure |     | Costs: | Computing |     | local resources | for |
| the outputs | for     | disparities, | which | are     | quantitative | measures |         |                  |     |        |           |     |                 |     |
ofperformancedisparities(e.g.,errorrates,sentimentscores) embedding generation, vector database maintenance,
andLLMinferenceforopenmodels.
| acrossdemographicgroups[94]. |     |     |     | StereotypeDetectionmea- |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
suresthefrequencyorseverityofharmfulstereotypesingen- • Token-basedExpenses: APIchargesforexternalLLM
servicesbasedoninputandoutputtokenusage.
| erated text, | assessed | via | lists | or human | evaluation. |     | Coun- |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ----- | -------- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
terfactualFairnesschecksifoutputschangeinappropriately • Storage Costs: Vector database hosting and mainte-
whensensitiveattributesinqueriesorcontextarealtered. nanceexpensesthatscalewithcorpussize.

10 Front.Comput.Sci.,2025,0(0):1–18
Table1 OverviewofRAGbenchmarksandtheirevaluationdatasets.SourceDomainindicatesthedataorigin(e.g.,real-timenews,specializedcorpora),
andSpecialPointshighlightuniqueornovelfeatures(likedomain-specifictasks,dynamicchanges,orfalse-premisedata).
Benchmark Time DatasetName(s) SourceDomain SpecialPoints
RAGAS[61] 2023.09 WikiEval Post-2022Wikipedia Manuallylabeledforfaithfulness
FreshLLMs[56] 2023.11 FRESHQA Real-timenews/webqueries DynamicQAwithfalse-premisedetection
RECALL[78] 2023.11 EventKG,UJ MultilingualKGs,sci.terms Edited/counterfactualcontexttests
NQ[100],HotpotQA[101],FEVER[102],
ARES[73] 2023.11 KILTandSuperGLUEcorpora Re-usesclassicQAsets,multi-domain
WoW[103],MultiRC[104],ReCoRD[105]
RGB[85] 2023.12 Customcorpus Latestnewsarticles Emphasizesinfointegration,noiserejections
MultiHop-RAG[7] 2024.01 Generatedcorpus Dailynewssegmentsviamediastack Multi-hopcross-documentqueries
CRUD-RAG[106] 2024.02 Generatedcorpus,UHGEval Chinesenews,domaintexts Create/Read/Update/Deletetasks
MedRAG[107] 2024.02 MIRAGE MedicalQAcorpora Healthcaredomainknowledge
FeB4RAG[108] 2024.02 FeB4RAG,BEIR[109] Federatedsearchtasks Multi-domain,multi-engineretrieval
PubMedQA,CovidQA,HotpotQA,
RAGBench[110] 2024.06 MSMarco,CUAD,DelucionQA, Multi-domaincorpora FaithfulnesswithTRACe(Util,Rel,Adh,Compl)
EManual,TechQA,FinQA,TAT-QA
ReEval[111] 2024.05 NQ(MRQA)+RealTimeQA Wikipedia,real-timeQA Adversarialtestcases
forhallucinationdetection
DomainRAG[112] 2024.06 GeneratedadmissionQA Collegedocswithyearlyupdates Single-/multi-doc,single-/multi-turnQA
TelecomRAGEval.[113] 2024.07 TeleQuAD 3GPP-baseddomaindocs Triple-labeledQAfromSMEs(telecomcontext)
PrivacyQA,CUAD,MAUD,
LegalBench-RAG[114] 2024.08 Expert-annotatedlegalcorpora Emphasizesstrictretrievaloflegaltext
ContractNLI
RAGEval[115] 2024.08 DragonBall Finance,law,medicaldocs Schema-basedgeneration,scenario-specific
CoURAGE[116] 2024.09 RealTimeQA[117],NQ[100] OnlineQA+KILTtasks Hallucinationresilience,dynamicupdates
RAGUnfairness[118] 2024.09 TREC22FairRank,BBQ Wikipedia-basedtrack+socioecon.QA Fairnessmetrics,groupdisparity
CoFE-RAG[119] 2024.10 CoFEdata PDF,DOC,multi-lingualdocs Fine-grainedchunking,multi-keywordapproach
OCRHindersRAG[55] 2024.12 1,261PDFs+8,561images OCRtextfromscanneddocs EvaluatesnoisefromOCRerrors
OmniEval[120] 2024.12 Financedomainset Financialdocs,numerictasks Emphasizesnumericcorrectness/factualQA
CRAG[121] 2024.12 KG+webcorpus Knowledgegraphs+webpages Multi-entityqueries,curateddynamicfacts
RAGPlayground[122] 2024.12 319QApairs Curatedmulti-domaintasks Promptengineering/userflows
MTRAG[123] 2025.01 CLAPNQ,FiQA,Govt,Cloud Wikipedia,finance,gov,techdocs Multi-turn,bridgingqueries
CDQA[124] 2025.01 ChineseDynamicQA RecentChinesenewsqueries Time-varyingevolvinganswers
U-NIAH[125] 2025.03 StarlightAcademy Synthetic“needle-in-haystack”data Evaluatesextremelylongcontexts
Modularorblack-boxapproach
SCARF[54] 2025.04 (User-provided) Genericmulti-domain
integrateswidemetrics(LLMjudge)
• OperationalOverhead:Humansupervision,systemmain- acrossaspectrumofcostconstraintsratherthanatfixed
tenance,andregularupdatestoknowledgebases. operatingpoints.
• Development Costs: Initial implementation, integra- • Comparative Cost Analysis: Methodologies for eval-
tion,andcustomizationexpenses. uating relative cost efficiency between different RAG
Formoredetailsinthetoken-basedexpenses,LLMproviders implementationsforspecificusecases,consideringboth
such as OpenAI and Google offer token usage metrics that directcostsandlong-termeconomicsustainability[129].
track input and output token consumption during evaluation
processes. Thisapproachcalculatescostsbymultiplyingto-
kencountsbytheirrespectivepricingrates[127].Researchers 5 Resources
havedevelopedmetricstoevaluatetheeconomicefficiencyof
Theevaluationmethodologiespreviouslyexaminedarecom-
RAGimplementations:
prehensive, though not necessarily abundant. This section
• Cost-Effectiveness Ratio: Measures performance im-
systematicallycompiles,categorizes,andpresentstheimple-
provement per unit of cost, allowing for standardized
mentedRAGevaluationframeworks,benchmarks,analytical
comparisonbetweendifferentRAGconfigurations[127].
tools, and datasets that have emerged in the large language
• Retrieval Precision ROI: Quantifies the economic re- modelera.Toourknowledge,thiscompilationconstitutesthe
turnofimprovingretrievalprecisionbymeasuringthe most exhaustive collection of RAG evaluation frameworks
reduction in irrelevant context processing costs [127]. currentlydocumentedintheliterature.
Thismetricdemonstratedthatoptimizingretrievalcan Datasets.Wecompiledthebenchmarksalongwiththeas-
improve cost efficiency by up to around 50% through sociateddatasetsinrecentyears. Earlyworksfocusonstatic
reducingtokenconsumptionduringLLMinference. general-purposeQAdatasets(e.g.,NQ[100],HotpotQA[101]),
• User-Controllable Cost-Accuracy Tradeoffs: Su et al. providingwell-establishedbaselinesbutlackrecencyordo-
[128]proposeevaluationmethodsusinganinterpretable main specificity. Recent benchmarks counter these limita-
controlparameter(α)thatallowssystematicassessment tionsby1)sourcinglivenewsorrapidlyupdatedonlinedoc-
of the relationship between retrieval costs and accu- uments (e.g., RGB [85], MultiHop-RAG [7]) to test time-
racy. This approach enables evaluating RAG systems sensitivecapabilities;2)curatingdomain-specificcorporain

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 11
Table2 RAGevaluationframeworks,highlightingprincipalevaluationtargetsandmethods.RetrievalfocusesmainlyonRelevance(R),Correctness
(C)orComprehensiveness,whereasgeneration(right)focusesonFaithfulness(F),Correctness(C),orRelevance(R).Externalevaluationtargets(safety,
efficiency)orotherstatementsappearinitalics.
Type Framework Time RawTargets RetrievalMetrics GenerationMetrics
Research FiD-Light[99] 2023.07 Latency – –
Research DiversityReranker[40] 2023.08 Diversity CosineDistances –
LLMCosSim,
Benchmark RAGAS[61] 2023.09 ContextR,AnswerR,F LLMasJudge
LLMasJudge
Tool TruEraRAGTriad[130] 2023.10 ContextR,AnswerR,Groundedness LLMasJudge LLMasJudge
Tool LangChainBench.[131] 2023.11 C,F,ExecutionTime,EmbCosDist Exact-match LLMasJudge
STRICT/RELAXED,
Benchmark FreshLLMs[56] 2023.11 ResponseC,Fast-changing,Falsepremise (retrievallogs)
FRESHEVAL(LLM-based)
Tool RECALL[78] 2023.11 ResponseQuality,Robustness – BLEU,ROUGE-L
Benchmark ARES[73] 2023.11 ContextR,AnswerF,AnswerR LLM+Classifier L L L L M M + + C C l l a a s s s s i i fi fi e e r r ,
InfoIntegration,NoiseRobust,
Benchmark RGB[85] 2023.12 – Accuracy
NegRejection,Counterfact
Tool DatabricksEval[62] 2023.12 C,Readability,Comprehensiveness – LLMasJudge
Benchmark MultiHop-RAG[7] 2024.01 RetrievalC,ResponseC MAP,MRR,Hit@K LLMasJudge
ROUGE,BLEU,
Benchmark CRUD-RAG[106] 2024.02 Create,Read,Update,Delete –
RAGQuestEval
Benchmark MedRAG[107] 2024.02 Accuracy(medical) – Exact-match,Acc.
HumanEval,
Benchmark FeB4RAG[108] 2024.02 Consistency,C,Clarity,Coverage –
HumanEval
Benchmark ArabicRAGEval.[132] 2024.05 DocR,AnswerR nDCG,MRR,mAP PossiblyCosSimtoQA
ContextR,AnswerR,Explainability,
Benchmark RAGBench[110] 2024.06 TRACe=Util,Rel,Adh,Compl. LLM-basedEval LLM-basedEval,TRACeMetrics
Hallucination F1,EM,Entailment
Benchmark ReEval[111] 2024.05 –
AdversarialAttack LLMorHumanEval
F1,EM,
Benchmark DomainRAG[112] 2024.06 C,F,NoiseRobust,StructOutput –
ROUGE-L,LLM
F1,EM,LLMasJudge,
Benchmark CoURAGE[116] 2024.06 Hallucination –
HumanEval
ContextR,Faithfulness,
Tool TelecomRAGEval.[113] 2024.07 LLM-basedMetrics RAGAS-based,LLMEval
Correctness
Benchmark LegalBench-RAG[114] 2024.08 Doc-levelPrecision,CitationRel. Precision,Recall –
Completeness,Hallucination,
Benchmark RAGEval[115] 2024.08 LLM-basedScoring LLM-based,HumanAlignment
Irrelevance
Benchmark RAGUnfairness[118] 2024.09 Fairness,C,C MRR@K EM,ROUGE
Fine-grainedRetrieval,RespQuality, Recall,Correctness,
Benchmark CoFE-RAG[119] 2024.10 BLEU,ROUGE-L,LLMasJudge
Diversity Multi-keyword
LLMasJudge,
Benchmark TowardInstr.-Following[133] 2024.10 Instr.Relevance,Constraint –
AtomicPassRate
Benchmark OmniEval[120] 2024.12 FactualAcc.,DomainTasks Rule+LLM ManualorLLMFT
Accuracy,Dynamism,ComplexFacts,
Benchmark CRAG[121] 2024.12 Weightedscoring Accuracy,Truthfulnessmeasure
R,C
Accuracy,OCRNoise,
Benchmark OCRHindersRAG[55] 2024.12 EditDist,LCS F1-score
Semanticvs.FormatNoise
RetrievalStrategy,
Benchmark RAGPlayground[122] 2024.12 Comparison-based LLM-basedEval
PromptEng.
Benchmark MTRAG[123] 2025.01 Multi-turnQuality,Conv.C Recall,nDCG LLMasJudge
Benchmark CDQA[124] 2025.01 Accuracy – F1
Benchmark U-NIAH[125] 2025.03 NeedleDetect,LongContext,NoHalluc. Recall LLMJudge,Heatmap
Tool eRAG[134] 2024.04 Doc-levelRel.,DownstreamQuality Doc-levelLLM Kendall’sτ
RAGAS-likeRelevance,
ContextR,AnswerR, LLM-basedor
Tool SCARF[54] 2025.04 Faithfulness BLEU/ROUGE LLM-based
(Black-boxIntegration)
law, healthcare, or finance (e.g., MedRAG [107], OmniEval ingframeworks,asillustratedinTable2. Theseeffortsspan
[120], LegalBench-RAG [114]); or 3) generating synthetic from initial, point-level researches [40,99] to later, multi-
data orspecialized QApairs, possiblywith false-premiseor component evaluation tools and benchmarks [73,131], en-
counterfactualelements(e.g.,FreshLLMs[56],RAGEval[115])compassingaremarkablycomprehensivecollectionofassess-
to assess robustness and misinformation handling. We fur- mentframeworks.Theevaluationmethodsemployedarevar-
therprovideaconcisedescriptionoftheoriginaldomainsand ied,encompassingbothtraditional[78,132]andLLM-based
characteristics according to the original resource, as shown metrics [106,110]. Additionally, there are frameworks that
inTable1. Notedthatonlythedatasetscontainingretrieved facilitatesafety-focusedevaluations[85,116],oraretailored
groundtruthdocumentsareincluded,indicatingaconcernfor tospecificdownstreamdomainslikedocument[55,125],tele-
morein-depthsystemcomponentevaluation. com[113],medicine[107],etc. Referencingthecomponent
Frameworks with Evaluation Methods. We compiled evaluation objectives outlined in section 3.1, we categorize
and summarized the evaluation methods devised by exist- andhighlighttheevaluationelementsandspecificmetrics.

| 12  |     |     |     |     | Front.Comput.Sci.,2025,0(0):1–18 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
srepaP egduJ-sa-MLL fo tnuoC
|     | 100 |     | 90.9% |     |     |     |     |     |     |     | 43  |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
89.3%
40
)%( egatnecreP 80
|     | 60  |     |     |     |     |     | 30  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
47.3%
|     | 40  |     |     |     |     |     | 20  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
12
11
|     | 20  |     |     | 9.1% |     |     | 10  |     |     | 7   |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |      |     |     | 1   | 1   |     |     |     |     |     |
0
|     |     | Retrieval | Generation | Safety Efficiency |     |     | 0       |         |         |         |         |         |     |
| --- | --- | --------- | ---------- | ----------------- | --- | --- | ------- | ------- | ------- | ------- | ------- | ------- | --- |
|     |     |           |            |                   |     |     | 2022 H2 | 2023 H1 | 2023 H2 | 2024 H1 | 2024 H2 | 2025 H1 |     |
Fig.3 StatisticsonthedistributionofRAGstudiesacrossfourkeyareas: Time
retrieval,generation,safety,andefficiency.
Apapermayutilizeevaluation Fig.5 ThenumberofpapersexplicitlymentioningLLM-basedevaluation
methodsinmorethanoneareas. onRAG.The2025H1collectionisuptoMarch31st.
ricsinthesamesessionandexcludedthewordswithglobal
|     |     |     |     |     |     | occurrences | lower | than | twice. | It is observed |     | that traditional |     |
| --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ------ | -------------- | --- | ---------------- | --- |
metricspredominantlydominatetheevaluationusage,while
LLM-basedmethodshavenotyetgainedwidespreadaccep-
|     |     |     |     |     |     | tance | among researchers. |     | This | phenomenon |     | is attributed | to  |
| --- | --- | --- | --- | --- | --- | ----- | ------------------ | --- | ---- | ---------- | --- | ------------- | --- |
thesimplicityandreliabilityoftheconventionalmetrics.Con-
effort
Fig.4 FrequencystatisticswordcloudofevaluationmetricsinRAGstud- versely, the LLM-based methods often require more
ies. TheLLM-basedmethodsarecategorizedbasedonthetargetsandpre- and involve multiple settings that are difficult to keep the
sentedwiththesuffix‘-LLM’.F-scorereferstotheexpandedF1-score. same across different researches, such as the LLM version
andpromptdesign.
|     |     |     |     |     |     | Trend | of LLM | Usage. | Despite | the | potential | issues | with |
| --- | --- | --- | --- | --- | --- | ----- | ------ | ------ | ------- | --- | --------- | ------ | ---- |
6 Discussion
LLM-basedmethods,thereisanobservabletrendofincreas-
6.1 StatisticsandAnalysisofRAGEvaluation ingapplication,asshowninFigure5. 2024H2and2025H1
havethetoptwohighestnumbers.LLMjudgesareultimately
TheproliferationofLLMhascontributedtoasignificantdi-
capableofhandlingmorecomplexdesigns,drawingcloserto
versificationofRAGevaluationmethods.Currentresearches,
|                     |     |               |     |          |              | real-worldapplications. |     |     | LLMitself,additionally,hascontin- |     |     |     |     |
| ------------------- | --- | ------------- | --- | -------- | ------------ | ----------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
| while demonstrating |     | comprehensive |     | coverage | of RAG eval- |                         |     |     |                                   |     |     |     |     |
uedtoevolveinrecentyears,withtheperformanceprogres-
| uation | dimensions, | often | subjectively | assert | their respective |     |     |     |     |     |     |     |     |
| ------ | ----------- | ----- | ------------ | ------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
sivelyimproving,andthesupportedfunctionsexpanding.
utilitystatements.Toassessthepopularityoftheseevaluation
methods, weconductedastatisticalanalysisoftheavailable
6.2 ChallengesandFutureDirections
| methodsfromasurveyperspective. |     |     |     | Thiscanalsobeviewed |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as a research-oriented simple meta-evaluation. We crawled Thissectionaddressesseveralchallengesinherentincontem-
thecollectionofthepaperssince2022autumnwithkeywords poraryRAGevaluation.
about RAG in the accepted papers of the high-level confer- LimitationsofLLM-basedMethods. Thecurrentevalu-
encesaboutNLP&AI,andextractedthecomponentaswell ation design does not sufficiently address the timeliness and
as the evalauation metrics the papers focus and utilize. We the black-box nature inherent in the LLM. The method of
finally amassed a total of 582 PDF manuscripts. All the in- employing LLMs for assessments, particularly through di-
cludedpapershaveundergonerigorouspeerreview,demon- rect prompts, raises latent risk about stability and security.
stratingscholarlymeritwithcompleteexperimentalmethod- Futureresearchshouldfocusonenhancingtherobustnessof
ologiesandlogicallystructuredevaluationprocedures. theevaluationprocessitselfandminimizingthelikelihoodof
ResearchFocus. Figure3illustratesthestatisticaldistri- LLMerrorsintheRAGsystem.
different
bution of evaluation methods used across the four Cost of Evaluation. The cost associated with the RAG
segments in RAG studies (Retrieval / Generation / Safety / systemhasgarneredattention.Nevertheless,athorougheval-
Efficiency).
Thedatasuggestsaprevailingfocusoninternal uation remains expensive due to the vast scale of the tools
efficient
researchandevaluationofRAGsystems,asindicatedbythe and datasets involved. Determining an method for
extensivecoverageoftheretrievalandgenerationprocesses. systemevaluation,orstrikingabalancebetweencostandef-
Incontrast,externalevaluations,particularlythoserelatedto fectiveness,isoneofthedirectionsforfutureresearch.
safety,havegarneredlessattention. Advanced Evaluation Methods. As LLMs continue to
Metric Preference. Word frequency counts were con- evolve,thecomponentsofRAGsystemsarebecomingmore
ducted for the assessment metrics mentioned in the papers, diverse. Currently, manyofthesecomponentsareevaluated
withthewordclouddisplayedinFigure4. Wheneveramet- usingend-to-endRAGontologymetrics,withalackofcom-
ricisformallyintroducedinthebodyofapaperorreportedin prehensive functional decomposition evaluation or theoreti-
thetableofexperimentalresults,itswordfrequencycountis calanalysis. Concurrently,thereremainsuntappedpotential
set+1. Wemanuallymergedandmappedsynonymousmet- inthefunctionalitiesofLLMsthemselves. Forinstance,the

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 13
evaluationaboutdeepthinkingmodels(e.g.openai-o1[135])
|     |     |     |     |     |     | 4. YaoJY,NingKP,LiuZH,NingMN,YuanL. |     |     | Llmlies: | Hallu- |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | -------- | ------ |
alongwiththethinkingprocessofLLMsinconjunctionwith cinationsarenotbugs,butfeaturesasadversarialexamples. arXiv
| RAG’s retrieval | and | generation | process, | is still | inadequate. |     |     |     |     |     |
| --------------- | --- | ---------- | -------- | -------- | ----------- | --- | --- | --- | --- | --- |
preprintarXiv:2310.01469,2023
These in-depth evaluation strategies require further research 5. Wang L, Yang N, Huang X, Jiao B, Yang L, Jiang D, Majumder
anddevelopmentinthefuture.
|     |     |     |     |     |     | R,WeiF. | Textembeddingsbyweakly-supervisedcontrastivepre- |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------------------------------------------ | --- | --- | --- |
ComprehensivenessoftheEvaluationFramework.De-
training.arXivpreprintarXiv:2212.03533,2022
spitetheabundantevaluationframeworksatpresent,individ-
6. RobertsonS,ZaragozaH,others.Theprobabilisticrelevanceframe-
ualonesaresomewhatlimitedintheirmetricsandmethodsof
FoundationsandTrends®inInformation
work: Bm25andbeyond.
| evaluation. | Moreover, | most | contemporary | frameworks | con- |     |     |     |     |     |
| ----------- | --------- | ---- | ------------ | ---------- | ---- | --- | --- | --- | --- | --- |
Retrieval,2009,3(4):333–389
centrateonwidelyusedlanguagessuchasEnglishandChi-
nese. There is an urgent need for frameworks that are not 7. TangY,YangY. Multihop-rag: Benchmarkingretrieval-augmented
|     |     |     |     |     |     | generationformulti-hopqueries. |     | arXivpreprintarXiv:2401.15391, |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ------------------------------ | --- | --- |
onlymethodologicallybutalsolinguisticallydiverse.
2024
8. SunJ,XuC,TangL,WangS,LinC,GongY,ShumHY,GuoJ.
|              |     |     |     |     |     | Think-on-graph:                   | Deepandresponsiblereasoningoflargelanguage |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --------------------------------- | ------------------------------------------ | --- | --- | --- |
| 7 Conclusion |     |     |     |     |     | modelwithknowledgegraph.CoRR,2023 |                                            |     |     |     |
9. GaoY,XiongY,GaoX,JiaK,PanJ,BiY,DaiY,SunJ,WangH,
Inthispaper,wehavepresentedthefirstcomprehensivesur-
WangH.Retrieval-augmentedgenerationforlargelanguagemodels:
| veyofRAGevaluationmethodologiesintheLLMera. |     |     |     |     | Our |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Asurvey.arXivpreprintarXiv:2312.10997,2023,2
systematicanalysisrevealsseveralimportantinsightsforre-
searchers and practitioners working with these increasingly 10. BrownT,MannB,RyderN,SubbiahM,KaplanJD,DhariwalP,
NeelakantanA,ShyamP,SastryG,AskellA,others.Languagemod-
| prevalent | systems. | For the | evaluation | of internal | RAG per- |     |     |     |     |     |
| --------- | -------- | ------- | ---------- | ----------- | -------- | --- | --- | --- | --- | --- |
formance, we dissect the internal components of RAG sys- elsarefew-shotlearners. Advancesinneuralinformationprocessing
tems,definetheassessmentobjectives,andgatherarangeof systems,2020,33:1877–1901
methods and metrics from traditional to innovative. More- 11. ZhaoWX,ZhouK,LiJ,TangT,WangX,HouY,MinY,ZhangB,
over,weinvestigatetheexternalevaluationrelatedtosystem ZhangJ,DongZ,others. Asurveyoflargelanguagemodels. arXiv
efficiency,
integrity such as safety and which are underex- preprintarXiv:2303.18223,2023
plored in RAG research according to our statistical analy- 12. YildirimI,PaulL. Fromtaskstructurestoworldmodels: whatdo
sis.Additionally,wecompileandcategorizethecurrenteval-
|                 |     |            |              |     |            | llmsknow? | TrendsinCognitiveSciences,2024 |     |     |     |
| --------------- | --- | ---------- | ------------ | --- | ---------- | --------- | ------------------------------ | --- | --- | --- |
| uation datasets | and | frameworks | to elucidate | the | unique at- |           |                                |     |     |     |
13. ZhangS,DongL,LiX,ZhangS,SunX,WangS,LiJ,HuR,Zhang
| tributesandassessmentfocusesoftheresources. |         |                    |     |             | Lastbutnot |               |                                          |     |     |     |
| ------------------------------------------- | ------- | ------------------ | --- | ----------- | ---------- | ------------- | ---------------------------------------- | --- | --- | --- |
|                                             |         |                    |     |             |            | T,WuF,others. | Instructiontuningforlargelanguagemodels: |     |     | A   |
| least, we                                   | analyze | the implementation |     | of existing | evaluation |               |                                          |     |     |     |
survey.arXivpreprintarXiv:2308.10792,2023
| methodsand | synthesizethechallenges |     |     | andfuturedirections |     |           |                       |                   |                   |     |
| ---------- | ----------------------- | --- | --- | ------------------- | --- | --------- | --------------------- | ----------------- | ----------------- | --- |
|            |                         |     |     |                     |     | 14. Verma | P, Pilanci M. Towards | signal processing | in large language |     |
ofRAGevaluationintheLLMera.
models.arXivpreprintarXiv:2406.10254,2024
15. LyuH,JiangS,ZengH,XiaY,WangQ,ZhangS,ChenR,LeungC,
Acknowledgements
TangJ,LuoJ.Llm-rec:Personalizedrecommendationviaprompting
largelanguagemodels.In:FindingsoftheAssociationforComputa-
| Competing | interests | The authors | declare that | they have | no competing |     |     |     |     |     |
| --------- | --------- | ----------- | ------------ | --------- | ------------ | --- | --- | --- | --- | --- |
interestsorfinancialconflictstodisclose. tionalLinguistics:NAACL2024.2024,583–612
|            |     |     |     |     |     | 16. ZhangB,LiuZ,CherryC,FiratO. |                                           | Whenscalingmeetsllmfine-          |     |       |
| ---------- | --- | --- | --- | --- | --- | ------------------------------- | ----------------------------------------- | --------------------------------- | --- | ----- |
|            |     |     |     |     |     | tuning:                         | Theeffectofdata,modelandfinetuningmethod. |                                   | In: | ICLR. |
| References |     |     |     |     |     | 2024                            |                                           |                                   |     |       |
|            |     |     |     |     |     | 17. ReynoldsL,McDonellK.        |                                           | Promptprogrammingforlargelanguage |     |       |
1. FanW,DingY,NingL,WangS,LiH,YinD,ChuaTS,LiQ.Asur- models:Beyondthefew-shotparadigm.In:Extendedabstractsofthe
veyonragmeetingllms:Towardsretrieval-augmentedlargelanguage 2021CHIconferenceonhumanfactorsincomputingsystems.2021,
| models. | In: Proceedingsofthe30thACMSIGKDDConferenceon |     |     |     |     | 1–7 |     |     |     |     |
| ------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
KnowledgeDiscoveryandDataMining.2024,6491–6501 18. WeiJ,WangX,SchuurmansD,BosmaM,XiaF,ChiE,LeQV,Zhou
2. Gutie´rrezBJ,ShuY,GuY,YasunagaM,SuY. Hipporag: Neuro- D,others.Chain-of-thoughtpromptingelicitsreasoninginlargelan-
biologicallyinspiredlong-termmemoryforlargelanguagemodels. guagemodels. Advancesinneuralinformationprocessingsystems,
| arXivpreprintarXiv:2405.14831,2024 |     |     |     |     |     | 2022,35:24824–24837 |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
3. ZhangY,KhalifaM,LogeswaranL,LeeM,LeeH,WangL. Merg- 19. HuangY,HuangJ. Asurveyonretrieval-augmentedtextgeneration
ingGeneratedandRetrievedKnowledgeforOpen-DomainQA. In: forlargelanguagemodels.arXivpreprintarXiv:2404.10981,2024
BouamorH,PinoJ,BaliK,eds,Proceedingsofthe2023Conference 20. ZhouY,LiuY,LiX,JinJ,QianH,LiuZ,LiC,DouZ,HoTY,
onEmpiricalMethodsinNaturalLanguageProcessing. December YuPS. Trustworthinessinretrieval-augmentedgenerationsystems:
| 2023,4710–4728 |     |     |     |     |     | Asurvey.arXivpreprintarXiv:2409.10102,2024 |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- |

14 Front.Comput.Sci.,2025,0(0):1–18
21. YuH,GanA,ZhangK,TongS,LiuQ,LiuZ.Evaluationofretrieval- ume1:LongPapers).August2021,4089–4100
augmentedgeneration: Asurvey. In: CCFConferenceonBigData. 37. Mekala D, Vu T, Schick T, Shang J. Leveraging QA datasets to
2024,102–120 improve generative data augmentation. In: Goldberg Y, Kozareva
22. LewisP,PerezE,PiktusA,PetroniF,KarpukhinV,GoyalN,Ku¨ttler Z,ZhangY,eds,Proceedingsofthe2022ConferenceonEmpirical
H,LewisM,YihWt,Rockta¨schelT,others. Retrieval-augmented MethodsinNaturalLanguageProcessing. December2022, 9737–
generation for knowledge-intensive nlp tasks. Advances in neural 9750
informationprocessingsystems,2020,33:9459–9474 38. AsaiA,WuZ,WangY,SilA,HajishirziH.Self-rag:Learningtore-
23. LiH,SuY,CaiD,WangY,LiuL. Asurveyonretrieval-augmented trieve,generate,andcritiquethroughself-reflection. In:TheTwelfth
textgeneration.arXivpreprintarXiv:2202.01110,2022 InternationalConferenceonLearningRepresentations.2023
24. Dinan E, Roller S, Shuster K, Fan A, Auli M, Weston J. Wiz- 39. DouzeM,GuzhvaA,DengC,JohnsonJ,SzilvasyG,Mazare´ PE,
ardofwikipedia: Knowledge-poweredconversationalagents. arXiv LomeliM,HosseiniL,Je´gouH.Thefaisslibrary.CoRR,2024
preprintarXiv:1811.01241,2018 40. BlagojevicV. EnhancingRAGPipelinesinHaystack: Introducing
25. QinL,GalleyM,BrockettC,LiuX,GaoX,DolanWB,ChoiY,Gao DiversityRankerandLostInTheMiddleRanker,August2023
J. Conversingbyreading: Contentfulneuralconversationwithon- 41. BestaM,BlachN,KubicekA,GerstenbergerR,PodstawskiM,Gi-
demandmachinereading. In:Proceedingsofthe57thAnnualMeet- aninazziL,GajdaJ,LehmannT,NiewiadomskiH,NyczykP,others
ingoftheAssociationforComputationalLinguistics. 2019,5427– .Graphofthoughts:Solvingelaborateproblemswithlargelanguage
5436 models. In:ProceedingsoftheAAAIConferenceonArtificialIntel-
26. KobayashiM,TakedaK. Informationretrievalontheweb. ACM ligence.2024,17682–17690
computingsurveys(CSUR),2000,32(2):144–173 42. LanchantinJ,ToshniwalS,WestonJ,SukhbaatarS,others.Learning
27. LeeH,YangS,OhH,SeoM. Generativemulti-hopretrieval. In: toreasonandmemorizewithself-notes. AdvancesinNeuralInfor-
Proceedingsofthe2022ConferenceonEmpiricalMethodsinNatural mationProcessingSystems,2023,36:11891–11911
LanguageProcessing.2022,1417–1436 43. DengY,ZhangW,ChenZ,GuQ. Rephraseandrespond: Letlarge
28. ZhangS,YaoL,SunA,TayY. Deeplearningbasedrecommender languagemodelsaskbetterquestionsforthemselves.CoRR,2023
system: Asurveyandnewperspectives. ACMComputingSurveys, 44. Wang C, Liu X, Yue Y, Tang X, Zhang T, Jiayang C, Yao Y, Gao
2019,52(1):1–38 W, Hu X, Qi Z, others . Survey on factuality in large language
29. Wang W, Lin X, Feng F, He X, Chua T S. Generative recom- models:Knowledge,retrievalanddomain-specificity. arXivpreprint
mendation: Towardsnext-generationrecommenderparadigm. arXiv arXiv:2310.07521,2023
preprintarXiv:2304.03516,2023 45. ZhaoP,ZhangH,YuQ,WangZ,GengY,FuF,YangL,ZhangW,
30. KarpukhinV,OguzB,MinS,LewisP,WuL,EdunovS,ChenD,Yih CuiB. Retrieval-augmentedgenerationforai-generatedcontent: A
Wt. Densepassageretrievalforopen-domainquestionanswering. survey.CoRR,2024
In: WebberB,CohnT,HeY,LiuY,eds, Proceedingsofthe2020 46. ChengM,LuoY,OuyangJ,LiuQ,LiuH,LiL,YuS,ZhangB,Cao
ConferenceonEmpiricalMethodsinNaturalLanguageProcessing J,MaJ,others.Asurveyonknowledge-orientedretrieval-augmented
(EMNLP).November2020,6769–6781 generation.arXivpreprintarXiv:2503.10677,2025
31. Google.ProgrammableSearchEngine|GoogleforDevelopers,2024 47. Ja¨rvelinK,Keka¨la¨inenJ.Cumulatedgain-basedevaluationofirtech-
32. Yepes A J, You Y, Milczek J, Laverde S, Li R. Financial report niques. ACMTransactionsonInformationSystems(TOIS),2002,
chunkingforeffectiveretrievalaugmentedgeneration.arXivpreprint 20(4):422–446
arXiv:2402.05131,2024 48. Sankoff D, Kruskal J B. Time warps, string edits, and macro-
33. FanW,DingY,NingL,WangS,LiH,YinD,ChuaTS,LiQ.Asur- molecules:thetheoryandpracticeofsequencecomparison.Reading:
veyonragmeetingllms:Towardsretrieval-augmentedlargelanguage Addison-WesleyPublication,1983
models. In: Proceedingsofthe30thACMSIGKDDConferenceon 49. YujianL,BoL. Anormalizedlevenshteindistancemetric. IEEE
KnowledgeDiscoveryandDataMining.2024,6491–6501 transactions on pattern analysis and machine intelligence, 2007,
34. SinghIS,AggarwalR,AllahverdiyevI,TahaM,AkalinA,ZhuK, 29(6):1091–1095
O’BrienS. Chunkrag:Novelllm-chunkfilteringmethodforragsys- 50. LinCY.ROUGE:Apackageforautomaticevaluationofsummaries.
tems.arXivpreprintarXiv:2410.19572,2024 In:TextSummarizationBranchesOut.July2004,74–81
35. Multi-Granularity M L M F. M3-embedding: Multi-linguality, 51. PapineniK,RoukosS,WardT,ZhuWJ. Bleu: amethodforauto-
multi-functionality, multi-granularitytextembeddingsthroughself- maticevaluationofmachinetranslation. In: IsabelleP,CharniakE,
knowledgedistillation.2024 LinD,eds,Proceedingsofthe40thAnnualMeetingoftheAssocia-
36. MaoY,HeP,LiuX,ShenY,GaoJ,HanJ,ChenW. Generation- tionforComputationalLinguistics.July2002,311–318
augmentedretrievalforopen-domainquestionanswering. In: Zong 52. BanerjeeS,LavieA. Meteor:Anautomaticmetricformtevaluation
C,XiaF,LiW,NavigliR,eds,Proceedingsofthe59thAnnualMeet- withimprovedcorrelationwithhumanjudgments. In: Proceedings
ing of the Association for Computational Linguistics and the 11th oftheaclworkshoponintrinsicandextrinsicevaluationmeasuresfor
InternationalJointConferenceonNaturalLanguageProcessing(Vol- machinetranslationand/orsummarization.2005,65–72

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 15
53. ZhangT,KishoreV,WuF,WeinbergerKQ,ArtziY. BERTScore: Linguistics:EMNLP2024.2024,4852–4872
EvaluatingTextGenerationwithBERT. In: 8thInternationalCon- 68. LiM,LiX,ChenY,XuanW,ZhangW. Unravelingandmitigating
ference on Learning Representations, ICLR 2020, Addis Ababa, retrieverinconsistenciesinretrieval-augmentedlargelanguagemod-
Ethiopia,April26-30,2020.2020 els. In: FindingsoftheAssociationforComputationalLinguistics
54. Rengo M, Beadini S, Alfano D, Abbruzzese R. A system for ACL2024.2024,4833–4850
comprehensive assessment of rag frameworks. arXiv preprint 69. MinS,KrishnaK,LyuX,LewisM,YihWt,KohP,IyyerM,Zettle-
arXiv:2504.07803,2025 moyer L, Hajishirzi H. Factscore: Fine-grained atomic evaluation
55. ZhangJ,ZhangQ,WangB,OuyangL,WenZ,LiY,ChowKH,HeC, offactualprecisioninlongformtextgeneration. In: Proceedings
ZhangW. Ocrhindersrag: Evaluatingthecascadingimpactofocr ofthe2023ConferenceonEmpiricalMethodsinNaturalLanguage
onretrieval-augmentedgeneration.arXivpreprintarXiv:2412.02592, Processing.2023,12076–12100
2024 70. Song Y, Kim Y, Iyyer M. Veriscore: Evaluating the factuality
56. VuT,IyyerM,WangX,ConstantN,WeiJ,WeiJ,TarC,SungYH, of verifiable claims in long-form text generation. arXiv preprint
Zhou D, Le Q, Luong T. FreshLLMs: Refreshing large language arXiv:2406.19276,2024
modelswithsearchengineaugmentation. In: KuLW,MartinsA, 71. Chen L, Zhang R, Guo J, Fan Y, Cheng X. Controlling risk of
SrikumarV,eds,FindingsoftheAssociationforComputationalLin- retrieval-augmentedgeneration: Acounterfactualpromptingframe-
guistics:ACL2024.August2024,13697–13720 work.In:FindingsoftheAssociationforComputationalLinguistics:
57. SælemyrJ,FemdalHT. Chunksmarter,retrievebetter: Enhancing EMNLP2024.2024,2380–2393
llmsinfinance: Anempiricalcomparisonofchunkingtechniquesin 72. FuJ,NgSK,JiangZ,LiuP. Gptscore: Evaluateasyoudesire. In:
retrievalaugmentedgenerationforfinancialreports. Master’sthesis, Proceedingsofthe2024ConferenceoftheNorthAmericanChapter
NORWEGIANSCHOOLOFECONOMICS,2024 oftheAssociationforComputationalLinguistics: HumanLanguage
58. FinardiP,AvilaL,CastaldoniR,GengoP,LarcherC,PiauM,Costa Technologies(Volume1:LongPapers).2024,6556–6576
P,Carida´V. Thechroniclesofrag: Theretriever,thechunkandthe 73. Saad-FalconJ,KhattabO,PottsC,ZahariaM. Ares: Anautomated
generator.arXivpreprintarXiv:2401.07883,2024 evaluationframeworkforretrieval-augmentedgenerationsystems.In:
59. MuennighoffN,TaziN,MagneL,ReimersN. Mteb: Massivetext Proceedingsofthe2024ConferenceoftheNorthAmericanChapter
embeddingbenchmark.arXivpreprintarXiv:2210.07316,2022 oftheAssociationforComputationalLinguistics: HumanLanguage
60. EnevoldsenK,ChungI,KerbouaI,KardosM,MathurA,StapD, Technologies(Volume1:LongPapers).2024,338–354
Gala J, Siblini W, Krzemin´ski D, Winata G I, others . Mmteb: 74. ZhaoX,ZhangH,PanX,YaoW,YuD,ChenJ. Thrust:Adaptively
Massive multilingual text embedding benchmark. arXiv preprint propelslargelanguagemodelswithexternalknowledge.Advancesin
arXiv:2502.13595,2025 NeuralInformationProcessingSystems,2023,36:69930–69948
61. EsS,JamesJ,AnkeLE,SchockaertS. Ragas: Automatedevalua- 75. Zhu K, Feng X, Du X, Gu Y, Yu W, Wang H, Chen Q, Chu Z,
tionofretrievalaugmentedgeneration. In: Proceedingsofthe18th Chen J, Qin B. An information bottleneck perspective for effec-
ConferenceoftheEuropeanChapteroftheAssociationforCompu- tivenoisefilteringonretrieval-augmentedgeneration. arXivpreprint
tationalLinguistics:SystemDemonstrations.2024,150–158 arXiv:2406.01549,2024
62. Leng Q, Uhlenhuth K, Polyzotis A. Best practices for llm eval- 76. LiD,YanJ,ZhangT,WangC,HeX,HuangL,XueH,HuangJ.On
uation of rag applications (2023). URL https://www. databricks. theroleoflong-tailknowledgeinretrievalaugmentedlargelanguage
com/blog/LLM-auto-eval-best-practices-RAG models.arXivpreprintarXiv:2406.16367,2024
63. ZhangH,SemnaniS,GhassemiF,XuJ,LiuS,LamM. Spaghetti: 77. SunZ,ZangX,ZhengK,SongY,XuJ,ZhangX,YuW,LiH. Re-
Open-domainquestionansweringfromheterogeneousdatasources deep: Detectinghallucinationinretrieval-augmentedgenerationvia
withretrievalandsemanticparsing. In: FindingsoftheAssociation mechanisticinterpretability.arXivpreprintarXiv:2410.11414,2024
forComputationalLinguisticsACL2024.2024,1663–1678 78. LiuY,HuangL,LiS,ChenS,ZhouH,MengF,ZhouJ,SunX. Re-
64. FinsåsM,MaksimJ. Optimizingragsystemsfortechnicalsupport call:Abenchmarkforllmsrobustnessagainstexternalcounterfactual
withllm-basedrelevancefeedbackandmulti-agentpatterns.Master’s knowledge.arXivpreprintarXiv:2311.08147,2023
thesis,NTNU,2024 79. WuS,XieJ,ChenJ,ZhuT,ZhangK,XiaoY. Howeasilydoir-
65. PatilSG,ZhangT,WangX,GonzalezJE. Gorilla:Largelanguage relevantinputsskewtheresponsesoflargelanguagemodels? arXiv
modelconnectedwithmassiveapis.AdvancesinNeuralInformation preprintarXiv:2404.03302,2024
ProcessingSystems,2024,37:126544–126565 80. Liang X, Niu S, Li Z, Zhang S, Wang H, Xiong F, Fan J Z, Tang
66. DaiL,XuY,YeJ,LiuH,XiongH. Seper: Measureretrievalutil- B, Song S, Wang M, others . Saferag: Benchmarking security
itythroughthelensofsemanticperplexityreduction. arXivpreprint in retrieval-augmented generation of large language model. arXiv
arXiv:2503.01478,2025 preprintarXiv:2501.18636,2025
67. QiZ,XuR,GuoZ,WangC,ZhangH,XuW. Long2rag: Evalu- 81. KangM,Gu¨relNM,YuN,SongD,LiB. C-rag: Certifiedgenera-
atinglong-context&long-formretrieval-augmentedgenerationwith tionrisksforretrieval-augmentedlanguagemodels. In:International
keypointrecall. In: FindingsoftheAssociationforComputational ConferenceonMachineLearning.2024,22963–23000

16 Front.Comput.Sci.,2025,0(0):1–18
82. ChengX,WangX,ZhangX,GeT,ChenSQ,WeiF,ZhangH,Zhao EffectiveRetrieval-AugmentedTextGeneration. In: Proceedingsof
D. xrag: Extremecontextcompressionforretrieval-augmentedgen- the46thInternationalACMSIGIRConferenceonResearchandDe-
erationwithonetoken.arXivpreprintarXiv:2405.13792,2024 velopmentinInformationRetrieval, SIGIR’23. July2023, 1437–
83. AsaiA,WuZ,WangY,SilA,HajishirziH.Self-rag:Learningtore- 1447
trieve,generate,andcritiquethroughself-reflection. In:TheTwelfth 100. KwiatkowskiT,PalomakiJ,RedfieldO,CollinsM,ParikhA,Alberti
InternationalConferenceonLearningRepresentations.2023 C,EpsteinD,PolosukhinI,DevlinJ,LeeK,ToutanovaK,JonesL,
84. Trivedi H, Balasubramanian N, Khot T, Sabharwal A. Interleav- KelceyM,ChangMW,DaiAM,UszkoreitJ,LeQ,PetrovS.Natu-
ingretrievalwithchain-of-thoughtreasoningforknowledge-intensive ralquestions:Abenchmarkforquestionansweringresearch. Trans-
multi-stepquestions.In:ACL(1).2023,10014–10037 actions of the Association for Computational Linguistics, 2019, 7:
85. ChenJ,LinH,HanX,SunL. Benchmarkinglargelanguagemod- 453–466
elsinretrieval-augmentedgeneration. In: ProceedingsoftheAAAI 101. Yang Z, Qi P, Zhang S, Bengio Y, Cohen W W, Salakhutdinov R,
ConferenceonArtificialIntelligence.2024,17754–17762 ManningCD. HotpotQA:Adatasetfordiverse,explainablemulti-
86. ZouW,GengR,WangB,JiaJ. Poisonedrag:Knowledgecorruption hopquestionanswering. In: ConferenceonEmpiricalMethodsin
attackstoretrieval-augmentedgenerationoflargelanguagemodels. NaturalLanguageProcessing(EMNLP).2018
arXivpreprintarXiv:2402.07867,2024 102. ThorneJ,VlachosA,ChristodoulopoulosC,MittalA. FEVER:a
87. ZhangY,LiQ,DuT,ZhangX,ZhaoX,FengZ,YinJ. Hijackrag: large-scaledatasetforfactextractionandVERification.In:NAACL-
Hijackingattacksagainstretrieval-augmentedlargelanguagemodels. HLT.2018
arXivpreprintarXiv:2410.22832,2024 103. Dinan E, Roller S, Shuster K, Fan A, Auli M, Weston J. Wizard
88. ChaudhariH,SeveriG,AbascalJ,JagielskiM,Choquette-ChooCA, ofWikipedia: Knowledge-poweredconversationalagents. In: Pro-
Nasr M, Nita-Rotaru C, Oprea A. Phantom: General trigger at- ceedingsoftheInternationalConferenceonLearningRepresentations
tacks on retrieval augmented language generation. arXiv preprint (ICLR).2019
arXiv:2405.20485,2024 104. DeYoungJ,JainS,RajaniNF,LehmanE,XiongC,SocherR,Wal-
89. ShafranA,SchusterR,ShmatikovV. Machineagainsttherag:Jam- laceBC. Eraser: Abenchmarktoevaluaterationalizednlpmodels.
mingretrieval-augmentedgenerationwithblockerdocuments. arXiv In: Proceedingsofthe58thAnnualMeetingoftheAssociationfor
preprintarXiv:2406.05870,2024 ComputationalLinguistics.2020,4443–4458
90. ZengS,ZhangJ,HeP,LiuY,XingY,XuH,RenJ,ChangY,Wang 105. ZhangS,LiuX,LiuJ,GaoJ,DuhK,VanDurmeB.Record:Bridging
S,YinD,others. Thegoodandthebad:Exploringprivacyissuesin thegapbetweenhumanandmachinecommonsensereadingcompre-
retrieval-augmentedgeneration(rag).In:FindingsoftheAssociation hension.arXivpreprintarXiv:1810.12885,2018
forComputationalLinguisticsACL2024.2024,4505–4524 106. LyuY,LiZ,NiuS,XiongF,TangB,WangW,WuH,LiuH,XuT,
91. ChengP,DingY,JuT,WuZ,DuW,YiP,ZhangZ,LiuG. Trojan- ChenE.Crud-rag:Acomprehensivechinesebenchmarkforretrieval-
rag:Retrieval-augmentedgenerationcanbebackdoordriverinlarge augmentedgenerationoflargelanguagemodels. ACMTrans.Inf.
languagemodels.arXivpreprintarXiv:2405.13401,2024 Syst.,2025,43(2)
92. ChaudhariH,SeveriG,AbascalJ,JagielskiM,Choquette-ChooCA, 107. XiongG,JinQ,LuZ,ZhangA. Benchmarkingretrieval-augmented
Nasr M, Nita-Rotaru C, Oprea A. Phantom: General trigger at- generationformedicine.In:FindingsoftheAssociationforCompu-
tacks on retrieval augmented language generation. arXiv preprint tationalLinguisticsACL2024.2024,6233–6251
arXiv:2405.20485,2024 108. Wang S, Khramtsova E, Zhuang S, Zuccon G. Feb4rag: Evaluat-
93. Perez E, Huang S, Song F, Cai T, Ring R, Aslanides J, Glaese A, ingfederatedsearchinthecontextofretrievalaugmentedgeneration.
McAleeseN,IrvingG. Redteaminglanguagemodelswithlanguage In:Proceedingsofthe47thInternationalACMSIGIRConferenceon
models,2022 ResearchandDevelopmentinInformationRetrieval.2024,763–773
94. Shrestha R, Zou Y, Chen Q, Li Z, Xie Y, Deng S. Fairrag: Fair 109. KamallooE,ThakurN,LassanceC,MaX,YangJH,LinJ. Re-
human generation via fair retrieval augmentation. CoRR, 2024, sourcesforbrewingbeir: reproduciblereferencemodelsandanoffi-
abs/2403.19964 cialleaderboard,2023
95. Zhou Y, Liu Z, Jin J, Nie J Y, Dou Z. Metacognitive retrieval- 110. Friel R, Belyi M, Sanyal A. Ragbench: Explainable bench-
augmentedlargelanguagemodels.In:WWW.2024,1453–1463 mark for retrieval-augmented generation systems. arXiv preprint
96. SudhiV,BhatSR,RudatM,TeucherR. Rag-ex: Agenericframe- arXiv:2407.11005,2024
workforexplainingretrievalaugmentedgeneration.In:SIGIR.2024, 111. YuX,ChengH,LiuX,RothD,GaoJ. ReEval: Automatichalluci-
2776–2780 nationevaluationforretrieval-augmentedlargelanguagemodelsvia
97. Ding T, Banerjee A, Mombaerts L, Li Y, Borogovac T, Weinstein transferableadversarialattacks.In:DuhK,GomezH,BethardS,eds,
JPDlC. Vera: Validationandevaluationofretrieval-augmented FindingsoftheAssociationforComputationalLinguistics: NAACL
systems.arXivpreprintarXiv:2409.03759,2024 2024.June2024,1333–1351
98. Anthropic.Reducinglatency,January2025 112. WangS,LiuJ,SongS,ChengJ,FuY,GuoP,FangK,ZhuY,Dou
99. Hofsta¨tterS,ChenJ,RamanK,ZamaniH. FiD-Light:Efficientand Z. Domainrag:Achinesebenchmarkforevaluatingdomain-specific

AoranGANetal.RetrievalAugmentedGenerationEvaluationintheEraofLLMs 17
retrieval-augmentedgeneration.CoRR,2024 126. SelvarajT.Calculatethetotalcostofaretrievalaugmentedgeneration
113. RoychowdhuryS,SomanS,RanjaniH,GundaN,ChhabraV,BALA (rag)solution,February2024
SK.Evaluationofragmetricsforquestionansweringinthetelecom 127. ZhangJ,LiG,SuJ. Sage:Aframeworkofpreciseretrievalforrag.
domain. ICML2024WorkshoponFoundationModelsintheWild, arXivpreprintarXiv:2503.01713,2025
2024 128. SuJ,HealeyJ,NakovP,CardieC.Fastorbetter?balancingaccuracy
114. Pipitone N, Alami G H. Legalbench-rag: A benchmark for andcostinretrieval-augmentedgenerationwithflexibleusercontrol.
| retrieval-augmentedgenerationinthelegaldomain. |     |     |     |     | arXivpreprint |     | CoRR,2025 |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- |
S¸akarT,EmekciH.Maximizingragefficiency:Acomparativeanaly-
| arXiv:2408.10343,2024 |     |     |     |     |     | 129. |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
115. ZhuK,LuoY,XuD,WangR,YuS,WangS,YanY,LiuZ,Han sisofragmethods.NaturalLanguageProcessing,2025,31(1):1–25
X,LiuZ,others. Rageval: Scenariospecificragevaluationdataset 130. DattaA,FredriksonM,LeinoK,LuK,SenS,ShihR,WangZ. Ex-
generationframework.CoRR,2024 ploringconceptualsoundnesswithtrulens. In: NeurIPS2021Com-
116. GallaD,HodaS,ZhangM,QuanW,YangTD,VoylesJ.Courage:A petitionsandDemonstrationsTrack.2022,302–307
frameworktoevaluateragsystems. In:RappA,DiCaroL,Meziane 131. LangChain . Evaluating rag architectures on benchmark tasks,
| F,SugumaranV,eds,NaturalLanguageProcessingandInformation |     |     |     |     |     |     | November2023 |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
Systems.2024,392–407 132. Mahboub A, Za’ter M E, Al-Rfooh B, Estaitia Y, Jaljuli A, Hak-
117. Kasai J, Sakaguchi K, Le Bras R, Asai A, Yu X, Radev D, Smith ouz A. Evaluation of semantic search and its role in retrieved-
NA,ChoiY,InuiK,others. Realtimeqa: What’stheanswerright augmented-generation (rag) for arabic language. arXiv preprint
now? Advancesinneuralinformationprocessingsystems,2023,36: arXiv:2403.18350,2024
49025–49043 133. DongG,SongX,ZhuY,QiaoR,DouZ,WenJR. Towardgeneral
118. WuX,LiS,WuHT,TaoZ,FangY.DoesRAGintroduceunfairness instruction-followingalignmentforretrieval-augmentedgeneration.
inLLMs? evaluatingfairnessinretrieval-augmentedgenerationsys- arXivpreprintarXiv:2410.09584,2024
tems.In:RambowO,WannerL,ApidianakiM,Al-KhalifaH,Euge- 134. Salemi A, Zamani H. Evaluating retrieval quality in retrieval-
nioBD,SchockaertS,eds,Proceedingsofthe31stInternationalCon- augmented generation. In: Proceedings of the 47th International
ferenceonComputationalLinguistics.January2025,10021–10036 ACMSIGIRConferenceonResearchandDevelopmentinInforma-
119. LiuJ,DingR,ZhangL,XieP,HuangF.Cofe-rag:Acomprehensive tionRetrieval,SIGIR’24.2024,2395–2400
full-chainevaluationframeworkforretrieval-augmentedgeneration 135. JaechA,KalaiA,LererA,RichardsonA,El-KishkyA,LowA,Hel-
withenhanceddatadiversity.arXivpreprintarXiv:2410.12248,2024 yarA,MadryA,BeutelA,CarneyA,others.Openaio1systemcard.
120. Wang S, Tan J, Dou Z, Wen J R. Omnieval: An omnidirectional arXivpreprintarXiv:2412.16720,2024
| andautomaticragevaluationbenchmarkinfinancialdomain. |     |     |     |     |     | arXiv |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
preprintarXiv:2412.13018,2024
121. YangX,SunK,XinH,SunY,BhallaN,ChenX,ChoudharyS,Gui
RD,JiangZW,JiangZ,KongL,MoranB,WangJ,XuYE,Yan
A,YangC,YuanE,ZhaH,TangN,ChenL,SchefferN,LiuY,Shah
N,WangaR,KumarA,YihWt,DongXL. Crag-comprehensive Aoran Gan is working toward the PhD
| ragbenchmark. |     | In: Globerson | A,MackeyL, | BelgraveD,Fan |     | A,  |     |           |            |     |            |     |
| ------------- | --- | ------------- | ---------- | ------------- | --- | --- | --- | --------- | ---------- | --- | ---------- | --- |
|               |     |               |            |               |     |     |     | degree in | the School | of  | Artificial | In- |
PaquetU,TomczakJ,ZhangC,eds,AdvancesinNeuralInformation telligence and Data Science, University
ProcessingSystems.2024,10470–10490
|                    |     |                |                |            |        |           |     | of Science   | and Technology |         | of   | China. |
| ------------------ | --- | -------------- | -------------- | ---------- | ------ | --------- | --- | ------------ | -------------- | ------- | ---- | ------ |
| 122. Papadimitriou | I,  | Gialampoukidis | I, Vrochidis   | S,         | others | . Rag     |     |              |                |         |      |        |
|                    |     |                |                |            |        |           |     | His research | interests      | include | text | min-   |
| playground:        | A   | framework      | for systematic | evaluation | of     | retrieval |     |              |                |         |      |        |
ing,knowledgegraphandlargelanguage
| strategies | and prompt | engineering | in rag | systems. | arXiv | preprint |     |     |     |     |     |     |
| ---------- | ---------- | ----------- | ------ | -------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
models.
arXiv:2412.12322,2024
123. KatsisY,RosenthalS,FadnisK,GunasekaraC,LeeYS,PopaL,
| ShahV,ZhuH,ContractorD,DanilevskyM. |     |     |     | Mtrag: | Amulti-turn |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
conversationalbenchmarkforevaluatingretrieval-augmentedgener-
ationsystems.arXivpreprintarXiv:2501.03468,2025
124. XuZ,LiY,DingR,WangX,ChenB,JiangY,ZhengH,LuW,Xie
|     |     |     |     |     |     |     |     | Hao Yu | is pursuing | a MS | degree | at  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ---- | ------ | --- |
P,HuangF.Letllmstakeonthelatestchallenges!achinesedynamic
|                             |     |     |                                 |     |     |     |     | McGill University |            | and is       | affiliated | with |
| --------------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | ----------------- | ---------- | ------------ | ---------- | ---- |
| questionansweringbenchmark. |     |     | In:Proceedingsofthe31stInterna- |     |     |     |     |                   |            |              |            |      |
|                             |     |     |                                 |     |     |     |     | Quebec            | Artificial | Intelligence | Institute. |      |
tionalConferenceonComputationalLinguistics.2025,10435–10448
Hisresearchfocusesonmultilingualand
| 125. GaoY,XiongY,WuW,HuangZ,LiB,WangH.                 |     |     |     |     | U-niah: | Unified |     |              |      |         |        |      |
| ------------------------------------------------------ | --- | --- | --- | --- | ------- | ------- | --- | ------------ | ---- | ------- | ------ | ---- |
|                                                        |     |     |     |     |         |         |     | low-resource | NLP, | as well | as RAG | sys- |
| ragandllmevaluationforlongcontextneedle-in-a-haystack. |     |     |     |     |         | arXiv   |     |              |      |         |        |      |
temsformisinformationdetection.
preprintarXiv:2503.00353,2025

18 Front.Comput.Sci.,2025,0(0):1–18
KaiZhangisanAssociateResearcherat Shiwei Tong is a senior data scientist at
theUniversityofScienceandTechnology Tencent Company. His research focuses
ofChina. Hisgeneralareaofresearchis onGameDataMiningandGameAppli-
natural language processing and knowl- cations driven by Large Language Mod-
| edgediscovery.HeisamemberofACM, |     |     |     | els. |     |     |     |     |
| ------------------------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
SIGIR,AAAI,andCCF.
QiLiuisaprofessorintheSchoolofAr-
| tificial Intelligence | and Data | Science | at  |     |     |     |     |     |
| --------------------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
USTC.Hisareaofresearchisdatamining
| and knowledge | discovery. | He has | pub- |     |     |     |     |     |
| ------------- | ---------- | ------ | ---- | --- | --- | --- | --- | --- |
lishedprolificallyinrefereedjournalsand
conferences.HeisanAssociateEditorof
IEEETBDandNeurocomputing.
EnhongChenisaprofessorintheSchool
|     |     |     |     | of Computer | Science | and | Technology | at  |
| --- | --- | --- | --- | ----------- | ------- | --- | ---------- | --- |
WenyuYaniscurrentlypursuingMSde-
|     |     |     |     | USTC. His | general | area | of research | in- |
| --- | --- | --- | --- | --------- | ------- | ---- | ----------- | --- |
gree in University of Science and Tech- cludes data mining and machine learn-
| nology of | China. His research | interests |     |             |         |           |     |        |
| --------- | ------------------- | --------- | --- | ----------- | ------- | --------- | --- | ------ |
|           |                     |           |     | ing, social | network | analysis, | and | recom- |
focusonconversationalsearch,retrieval-
|                          |     |     |     | mender                             | systems. | He  | was on | program |
| ------------------------ | --- | --- | --- | ---------------------------------- | -------- | --- | ------ | ------- |
| augmentedgeneration,etc. |     |     |     | committeesofnumerousconferencesin- |          |     |        |         |
cludingSIGKDD,ICDM,andSDM.
|              |              |              |     | Guoping  | Hu is    | senior | vice president | of  |
| ------------ | ------------ | ------------ | --- | -------- | -------- | ------ | -------------- | --- |
| Zhenya Huang | is currently | an Associate |     |          |          |        |                |     |
|              |              |              |     | iFLYTEK, | director | of     | the National   | Key |
ProfessorwithUSTC.Hismainresearch
|     |     |     |     | LaboratoryofCognitiveIntelligence. |     |     |     | He  |
| --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
interestsincludedatamining,knowledge
|                 |                  |             |      | has been      | honored | with       | the First | Prize of |
| --------------- | ---------------- | ----------- | ---- | ------------- | ------- | ---------- | --------- | -------- |
| reasoning,      | natural language | processing, |      |               |         |            |           |          |
|                 |                  |             |      | State Science | and     | Technology | Advance-  |          |
| and intelligent | education.       | He has      | pub- |               |         |            |           |          |
mentAwardandgarneredover300autho-
| lished more | than 50 papers | in refereed |     |     |     |     |     |     |
| ----------- | -------------- | ----------- | --- | --- | --- | --- | --- | --- |
rizedpatents.
journalsandconferenceproceedings.