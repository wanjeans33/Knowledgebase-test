MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for
|     |     |     |            | Multi-Hop | Queries    |     |     |     |     |
| --- | --- | --- | ---------- | --------- | ---------- | --- | --- | --- | --- |
|     |     |     | YixuanTang |           | and YiYang |     |     |     |     |
HongKongUniversityofScienceandTechnology
{yixuantang,imyiyang}@ust.hk
Abstract
| Retrieval-augmented |          | generation | (RAG) | aug-   |     |     |     |     |     |
| ------------------- | -------- | ---------- | ----- | ------ | --- | --- | --- | --- | --- |
| ments large         | language | models     | (LLM) | by re- |     |     |     |     |     |
trievingrelevantknowledge,showingpromis-
4202 naJ 72  ]LC.sc[  1v19351.1042:viXra
ingpotentialinmitigatingLLMhallucinations
andenhancingresponsequality,therebyfacil-
| itating the | great | adoption | of LLMs | in prac- |     |     |     |     |     |
| ----------- | ----- | -------- | ------- | -------- | --- | --- | --- | --- | --- |
tice. However,wefindthatexistingRAGsys-
| tems are | inadequate | in answering | multi-hop |     |     |     |     |     |     |
| -------- | ---------- | ------------ | --------- | --- | --- | --- | --- | --- | --- |
queries,whichrequireretrievingandreasoning
| over multiple | pieces | of supporting  | evidence. |          |          |                        |     |     |     |
| ------------- | ------ | -------------- | --------- | -------- | -------- | ---------------------- | --- | --- | --- |
|               |        |                |           |          | Figure1: | RAGwithmulti-hopquery. |     |     |     |
| Furthermore,  | to     | our knowledge, | no        | existing |          |                        |     |     |     |
RAGbenchmarkingdatasetfocusesonmulti-
| hopqueries. | Inthispaper,wedevelopanovel |     |     |     |             |               |     |                   |     |
| ----------- | --------------------------- | --- | --- | --- | ----------- | ------------- | --- | ----------------- | --- |
|             |                             |     |     |     | nAI, 2023). | One promising | use | case isRetrieval- |     |
dataset,MultiHop-RAG,whichconsistsofa
AugmentedGeneration(RAG)(Asaietal.,2023),
| knowledge    | base, | a large      | collection | of multi- |                 |            |     |                  |     |
| ------------ | ----- | ------------ | ---------- | --------- | --------------- | ---------- | --- | ---------------- | --- |
|              |       |              |            |           | which optimizes | the output | of  | a large language |     |
| hop queries, | their | ground-truth | answers,   | and       |                 |            |     |                  |     |
modelbyreferencinganexternalknowledgebase
| theassociatedsupportingevidence. |     |          | Wedetail     |         |            |                  |      |         |        |
| -------------------------------- | --- | -------- | ------------ | ------- | ---------- | ---------------- | ---- | ------- | ------ |
|                                  |     |          |              |         | outside of | the LLM training | data | sources | before |
| the procedure                    | of  | building | the dataset, | utiliz- |            |                  |      |         |        |
inganEnglishnewsarticledatasetastheun- generatingaresponse. RAGimprovesLLM’sre-
derlying RAG knowledge base. We demon- sponse(Borgeaudetal.,2022)andalsomitigates
strate the benchmarking utility of MultiHop- theoccurrenceofhallucinations,therebyenhancing
RAGintwoexperiments. Thefirstexperiment the models’ credibility (Gao et al., 2023). LLM-
comparesdifferentembeddingmodelsforre-
basedframeworks,suchasLlamaIndex(Liu,2022)
| trievingevidenceformulti-hopqueries. |     |            |     | Inthe     |               |         |                   |     |         |
| ------------------------------------ | --- | ---------- | --- | --------- | ------------- | ------- | ----------------- | --- | ------- |
|                                      |     |            |     |           | and LangChain | (Chase, | 2022), specialize |     | in sup- |
| second experiment,                   |     | we examine | the | capabili- |               |         |                   |     |         |
portingRAGpipelines.
| ties of various | state-of-the-art |     | LLMs, | includ- |     |     |     |     |     |
| --------------- | ---------------- | --- | ----- | ------- | --- | --- | --- | --- | --- |
ing GPT-4, PaLM, and Llama2-70B, in rea- Inreal-worldRetrieval-AugmentedGeneration
soningandansweringmulti-hopqueriesgiven (RAG) applications, a user’s query often necessi-
| theevidence. | Bothexperimentsrevealthatex- |     |     |     |     |     |     |     |     |
| ------------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tatesretrievingandreasoningoverevidencefrom
istingRAGmethodsperformunsatisfactorily multipledocuments,aprocessknownasmulti-hop
inretrievingandansweringmulti-hopqueries.
query. Forinstance,considerfinancialanalysisus-
WehopeMultiHop-RAGwillbeavaluablere-
|     |     |     |     |     | ingadatabaseoffinancialreports. |     |     | Afinancialana- |     |
| --- | --- | --- | --- | --- | ------------------------------- | --- | --- | -------------- | --- |
sourceforthecommunityindevelopingeffec-
lystmightquery,WhichcompanyamongGoogle,
tiveRAGsystems,therebyfacilitatinggreater
Apple,andNvidiareportedthelargestprofitmar-
| adoptionofLLMsinpractice. |     |     | TheMultiHop- |     |     |     |     |     |     |
| ------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
RAGandimplementedRAGsystemispublicly gins in their third-quarter reports for 2023? or
availableathttps://github.com/yixuantt/
|     |     |     |     |     | inquire about | a specific | company’s | performance |     |
| --- | --- | --- | --- | --- | ------------- | ---------- | --------- | ----------- | --- |
MultiHop-RAG/. over time, such as How does Apple’s sales trend
|     |     |     |     |     | look over | the past three | years? | These queries | re- |
| --- | --- | --- | --- | --- | --------- | -------------- | ------ | ------------- | --- |
1 Introduction
quireevidencefrommultipledocumentstoformu-
Theemergenceoflargelanguagemodels(LLMs), lateananswer. Duetothemultifacetednatureof
suchasChatGPT,hasfosteredawiderangeofinno- suchqueries,involvinginformationfromvarious
vations,poweringintelligentchatbotsandothernat- sources, traditional similarity matching methods
urallanguageprocessing(NLP)applications(Ope- likecosinesimilaritybetweenqueryandfinancial

| Newssource | FortuneMagazine |     |     | TheSydneyMorningHerald |     |     |     |
| ---------- | --------------- | --- | --- | ---------------------- | --- | --- | --- |
Evidence Backthen,justliketoday,homepriceshadboomed Postponements of such reports could complicate
foryearsbeforeFedofficialswereultimatelyforced thingsfortheFed,whichhasinsisteditwillmake
tohikeinterestratesaggressivelyinanattemptto upcomingdecisionsoninterestratesbasedonwhat
|     | fightinflation. |     |     | incomingdatasayabouttheeconomy. |     |     |     |
| --- | --------------- | --- | --- | ------------------------------- | --- | --- | --- |
Claim FederalReserveofficialswereforcedtoaggressively TheFederalReservehasinsistedthatitwillbaseits
hikeinterestratestocombatinflationafteryearsof upcomingdecisionsoninterestratesontheincoming
|     | boominghomeprices. |     |     | economicdata. |     |     |     |
| --- | ------------------ | --- | --- | ------------- | --- | --- | --- |
Bridge-Topic Interestratehikestocombatinflation Interestratedecisionsbasedoneconomicdata
| Bridge-Entity | FederalReserve |     |     | FederalReserve |     |     |     |
| ------------- | -------------- | --- | --- | -------------- | --- | --- | --- |
Query DoesthearticlefromFortunesuggestthattheFederalReserve’sinterestratehikesarearesponsetopast
conditions,suchasboominghomeprices,whileTheSydneyMorningHeraldarticleindicatesthatthe
FederalReserve’sfutureinterestratedecisionswillbebasedonincomingeconomicdata?
| Answer | Yes |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
Table1: Anexampleofamulti-hopquery,includingsupportingevidencefromtwonewsarticles,theparaphrased
claim,thebridge-topicandbridge-entity,andthecorrespondinganswer.
reportchunkembeddingsmightnotyieldoptimal factual sentences from each news article as evi-
results. We demonstrate this multi-hop retrieval dence. Forexample,anextractedpieceofevidence
processinFigure1. from an article may state: “Back then, just like
However, existing RAG benchmarks, such as today, home prices had boomed for years before
RGB(Chenetal.,2023)andRECALL(Liuetal., Fedofficialswereultimatelyforcedtohikeinterest
ratesaggressivelyinanattempttofightinflation.”
2023),mainlyevaluateasimplecasewherethean-
swerofaquerycanberetrievedandsolvedusing Second,weinputeachevidencepieceintoGPT-4,
onesinglepieceofevidence. Noneofthesebench- promptingittorephrasetheevidenceintoaclaim.
Thisclaimisclarifiedwithadisambiguatedtopic
marksassesstheretrievalandreasoningcapability
of LLMs for complex multi-hop queries. To ad- andentity. Forinstance,GPT-4mightrephrasethe
dressthisgapandmakeRAGbenchmarkingmore aforementioned evidence into: “Federal Reserve
officialswereforcedtoaggressivelyhikeinterest
closelyresemblereal-worldscenarios,inthispaper,
|     |     |     |     | rates to combat | inflation after | years | of booming |
| --- | --- | --- | --- | --------------- | --------------- | ----- | ---------- |
weintroduceMultiHop-RAG.Toourknowledge,
MultiHop-RAG is one of the first RAG datasets home prices”, identifying “Interest rate hikes to
focusingspecificallyonmulti-hopqueries. combat inflation” as the topic and “Federal Re-
|       |                    |          |         | serve”astheentity. | Thesetopicsandentitiesactas |     |     |
| ----- | ------------------ | -------- | ------- | ------------------ | --------------------------- | --- | --- |
| Based | on the RAG queries | commonly | encoun- |                    |                             |     |     |
bridgesforconstructingmulti-hopqueries,known
| tered in | real-world scenarios, | we first | categorize |     |     |     |     |
| -------- | --------------------- | -------- | ---------- | --- | --- | --- | --- |
multi-hopqueriesintofourtypes: Inferencequery, asbridge-topicorbridge-entity. Next,weuseGPT-
4togeneratespecificmulti-hopqueriesrelatedto
| Comparison | query, Temporal   | query,       | and Null |                          |                   |                    |          |
| ---------- | ----------------- | ------------ | -------- | ------------------------ | ----------------- | ------------------ | -------- |
|            |                   |              |          | the same bridge-topic    | or bridge-entity, |                    | accompa- |
| query. The | first three types | — Inference, | Com-     |                          |                   |                    |          |
|            |                   |              |          | niedbythecorrectanswers. |                   | Lastly,weundertake |          |
parison,andTemporal—requiretheretrievaland
analysisofevidencefrommultiplesources,encom- avalidationsteptoensurethedataquality.
passingtaskslikeinferringrelationships,compar- Wedemonstratethebenchmarkingcapabilities
ing data points, and sequencing events over time. ofMultiHop-RAGusingtwoexperiments,utilizing
| The Null | query represents | a scenario | where the |     |     |     |     |
| -------- | ---------------- | ---------- | --------- | --- | --- | --- | --- |
aRAGsystemimplementedwithLlamaIndex(Liu,
querycannotbederivedfromtheknowledgebase. 2022). Thefirstexperimentinvolvesacomparison
This category is crucial for assessing whether an ofdifferentembeddingmodelsforretrievingrele-
LLMmighthallucinateananswertoamulti-hop
|     |     |     |     | vantevidenceformulti-hopqueries. |     |     | Inthesecond |
| --- | --- | --- | --- | -------------------------------- | --- | --- | ----------- |
querywhentheretrievedtextlacksrelevance.
experiment,weassessthereasoningandanswering
WeconstructourRAGknowledgebaseusinga abilitiesofvariousstate-of-the-artLLMs,including
collectionofnewsarticles. UsingGPT-4asadata GPT-4, GPT-3.5, PaLM, Claude-2, Llama2-70B,
generator,wethentakeanextensiveprocedureto andMixtral-8x7B,formulti-hopquerieswhenre-
constructadiversesetofmulti-hopqueries,each trievedtextisprovided. Theresultsfrombothex-
requiringtheretrievalandreasoningovermultiple perimentsindicatethatthecurrentRAGimplemen-
documents. Anexampleofqueryconstructionis tationsareinadequateforeffectivelyretrievingand
shown in Table 1. First, we begin by extracting answeringmulti-hopqueries. Wepubliclyrelease

thischallengingMultiHop-RAGdatasetandhopeit be: Whichreportdiscussesthesupplychainriskof
willbeavaluableresourceforthecommunityinde- Apple,the2019annualreportorthe2020annual
| velopingandbenchmarkingRAGsystems,thereby |     |     |     |     |     | report? |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
unleashingthegreatpotentialofgenerativeAIin Comparison query: For such a query q, the an-
practice.
swerrequiresacomparisonofevidencewithinthe
|     |     |     |     |     |     | retrievalsetR | q . Forinstance,acomparisonquery |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | -------------------------------- | --- | --- | --- | --- |
2 RAGwithmulti-Hopqueries
|     |     |     |     |     |     | might ask: | Did Netflix | or  | Google | report | higher |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------ | ------ | ------ |
revenuefortheyear2023?"
2.1 Retrieval-augmentedGeneration(RAG)
|     |     |     |     |     |     | Temporalquery: | Forsuchaqueryq,theanswer |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------------ | --- | --- | --- | --- |
InanRAGapplication,weutilizeanexternalcor-
|     |     |     |     |     |     | requires | an analysis | of the | temporal | information |     |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | -------- | ----------- | --- |
pus,denotedasD,whichcomprisesmultipledocu-
|                                      |     |     |     |          |        | oftheretrievedchunks. |          | Forexample, |           | atemporal |        |
| ------------------------------------ | --- | --- | --- | -------- | ------ | --------------------- | -------- | ----------- | --------- | --------- | ------ |
| mentsandservesastheknowledgebase.    |     |     |     | Eachdoc- |        |                       |          |             |           |           |        |
|                                      |     |     |     |          |        | query may             | ask: Did | Apple       | introduce | the       | AirTag |
| umentwithinthiscorpus,representedasd |     |     |     |          | ∈ D,is |                       |          |             |           |           |        |
i
trackingdevicebeforeorafterthelaunchofthe5th
| segmentedinto |     | asetofchunks.Thesechunks |     |     | are |     |     |     |     |     |     |
| ------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
generationiPadPro?
thentransformedintovectorrepresentationsusing
|     |     |     |     |     |     | Nullquery: | Forsuchasqueryq,theanswercannot |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------------------------- | --- | --- | --- | --- |
anembeddingmodelandstoredinanembedding
database. Given a user query q, the system typi- bederivedfromtheretrievedsetR . Weinclude
q
callyretrievesthetop-Kchunksthatbestmatchthe thenullquerytoassessthegenerationquality,es-
|              |        |            |     |               |     | peciallyregardingtheissueofhallucination. |     |     |     |     | Fora |
| ------------ | ------ | ---------- | --- | ------------- | --- | ----------------------------------------- | --- | --- | --- | --- | ---- |
| query. These | chunks | constitute |     | the retrieval | set |                                           |     |     |     |     |      |
forqueryq,representedasR = {r ,r ,...,r }. nullquery,eventhougharetrievedsetisprovided,
|     |     |     | q   | 1 2 | K   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The retrieved chunks, combined with the query an LLM should produce a null response instead
|     |     |     |     |     |     | of hallucinating | an  | answer. | For example, |     | assum- |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------------ | --- | ------ |
andanoptionalprompt,arethenfedintoanLLM
ingABCDisanon-existentcompany,anullquery
| to generate | a final | answer, | following | the | format: |     |     |     |     |     |     |
| ----------- | ------- | ------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
LLM(q,R ,prompt) → answer. mightask: WhatarethesalesofcompanyABCD
q
asreportedinits2022and2023annualreports?
2.2 Multi-HopQuery
We define a multi-hop query as one that requires 2.3 EvaluationMetrics
| retrieving | and reasoning |     | over multiple | pieces | of  |     |     |     |     |     |     |
| ---------- | ------------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
AnRAGsystemhandlingmulti-hopqueriescanbe
| supportingevidencetoprovideananswer. |     |     |     |     | Inother |                            |     |     |                     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | ------------------- | --- | --- |
|                                      |     |     |     |     |         | assessedfromtwokeyaspects: |     |     | retrievalevaluation |     |     |
words,foramulti-hopqueryq,thechunksinthe
retrieval set R collectively provide an answer andgenerationevaluation.
q
to q. For example, the query "Which company RetrievalEvaluation: Evidently,thequalityof
R
among Google, Apple, and Nvidia reported the the retrieval set q determines the final genera-
|     |     |     |     |     |     | tion quality. | We compare |     | the retrieved |     | set with |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ------------- | --- | -------- |
largestprofitmarginsintheirthird-quarterreports
for2023?"requires1)retrievingrelevantpiecesof the ground truth evidence associated with each
evidencerelatedtoprofitmarginsfromthereports query, except for the null queries, as they have
|     |     |     |     |     |     | no evidence | to derive | from. | Assuming |     | the top- |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ----- | -------- | --- | -------- |
ofthethreecompanies;2)generatingananswerby
comparingandreasoningfromthemultiplepieces K chunks are retrieved, i.e., |R | = K, we use
q
of retrieved evidence. This differs from a single- retrievalevaluationmetricsincludingMeanAver-
|     |     |     |     |     |     | age Precision | at K | (MAP@K), | Mean | Reciprocal |     |
| --- | --- | --- | --- | --- | --- | ------------- | ---- | -------- | ---- | ---------- | --- |
hopquerysuchas"WhatisGoogle’sprofitmargin
RankatK(MRR@K),andHitRateatK(Hit@K).
| in the third-quarter |     | reports | for 2023," | where | the |     |     |     |     |     |     |
| -------------------- | --- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
answercanbedirectlyderivedfromasinglepiece MAP@K measurestheaveragetop-Kretrievalpre-
| ofevidence. |     |     |     |     |     | cision across | all queries. | MRR@K |     | calculates | the |
| ----------- | --- | --- | --- | --- | --- | ------------- | ------------ | ----- | --- | ---------- | --- |
averageofthereciprocalranksofthefirstrelevant
| Based | on the | queries | commonly | used | in real- |     |     |     |     |     |     |
| ----- | ------ | ------- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- |
world RAG systems, we identify four types of chunk for each query, considering the top-K re-
multi-hop queries. For each type, we present a trievedset. Hit@K metricmeasuresthefractionof
evidencethatappearsinthetop-Kretrievedset.
hypotheticalquerywithinthecontextofafinancial
RAGsystem,wheretheknowledgebaseconsists Response Evaluation: Since the multi-hop
ofacollectionofannualreports. query requires reasoning over multiple pieces of
Inferencequery: Forsuchaqueryq,theanswer retrievedchunks,wecanalsoevaluatethereason-
is deduced through reasoning from the retrieval ingcapabilityoftheLLMbycomparingtheLLM
set R . An example of an inference query might responsewiththegroundtruthanswerofthequery.
q

newsarticleispairedwithmetadata,includingthe
title,publishdate,author,category,URL,andnews
source.
|     |     |     |     |     | Step2: | EvidenceExtraction. |     | Foreacharticle,we |     |     |
| --- | --- | --- | --- | --- | ------ | ------------------- | --- | ----------------- | --- | --- |
extractfactualoropinionsentencesusingatrained
|     |     |     |     |     | languagemodel2. |     | Thesefactualsentencesarelater |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | ----------------------------- | --- | --- | --- |
usedasevidenceforansweringmulti-hopqueries.
|     |     |     |     |     | We retain | only | those | news articles | containing | ev- |
| --- | --- | --- | --- | --- | --------- | ---- | ----- | ------------- | ---------- | --- |
idencethatmayhaveoverlappingkeywordswith
|     |     |     |     |     | othernewsarticles. |         | Thisallowsustolatercreate |              |           |     |
| --- | --- | --- | --- | --- | ------------------ | ------- | ------------------------- | ------------ | --------- | --- |
|     |     |     |     |     | multi-hop          | queries | where                     | the answer’s | evidences |     |
aredrawnfrommultiplesources.
Step3: Claim,Bridge-Entity,Bridge-TopicGen-
eration. OurgoalistouseGPT-4toautomatically
generatehigh-qualitymulti-hopqueriesusingthe
|     |     |     |     |     | evidenceset. | However,therawevidenceobtained |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | ------------------------------ | --- | --- | --- | --- |
fromStep2isnotidealforquerygenerationdue
|     |     |     |     |     | toinconsistencyinlinguisticstructure. |     |     |     | Forexam- |     |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | -------- | --- |
ple,somepiecesofevidenceusepronounstorefer
|          |                                   |     |     |     | to subjects   | and   | lack      | the actual entity | in the        | text. |
| -------- | --------------------------------- | --- | --- | --- | ------------- | ----- | --------- | ----------------- | ------------- | ----- |
| Figure2: | MultiHop-RAGConstructionPipeline. |     |     |     |               |       |           |                   |               |       |
|          |                                   |     |     |     | To address    | this, | we employ | GPT-4             | to paraphrase |       |
|          |                                   |     |     |     | the evidence, | which |           | we refer to as    | claims,       | given |
3 ABenchmarkingDataset:
|              |     |     |     |     | the original | evidence |     | and its context. | To        | ensure |
| ------------ | --- | --- | --- | --- | ------------ | -------- | --- | ---------------- | --------- | ------ |
| MultiHop-RAG |     |     |     |     | consistency  | between  |     | the generated    | claim and | the    |
evidence,wefurtherperformfact-checkingusing
| In this section, | we  | provide | detailed | information |     |     |     |     |     |     |
| ---------------- | --- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- |
theUniEval(Zhongetal.,2022)frameworktover-
ontheconstructionoftheMultiHop-RAGdataset.
ifythealignmentbetweentheevidenceandclaim.
Specifically,wedescribetheprocessofcreatinga
|     |     |     |     |     | Appendix | A presents |     | the prompt used | for | GPT-4 |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | --------------- | --- | ----- |
setofmulti-hopqueries,alongwiththecorrespond-
forclaimgeneration.
inggroundtruthevidencesetsandanswersderived
|     |     |     |     |     | Bridge-EntityandBridge-Topic: |     |     |     | Theshareden- |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ------------ | --- |
fromacollectionofnewsarticles.
tityortopicacrosspiecesofevidenceisreferredto
3.1 MultiHop-RAGConstruction asthebridge-entityorbridge-topic. Thesebridge-
|        |                    |     |                 |     | entities | or bridge-topics |     | can be used | to link | dif- |
| ------ | ------------------ | --- | --------------- | --- | -------- | ---------------- | --- | ----------- | ------- | ---- |
| Step1: | DatasetCollection. |     | Wedownloadanews |     |          |                  |     |             |         |      |
datasetusingthemediastackAPI1,aRESTAPIin- ferentpiecesofevidencefromwhichamulti-hop
terfacedeliveringworldwidenewsdata. Thenews query’sanswerisderived. Forexample,inaclaim
suchas“Googlereportsitsthird-quarterresultsfor
| data source | comprises | various | English-language |     |     |     |     |     |     |     |
| ----------- | --------- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
2023,showcasingadetailedoverviewofitsfinan-
| websitescoveringarangeofnewscategories: |     |     |     | en- |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tertainment, business, sports, technology, health, cialperformance,includingrevenuegrowth,profit
margins”,thetermprofitmargincanbeviewedas
| andscience. | Tomimicreal-worldRAGscenarios, |     |     |     |     |     |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
abridge-topicandthetermGooglecanbeviewed
| where the | knowledge | base | data, such | as an enter- |     |     |     |     |     |     |
| --------- | --------- | ---- | ---------- | ------------ | --- | --- | --- | --- | --- | --- |
prise’s internal data, may differ from the LLMs’ asabridge-entitythatlinksthedifferentpiecesof
|          |          |        |               |           | evidence.                          | WepromptGPT-4toidentifythebridge- |     |     |           |     |
| -------- | -------- | ------ | ------------- | --------- | ---------------------------------- | --------------------------------- | --- | --- | --------- | --- |
| training | data, we | select | news articles | published |                                    |                                   |     |     |           |     |
|          |          |        |               |           | entityandbridge-topicforeachclaim. |                                   |     |     | AppendixA |     |
fromSeptember26,2023,toDecember26,2023.
alsopresentsthepromptusedforGPT-4forbridge
Thistimeframeextendsbeyondtheknowledgecut-
| off of some | widely-used |     | LLMs, | including Chat- | generation. |     |     |     |     |     |
| ----------- | ----------- | --- | ----- | --------------- | ----------- | --- | --- | --- | --- | --- |
GPTandLLaMA,asofthetimeofwriting. This Step4: QueryandAnswerGeneration. Inthis
step,weleveragethebridge-entityorbridge-topic
| selection | also helps | in teasing | out | the possibility |     |     |     |     |     |     |
| --------- | ---------- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
of the underlying LLM having been exposed to togeneratemulti-hopqueries. Specifically,wefirst
these news articles. We only keep articles with a grouptheclaimshavingthesamebridge-entityor
| tokenlengthgreaterthanorequalto1,024. |     |     |     | Every |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
2https://huggingface.co/lighteternal/fact-or-opinion-xlmr-
| 1https://mediastack.com/ |     |     |     |     | el  |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

bridge-topicintoaclaimset. Werestricttheclaim Category Avg. Tokens EntryCount
settohaveatleasttwoclaimsbutnomorethanfour technology 2262.3 172
claims. Foreachtypeofquery,wefeedtheclaim entertainment 2084.3 114
set to GPT-4 and prompt itwith an instruction to sports 2030.6 211
generateaquerywithinformationfromeachclaim. science 1745.5 21
Below,weexplainthespecificationsfordifferent business 1723.8 81
multi-hopquerytypes. Intheconstructionofeach
health 1481.1 10
query,wealsoincludethesourceofthenewsarticle
total 2046.5 609
where the supporting evidence is associated with
to mimic real-world RAG scenarios. Appendix Table2: Descriptivestatisticsofthenewsarticleknowl-
ApresentsthepromptsusedforGPT-4forquery edgebaseinMultiHop-RAG.
generation.
QueryCategory EntryCount Percentage
InferenceQuery: Thesequeriesareformulated
InferenceQuery 816 31.92%
bysynthesizingthevariouscharacterizationsofthe
ComparisonQuery 856 33.49%
bridge-entityacrossmultipleclaims,withthefinal
TemporalQuery 583 22.81%
answerbeingtheidentificationoftheentityitself.
NullQuery 301 11.78%
Comparison Query: These queries are struc-
Total 2,556 100.00%
tured to compare the similarities and differences
relatedtothebridgeentityortopic. Theresultant Table3: ThedistributionofquerytypesinMultiHop-
answertosuchqueriesistypicallyadefinitive“yes” RAG.
or“no”,basedonthecomparison.
Temporal Query: These queries explore the
3.2 DescriptiveStatistics
temporalorderingofeventsacrossdifferentpoints
intime. Theanswertosuchqueriesistypicallya TheMultiHop-RAGdatasetcontainssixdifferent
“yes”or“no”orasingletemporalindicatorword typesofnewsarticles,covering609distinctnews,
like“before”or“after”. withanaverageof2,046tokens. Thedistributionof
thenewscategoriesisshowninTable2. MultiHop-
Null Query: Null query is a query whose an-
RAGcontainsfourtypesofmulti-hopqueriesand
swercannotbederivedfromtheretrievedset. To
thedistributionofthesequeriesisshowninTable
createnullqueries,wegeneratemulti-hopqueries
3. Intotal,about88%ofqueriesinthedatasetare
usingentitiesthatdonotexistintheexistingbridge-
non-null queries where answers can be retrieved
entities. To add complexity, we also include fic-
andreasonedfromtheknowledgebase. Inaddition,
tional news source metadata when formulating
theformofqueriesexhibitsconsiderablediversity.
thesequestions,ensuringthatthequestionsdonot
Approximately27%ofinterrogativequeriesstart
reference any contextually relevant content from
with "does," around 15% initiate with "what," a
theknowledgebase. Theanswertothenullquery
similar proportion start "which," and 14% begin
shouldbe“insufficientinformation”orsimilar.
with "who," with the remainder incorporating a
Step5: QualityAssurance. Finally,weusetwo
smallpercentageofotherinterrogativewordssuch
approachestoreassurethedatasetquality. First,we
as"when."Moreover,thenumberofevidencere-
manuallyreviewasubsetsampleofthegenerated
quiredtoansweramulti-hopqueryvaries. Table
multi-hop queries, their corresponding evidence
4 shows the distribution of evidence numbers for
sets,andthefinalanswers. Theresultsoftheman-
eachqueryinthedataset. Around42%ofqueries
ualexaminationindicateahighdegreeofaccuracy
can be answered using two pieces of evidence,
anddata quality. Second, weutilize GPT-4toas-
whileapproximately30%and15%ofqueriescan
sesseachexampleinthedatasetagainstthefollow-
beansweredusingthreeorfourpiecesofevidence,
ing criteria: 1) The generated query must utilize
respectively.
allprovidedevidenceinformulatingtheresponse;
2) The query should be answerable solely based
4 BenchmarkingRAGsystemusing
ontheprovidedevidence; 3)Theresponsetothe
MultiHop-RAG
generatedqueryshouldbeeitherasinglewordor
aspecificentity;4)Thequerymustconformtoits MultiHop-RAGcanbeusedasabenchmarkforvar-
designatedquerytype. iousRAG-relatedtasks. Broadlyspeaking,RAG-

| Num. | ofEvidenceNeeded |     | Count | Percentage |     |     |     |     |     |     |     |     |
| ---- | ---------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
beddingmodel,wefurtherselectthetop-Kchunks
|     | 0(NullQuery) |     |     | 301  | 11.78% | usingtheReranker. |         |           |           |         |         |           |
| --- | ------------ | --- | --- | ---- | ------ | ----------------- | ------- | --------- | --------- | ------- | ------- | --------- |
|     |              | 2   |     | 1078 | 42.18% | Experiment        | Result: |           | Table     | 5 shows | the     | retrieval |
|     |              | 3   |     | 779  | 30.48% |                   |         |           |           |         |         |           |
|     |              |     |     |      |        | result of         | using   | different | embedding |         | models. | It        |
|     |              | 4   |     | 398  | 15.56% |                   |         |           |           |         |         |           |
showsthatthereisstillasignificantgapinretriev-
|     |     | Total | 2,556 |     | 100.00% |              |          |     |     |               |     |          |
| --- | --- | ----- | ----- | --- | ------- | ------------ | -------- | --- | --- | ------------- | --- | -------- |
|     |     |       |       |     |         | ing relevant | evidence |     | for | the multi-hop |     | queries. |
WhileRerankcaneffectivelyimproveretrievalrel-
| Table | 4:  | The distribution | of the | number | of evidence |     |     |     |     |     |     |     |
| ----- | --- | ---------------- | ------ | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
requiredtoanswermulti-hopqueriesinMultiHop-RAG. evance,thehighestHits@10isonly0.7467when
|     |     |     |     |     |     | theRerankertechniqueisused.            |     |     |     | Moreover,thedrop |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | ---------------- | --- | --- |
|     |     |     |     |     |     | inthehighestHits@4to0.6625isworrisome. |     |     |     |                  |     | In  |
relatedtaskscanbecategorizedasretrieval-related
|       |     |                    |     |        |              | practical | RAG       | systems, | the | underlying |              | LLM of- |
| ----- | --- | ------------------ | --- | ------ | ------------ | --------- | --------- | -------- | --- | ---------- | ------------ | ------- |
| tasks | and | generation-related |     | tasks. | A retrieval- |           |           |          |     |            |              |         |
|       |     |                    |     |        |              | ten has   | a context | window   |     | limit.     | As a result, | the     |
relatedtaskfocusesonretrievingrelevanttextfrom numberofretrievedchunksisusuallyrestrictedto
theknowledgebase,whileageneration-relatedtask a small number. The low values of the retrieval
focusesongeneratinghigh-qualityresponsesgiven
metricshighlightthechallengesinretrievingrele-
| theretrievedtext. |     | Inthissection,weshowcasetwo |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vantpiecesofevidenceformulti-hopquerieswhen
usecasesforeachtaskwhereMultiHop-RAGcan usingdirectsimilaritymatchingbetweenthemulti-
beemployed.
hopqueryandtextchunks.
4.1 Retrieval-relatedTask
4.2 Generation-relatedTask
AnimportantdesignchoiceinanRAGsystemis
|                                  |       |          |           |           |          | The underlying |           | LLMs | play   | a crucial | role | in gen-  |
| -------------------------------- | ----- | -------- | --------- | --------- | -------- | -------------- | --------- | ---- | ------ | --------- | ---- | -------- |
| theselectionoftheembeddingmodel. |       |          |           |           | Anembed- |                |           |      |        |           |      |          |
|                                  |       |          |           |           |          | erating        | responses | in   | an RAG | system.   | In   | this ex- |
| ding                             | model | converts | data into | numerical | vectors  |                |           |      |        |           |      |          |
periment,weevaluatethequalityofgeneratedre-
andsubsequentlystoresthesevectorsinembedding
|            |     |                   |     |                   |     | sponses  | under     | two | different           | settings. | In  | the first |
| ---------- | --- | ----------------- | --- | ----------------- | --- | -------- | --------- | --- | ------------------- | --------- | --- | --------- |
| databases. |     | Inthisexperiment, |     | weevaluatediffer- |     |          |           |     |                     |           |     |           |
|            |     |                   |     |                   |     | setting, | we employ |     | the best-performing |           |     | retrieval |
entembeddingmodelsbyexaminingtheirretrieval
model,namelyvoyage-02withbge-reranker-large,
quality.
asindicatedinTable5,toretrievethetop-Ktexts
| Experiment |     | Setup: | We implement | an  | RAG sys- |          |      |      |          |      |        |        |
| ---------- | --- | ------ | ------------ | --- | -------- | -------- | ---- | ---- | -------- | ---- | ------ | ------ |
|            |     |        |              |     |          | and then | feed | them | into the | LLM. | In the | second |
temusingtheLlamaIndexframework(Liu,2022).
|     |     |     |     |     |     | setting, | we use | the | ground-truth |     | evidence | associ- |
| --- | --- | --- | --- | --- | --- | -------- | ------ | --- | ------------ | --- | -------- | ------- |
WepartitionthedocumentsintheMultiHop-RAG
|     |     |     |     |     |     | ated with | each | query | as the | retrieved | text | for the |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ----- | ------ | --------- | ---- | ------- |
knowledgebaseintochunks,eachconsistingof256
LLM.Thissettingrepresentsaceilingperformance
tokens. Wethenconvertthechunksusinganem-
|     |     |     |     |     |     | for testing | the | LLM’s | response | capabilities, |     | as it |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | -------- | ------------- | --- | ----- |
beddingmodelandsavetheembeddingsintoavec-
utilizestheactualevidences.
| tordatabase. |     | Similarly,intheretrievalstep,wecon- |     |     |     |            |        |     |        |       |             |     |
| ------------ | --- | ----------------------------------- | --- | --- | --- | ---------- | ------ | --- | ------ | ----- | ----------- | --- |
|              |     |                                     |     |     |     | Experiment | Setup: |     | In the | first | experiment, | we  |
vertaqueryusingthesameembeddingmodeland
retrievetop-6chunkssothatthetotallengthofthe
retrievethetop-Kmostrelevantchunksthathave
|     |     |     |     |     |     | retrieved | text | does not | exceed | 2,048. | All | queries |
| --- | --- | --- | --- | --- | --- | --------- | ---- | -------- | ------ | ------ | --- | ------- |
thehighestcosinesimilaritywiththequeryembed-
|     |     |     |     |     |     | in MultiHop-RAG |     |     | are tested | in  | the experiment. |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ---------- | --- | --------------- | --- |
ding. Inthisexperiment,wetestavarietysetofem-
|     |     |     |     |     |     | In the second |     | experiment, |     | since | the null | queries |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ----- | -------- | ------- |
beddingmodels,includingtheada-embeddingsby
|     |     |     |     |     |     | donothaveassociatedevidence, |     |     |     |     | weexcludethis |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | ------------- | --- |
OpenAI(text-embedding-ada-002,text-search-ada-
|     |     |     |     |     |     | type of | query | in the | experiment. |     | For the | LLMs |
| --- | --- | --- | --- | --- | --- | ------- | ----- | ------ | ----------- | --- | ------- | ---- |
3,
| query-001), |     | voyage-02 | llm-embedder |     | (Zhang |         |                 |     |     |          |               |     |
| ----------- | --- | --------- | ------------ | --- | ------ | ------- | --------------- | --- | --- | -------- | ------------- | --- |
|             |     |           |              |     |        | used in | the experiment, |     | we  | consider | state-of-the- |     |
etal.,2023),bge-large-en-v1.5(Xiaoetal.,2023),
artcommercialmodels,includingGPT-4(OpenAI,
jina-embeddings-v2-base-en(Güntheretal.,2023),
2023),GPT-3.5,Claude-2(Anthropic,2023),and
e5-base-v2(Wangetal.,2022),andinstructor-large
|     |         |             |         |     |             | Google-PaLM(Google,2023). |          |     |        | Weobtainanswers |     |         |
| --- | ------- | ----------- | ------- | --- | ----------- | ------------------------- | -------- | --- | ------ | --------------- | --- | ------- |
| (Su | et al., | 2023). NULL | queries | are | excluded in |                           |          |     |        |                 |     |         |
|     |         |             |         |     |             | using the                 | provided |     | API of | the respective  |     | models. |
thisexperimentbecausethereisnomatchingevi-
Wealsoassesssomeopen-sourcemodels,includ-
| dencetothequery. |     | Additionally,wealsoinclude |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ingMixtral-8x7b-instruct(Jiangetal.,2024)and
aRerankermoduletoexaminetheretrievalperfor-
Llama-2-70b-chat-hf(Touvronetal.,2023).
mance,usingbge-reranker-large(Xiaoetal.,2023).
|       |            |     |                |       |         | ExperimentResults: |              |     | Table6showstheresponse |        |     |         |
| ----- | ---------- | --- | -------------- | ----- | ------- | ------------------ | ------------ | --- | ---------------------- | ------ | --- | ------- |
| After | retrieving | 20  | related chunks | using | the em- |                    |              |     |                        |        |     |         |
|       |            |     |                |       |         | accuracy           | of different |     | LLMs.                  | First, | we  | can see |
thattheresponseaccuracyrateusingtheretrieved
3https://www.voyageai.com/

|     |     |     |     | WithoutReranker |     | Withbge-reranker-large |     |
| --- | --- | --- | --- | --------------- | --- | ---------------------- | --- |
Embedding
|     |     |     | MRR@10 | MAP@10 | Hits@10 Hits@4 | MRR@10 MAP@10 | Hits@10 Hits@4 |
| --- | --- | --- | ------ | ------ | -------------- | ------------- | -------------- |
text-embedding-ada-002 0.4203 0.3431 0.6381 0.504 0.5477 0.4625 0.7059 0.6169
text-search-ada-query-001 0.4203 0.3431 0.6399 0.5031 0.5483 0.4625 0.7064 0.6174
llm-embedder 0.2558 0.1725 0.4499 0.3189 0.425 0.3059 0.5478 0.4756
bge-large-en-v1.5 0.4298 0.3423 0.6718 0.5221 0.563 0.4759 0.7183 0.6364
jina-embeddings-v2-base-en 0.0621 0.031 0.1479 0.0802 0.1412 0.0772 0.1909 0.1639
intfloat/e5-base-v2 0.1843 0.1161 0.3556 0.2334 0.3237 0.2165 0.4176 0.3716
voyage-02 0.3934 0.3143 0.6506 0.4619 0.586 0.4795 0.7467 0.6625
hkunlp/instructor-large 0.3458 0.265 0.5717 0.4229 0.5115 0.4118 0.659 0.5775
|     |     |     | Table5: Retrievalperformanceofdifferentembeddingmodels. |     |     |     |     |
| --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- |
Accuracy
Models
|                       |        | RetrievedChunk            |      | Ground-truthChunk |     |     |     |
| --------------------- | ------ | ------------------------- | ---- | ----------------- | --- | --- | --- |
| GPT-4                 |        |                           | 0.56 | 0.89              |     |     |     |
| ChatGPT               |        |                           | 0.44 | 0.57              |     |     |     |
| Llama-2-70b-chat-hf   |        |                           | 0.28 | 0.32              |     |     |     |
| Mixtral-8x7B-Instruct |        |                           | 0.32 | 0.36              |     |     |     |
| Claude-2.1            |        |                           | 0.52 | 0.56              |     |     |     |
| Google-PaLM           |        |                           | 0.47 | 0.74              |     |     |     |
| Table6:               |        | GenerationaccuracyofLLMs. |      |                   |     |     |     |
| chunks                | is not | satisfactory,             | with | the state-of-the- |     |     |     |
| art GPT-4             | model  | achieving                 | only | 0.56 accuracy.    |     |     |     |
Thisisexpected,becausetheretrievalcomponent
fallsshortinretrievingrelevantevidencesfromthe
| knowledge | base. | Second, | even | when we provide |     |     |     |
| --------- | ----- | ------- | ---- | --------------- | --- | --- | --- |
theLLMwiththeground-truthevidences,wecan Figure3: Generationaccuracyfordifferentquerytypes.
seethattheresponseaccuracyisfarfrombeingper-
fect. OpensourceLLMsuchasLlama02-70Band
thechronologicalorderofevents,whichiscrucial
Mixtral-8x7Bonlyachieveanaccuracyof0.32and foransweringtemporalquerieswheretimingisa
| 0.36 respectively. |     | GPT-4 | achieves | strong | reason-    |                                    |     |
| ------------------ | --- | ----- | -------- | ------ | ---------- | ---------------------------------- | --- |
|                    |     |       |          |        | keyfactor. | Takentogether,thisexperimentdemon- |     |
ingcapabilitywithanaccuracyof0.89,followed
stratesthatthereisstillroomforimprovementin
bythesecond-basedLLMGoogle-PaLMwithan
|     |     |     |     |     | the reasoning | capabilities | of LLMs, particularly |
| --- | --- | --- | --- | --- | ------------- | ------------ | --------------------- |
accuracyof0.74.
thosethatareopen-source,formulti-hopqueries.
Figure3showsthedetailedresultsofdifferent
|     |     |     |     |     | 4.3 OtherUseCases |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --- |
querytypesforGPT-4andMixtral-8x7B-instruct.
Both models show relatively high robustness on BeyondembeddingmodelsandLLMgeneration,
null queries, meaning they are generally good at there are other areas worth exploring. For exam-
determining when a query cannot be answered ple,querydecompositionisawidelyutilizedtech-
basedontheretrievedtext. Thisisencouragingbe- nique in RAG frameworks, such as LLamaIndex.
causeonebenefitofRAGistomitigatingtheLLM This process involves breaking down the query
hallucination issue by augmenting LLM with re- intosmallersegments;ittargetsasingledocument
trievalknowledge. However,Mixtral-8x7Bmodel forretrievalandintegratestheinformationsubse-
performs significantly worse than the GPT-4 in quently,therebypotentiallyenhancingretrievalac-
comparisonandtemporalqueries. Uponreviewing curacy. Anotheradvancedandpromisingapproach
theincorrectresponses,wefindthatMixtral-8x7B involves building LLM-based agents that can au-
failstoaccuratelyhandlelogicalnegation,leading tomatically plan and execute multi-hop queries,
to misinterpretation of statements and thus a low suchasAutoGPT(Gravitas,2023). Anotherarea
performance in the comparison queries. In addi- ofinterestisthehybridretrievalapproach,which
tion,Mixtral-8x7Boftenfailstocorrectlyidentify combineskeywordandembeddingmatchingtech-

niques. We believe that there are many potential largeknowledgebase. Separately,(Kamallooetal.,
areasforenhancingRAG’sperformanceonmulti- 2023)evaluatesarangeofcommercialembedding
hop queries, and the curated dataset MultiHop- APIsforinformationretrieval,butthisevaluation
RAGcanbeavaluableresourcetothecommunity. isnotcontextualizedwithintheframeworkofRAG
systemseither.
| 5 RelatedWork |     |     |     |     |     |     | Multi-document |     | QA  | datasets: |     | Question- |     |
| ------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --------- | --- | --------- | --- |
answering(QA)isafundamentaltaskinNLP,and
| RAGEvaluation: |     | AsRAGsystemsgainincreas- |     |     |     |     |         |         |             |     |      |             |     |
| -------------- | --- | ------------------------ | --- | --- | --- | --- | ------- | ------- | ----------- | --- | ---- | ----------- | --- |
|                |     |                          |     |     |     |     | several | popular | benchmarks, |     | such | as HotpotQA |     |
ing popularity, a variety of RAG benchmarking (Yang et al., 2018), MultiRC (Khashabi et al.,
datasetsandevaluationtoolshavebeendeveloped.
|               |     |           |     |            |     |     | 2018), | and 2WikiMultiHopQA |     |      | (Ho      | et al., | 2020), |
| ------------- | --- | --------- | --- | ---------- | --- | --- | ------ | ------------------- | --- | ---- | -------- | ------- | ------ |
| For instance, |     | RGB (Chen | et  | al., 2023) | and | RE- |        |                     |     |      |          |         |        |
|               |     |           |     |            |     |     | aim to | achieve             | QA  | from | multiple | sources | of     |
CALL(Liuetal.,2023)evaluatetheperformance
|     |     |     |     |     |     |     | documents. | This | task | is similar | to  | our multi-hop |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---- | ---------- | --- | ------------- | --- |
ofLLMsingeneratingresponsesforRAGsystems query RAG task, as both involve reasoning from
underconditionsinvolvingnoisy,integrative,and
|                        |     |     |                          |     |     |     | multiple | sources   | of information. |     | However,  |     | these   |
| ---------------------- | --- | --- | ------------------------ | --- | --- | --- | -------- | --------- | --------------- | --- | --------- | --- | ------- |
| counterfactualqueries. |     |     | However,bothdatasetspri- |     |     |     |          |           |                 |     |           |     |         |
|                        |     |     |                          |     |     |     | datasets | primarily | focus           | on  | assessing | a   | model’s |
marily focus on evaluating the generation aspect reasoning skills, and they do not emphasize the
| of RAG          | systems | without   | specifically |     | addressing |     |           |     |          |      |             |     |       |
| --------------- | ------- | --------- | ------------ | --- | ---------- | --- | --------- | --- | -------- | ---- | ----------- | --- | ----- |
|                 |         |           |              |     |            |     | retrieval | of  | evidence | from | a knowledge |     | base. |
| their retrieval |         | accuracy. | In addition, |     | recent     | ad- |           |     |          |      |             |     |       |
Additionally,theirprimarydatasourcesWikipedia,
vancements have been made in automated RAG significantly overlap with the training data of
evaluationtools,suchasARES(Saad-Falconetal., most existing LLMs. If we use these sources for
| 2023) and | RAGAS | (Es | et al., | 2023). | These | tools |              |     |     |          |       |      |           |
| --------- | ----- | --- | ------- | ------ | ----- | ----- | ------------ | --- | --- | -------- | ----- | ---- | --------- |
|           |       |     |         |        |       |       | benchmarking |     | RAG | systems, | there | is a | potential |
utilizeLLMstoautomaticallyassessthequalityof
concernthatLLMresponsesmightrelyontraining
RAGgeneration,yettheydonotintroducebench- knowledgeratherthanreasoningfromtheretrieved
| markingdatasets. |     | Ourworkintroducesoneofthe |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
knowledgebase.
firstRAGbenchmarkingdatasets,consistingofa
| knowledge | base, | a large | collection | of  | multi-hop |     | 6 Conclusion |     |     |     |     |     |     |
| --------- | ----- | ------- | ---------- | --- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
queries,theirground-truthanswers,andtheassoci-
Inthiswork,weintroduceMultiHop-RAG,anovel
atedsupportingevidence,therebycomplementing
|     |     |     |     |     |     |     | and unique | dataset | designed |     | for | queries | that re- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | --- | --- | ------- | -------- |
existingRAGevaluations.
quireretrievalandreasoningfrommultiplepieces
| Retrieval    | datasets: |              | Apart from | the | context | of      |                       |     |     |                       |     |     |     |
| ------------ | --------- | ------------ | ---------- | --- | ------- | ------- | --------------------- | --- | --- | --------------------- | --- | --- | --- |
|              |           |              |            |     |         |         | ofsupportingevidence. |     |     | Thesetypesofmulti-hop |     |     |     |
| RAG, several |           | benchmarking | datasets   |     | exist   | for in- |                       |     |     |                       |     |     |     |
queriesrepresentuserqueriescommonlyencoun-
| formationretrievalevaluation. |     |     |     | TheFEVER(Fact |     |     |                             |     |     |     |                  |     |     |
| ----------------------------- | --- | --- | --- | ------------- | --- | --- | --------------------------- | --- | --- | --- | ---------------- | --- | --- |
|                               |     |     |     |               |     |     | teredinreal-worldscenarios. |     |     |     | MultiHop-RAGcon- |     |     |
ExtractionandVERification)dataset,forinstance,
|          |        |            |               |     |          |     | sists of | a knowledge |     | base, | a large | collection | of  |
| -------- | ------ | ---------- | ------------- | --- | -------- | --- | -------- | ----------- | --- | ----- | ------- | ---------- | --- |
| contains | claims | classified | as Supported, |     | Refuted, |     |          |             |     |       |         |            |     |
multi-hopqueries,theirground-truthanswers,and
orNotEnoughInfobythegivenWikipediaarticle
|                     |     |     |                             |     |     |     | the associated |     | supporting | evidence. |     | This | paper |
| ------------------- | --- | --- | --------------------------- | --- | --- | --- | -------------- | --- | ---------- | --------- | --- | ---- | ----- |
| (Thorneetal.,2018). |     |     | Similarly,theSciFactdataset |     |     |     |                |     |            |           |     |      |       |
detailsthecreationprocessofMultiHop-RAG,em-
| comprises                              | scientific |         | claims paired | with | evidence-  |      |             |          |               |     |                 |         |       |
| -------------------------------------- | ---------- | ------- | ------------- | ---- | ---------- | ---- | ----------- | -------- | ------------- | --- | --------------- | ------- | ----- |
|                                        |            |         |               |      |            |      | ploying     | a hybrid | approach      |     | that integrates |         | human |
| containingabstracts(Waddenetal.,2020). |            |         |               |      |            | How- |             |          |               |     |                 |         |       |
|                                        |            |         |               |      |            |      | effort with | GPT-4.   | Additionally, |     | we              | explore | two   |
| ever, the                              | claims     | in both | datasets      | are  | single-hop |      |             |          |               |     |                 |         |       |
usecasesofMultiHop-RAGinthebenchmarking
statements,andthesupportingevidenceisfromone
ofRAGsystems,therebyhighlightingthepotential
singlearticle,incontrasttothemulti-hopqueries
|           |         |        |         |          |        |     | applications |     | of this | dataset. | By  | publicly | releas- |
| --------- | ------- | ------ | ------- | -------- | ------ | --- | ------------ | --- | ------- | -------- | --- | -------- | ------- |
| discussed | in this | paper. | Another | dataset, | HoVer, |     |              |     |         |          |     |          |         |
ingMultiHop-RAG,weaimtoprovideavaluable
involvesclaimsthatrequireextractingandreason-
resourcetothecommunity,contributingtothead-
ingfrommultipleWikipediaarticles(Jiangetal.,
vancementandbenchmarkingofRAGsystems.
2020). However,unlikeourdataset,HoVerfocuses
solelyonclassifyingclaimsaseithersupportedor
Limitations
| not supported |     | by the | articles | without | evaluating |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
anLLMgenerationstep. Moreover,inHoVer,the This work has several limitations that can be im-
Wikipediaarticlesfromwhichevidenceisdrawn provedinfutureresearch. First, ourgroundtruth
are given for claim verification, which is signifi- answersarerestrictedtosimpleresponsessuchas
cantly different from our setting, where relevant “yes", “no", entity names, or temporal indicators
pieces of evidence need to be extracted from a like “before" or “after" to facilitate the use of a

straightforwardaccuracymetricforevaluatinggen- MichaelGünther,JackminOng,IsabelleMohr,Alaed-
erationperformance. Futureworkcouldconsider dineAbdessalem,TanguyAbel,MohammadKalim
Akram,SusanaGuzman,GeorgiosMastrapas,Saba
allowingfreetextasanswersandemployingmore
|     |     |     |     |     |     |     | Sturua, | Bo Wang, | Maximilian |     | Werk, | Nan Wang, |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ---------- | --- | ----- | --------- |
sophisticatedmetricstoassessgenerationquality.
|         |             |         |        |            |     |     | and Han | Xiao. | 2023. | Jina embeddings |     | 2: 8192- |
| ------- | ----------- | ------- | ------ | ---------- | --- | --- | ------- | ----- | ----- | --------------- | --- | -------- |
| Second, | the current | dataset | limits | supporting |     | ev- |         |       |       |                 |     |          |
tokengeneral-purposetextembeddingsforlongdoc-
| idence | for a query | to a   | maximum     | of  | four         | pieces. | uments. |     |     |     |     |     |
| ------ | ----------- | ------ | ----------- | --- | ------------ | ------- | ------- | --- | --- | --- | --- | --- |
| Future | work can    | extend | the dataset |     | by including |         |         |     |     |     |     |     |
XanhHo,Anh-KhoaDuongNguyen,SakuSugawara,
queriesthatrequireretrievingandreasoningfrom
|                   |     |                            |     |     |     |     | and Akiko | Aizawa. | 2020.             | Constructing |     | a multi-      |
| ----------------- | --- | -------------------------- | --- | --- | --- | --- | --------- | ------- | ----------------- | ------------ | --- | ------------- |
| evenmoreevidence. |     | Lastly,whileourexperiments |     |     |     |     |           |         |                   |              |     |               |
|                   |     |                            |     |     |     |     | hop QA    | dataset | for comprehensive |              |     | evaluation of |
utilizeabasicRAGframeworkusingLlamaIndex, reasoning steps. In Proceedings of the 28th Inter-
nationalConferenceonComputationalLinguistics,
futureworkcouldinvolveevaluatingtheanswering
of multi-hop queries using more advanced RAG pages6609–6625,Barcelona,Spain(Online).Inter-
nationalCommitteeonComputationalLinguistics.
frameworksorLLM-agentframeworks.
|     |     |     |     |     |     |     | Albert Q. | Jiang, | Alexandre | Sablayrolles, |         | Antoine |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --------- | ------------- | ------- | ------- |
|     |     |     |     |     |     |     | Roux,     | Arthur | Mensch,   | Blanche       | Savary, | Chris   |
References
|            |       |        |          |           |     |        | Bamford,      | Devendra | Singh      | Chaplot, |           | Diego de las |
| ---------- | ----- | ------ | -------- | --------- | --- | ------ | ------------- | -------- | ---------- | -------- | --------- | ------------ |
|            |       |        |          |           |     |        | Casas,        | Emma     | Bou Hanna, | Florian  | Bressand, | Gi-          |
| Anthropic. | 2023. | Claude | 2.1 (May | version). |     | https: |               |          |            |          |           |              |
|            |       |        |          |           |     |        | anna Lengyel, |          | Guillaume  | Bour,    | Guillaume | Lam-         |
//api.anthropic.com/v1/messages.
|     |     |     |     |     | Claude2.1. |     | ple, Lélio | Renard | Lavaud, | Lucile | Saulnier, | Marie- |
| --- | --- | --- | --- | --- | ---------- | --- | ---------- | ------ | ------- | ------ | --------- | ------ |
AnneLachaux,PierreStock,SandeepSubramanian,
| Akari Asai,   | Sewon                             | Min, | Zexuan | Zhong, | and | Danqi |                                         |         |         |           |        |          |
| ------------- | --------------------------------- | ---- | ------ | ------ | --- | ----- | --------------------------------------- | ------- | ------- | --------- | ------ | -------- |
|               |                                   |      |        |        |     |       | Sophia                                  | Yang,   | Szymon  | Antoniak, | Teven  | Le Scao, |
| Chen.2023.    | Retrieval-basedlanguagemodelsand  |      |        |        |     |       |                                         |         |         |           |        |          |
|               |                                   |      |        |        |     |       | Théophile                               | Gervet, | Thibaut | Lavril,   | Thomas | Wang,    |
| applications. | InProceedingsofthe61stAnnualMeet- |      |        |        |     |       |                                         |         |         |           |        |          |
|               |                                   |      |        |        |     |       | TimothéeLacroix,andWilliamElSayed.2024. |         |         |           |        | Mix-     |
ingoftheAssociationforComputationalLinguistics
tralofexperts.
| (Volume6: | TutorialAbstracts),pages41–46. |            |             |     |        |        |               |                                      |         |       |        |               |
| --------- | ------------------------------ | ---------- | ----------- | --- | ------ | ------ | ------------- | ------------------------------------ | ------- | ----- | ------ | ------------- |
|           |                                |            |             |     |        |        | Yichen Jiang, | Shikha                               | Bordia, | Zheng | Zhong, | Charles       |
| Sebastian | Borgeaud,                      | Arthur     | Mensch,     |     | Jordan | Hoff-  |               |                                      |         |       |        |               |
|           |                                |            |             |     |        |        | Dognin,       | Maneesh                              | Singh,  | and   | Mohit  | Bansal. 2020. |
| mann,     | Trevor                         | Cai, Eliza | Rutherford, |     | Katie  | Milli- |               |                                      |         |       |        |               |
|           |                                |            |             |     |        |        | HoVer:        | Adatasetformany-hopfactextractionand |         |       |        |               |
can,GeorgeBmVanDenDriessche,Jean-Baptiste
|          |        |        |       |     |        |       | claimverification. |     | InFindingsoftheConferenceon |     |     |     |
| -------- | ------ | ------ | ----- | --- | ------ | ----- | ------------------ | --- | --------------------------- | --- | --- | --- |
| Lespiau, | Bogdan | Damoc, | Aidan |     | Clark, | Diego |                    |     |                             |     |     |     |
DeLasCasas,AureliaGuy,JacobMenick,Roman EmpiricalMethodsinNaturalLanguageProcessing
| Ring,   | Tom Hennigan, | Saffron  |           | Huang, | Loren | Mag-     | (EMNLP).        |     |              |     |         |           |
| ------- | ------------- | -------- | --------- | ------ | ----- | -------- | --------------- | --- | ------------ | --- | ------- | --------- |
| giore,  | Chris Jones,  | Albin    | Cassirer, |        | Andy  | Brock,   |                 |     |              |     |         |           |
|         |               |          |           |        |       |          | Ehsan Kamalloo, |     | Xinyu Zhang, |     | Odunayo | Ogundepo, |
| Michela | Paganini,     | Geoffrey | Irving,   |        | Oriol | Vinyals, |                 |     |              |     |         |           |
SimonOsindero,KarenSimonyan,JackRae,Erich Nandan Thakur, David Alfonso-Hermelo, Mehdi
Elsen,andLaurentSifre.2022. Improvinglanguage Rezagholizadeh, and Jimmy Lin. 2023. Evaluat-
models by retrieving from trillions of tokens. In ingembeddingapisforinformationretrieval. arXiv
preprintarXiv:2305.06300.
| Proceedings        | of  | the 39th | International          |     | Conference |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ---------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| onMachineLearning, |     |          | volume162ofProceedings |     |            |     |     |     |     |     |     |     |
of Machine Learning Research, pages 2206–2240. DanielKhashabi, SnigdhaChaturvedi, MichaelRoth,
| PMLR. |     |     |     |     |     |     | Shyam  | Upadhyay,    | and | Dan Roth. | 2018. | Looking     |
| ----- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | --------- | ----- | ----------- |
|       |     |     |     |     |     |     | Beyond | the Surface: | A   | Challenge | Set   | for Reading |
HarrisonChase.2022. LangChain. ComprehensionoverMultipleSentences. InProc.of
theAnnualConferenceoftheNorthAmericanChap-
| Jiawei Chen, | Hongyu | Lin, | Xianpei | Han, | and | Le Sun. |     |     |     |     |     |     |
| ------------ | ------ | ---- | ------- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- |
teroftheAssociationforComputationalLinguistics
| 2023. | Benchmarking |     | large | language | models | in  | (NAACL). |     |     |     |     |     |
| ----- | ------------ | --- | ----- | -------- | ------ | --- | -------- | --- | --- | --- | --- | --- |
retrieval-augmentedgeneration.
|                        |            |        |        |                  |     |     | JerryLiu.2022. |     | LlamaIndex. |     |     |     |
| ---------------------- | ---------- | ------ | ------ | ---------------- | --- | --- | -------------- | --- | ----------- | --- | --- | --- |
| Shahul                 | Es, Jithin | James, | Luis   | Espinosa-Anke,   |     | and |                |     |             |     |     |     |
| StevenSchockaert.2023. |            |        | Ragas: | Automatedevalua- |     |     |                |     |             |     |     |     |
YiLiu,LianzheHuang,ShichengLi,SishuoChen,Hao
tionofretrievalaugmentedgeneration.
Zhou,FandongMeng,JieZhou,andXuSun.2023.
|     |     |     |     |     |     |     | Recall: | A benchmark |     | for llms | robustness | against |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | -------- | ---------- | ------- |
TianyuGao,HowardYen,JiatongYu,andDanqiChen.
externalcounterfactualknowledge.
2023. Enablinglargelanguagemodelstogenerate
textwithcitations.
|         |       |      |     |        |     |           | OpenAI.2023.     | GPT4(Nov7version). |                     |     | https://chat. |     |
| ------- | ----- | ---- | --- | ------ | --- | --------- | ---------------- | ------------------ | ------------------- | --- | ------------- | --- |
|         |       |      |     |        |     |           | openai.com/chat. |                    | gpt-4-1106-preview. |     |               |     |
| Google. | 2023. | PaLM |     | 2 (May |     | version). |                  |                    |                     |     |               |     |
https://generativelanguage.googleapis.
com/v1beta2/models/. Chat-bison-002. JonSaad-Falcon,OmarKhattab,ChristopherPotts,and
|     |     |     |     |     |     |     | Matei Zaharia. |     | 2023. Ares: | An  | automated | evalua- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | --------- | ------- |
SignificantGravitas.2023. Autogpt. https://github. tionframeworkforretrieval-augmentedgeneration
| com/Significant-Gravitas/AutoGPT. |     |     |     |     |     |     | systems. |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |

HongjinSu,WeijiaShi,JungoKasai,YizhongWang, Jiawei Han. 2022. Towards a unified multi-
Yushi Hu, Mari Ostendorf, Wen tau Yih, Noah A. dimensionalevaluatorfortextgeneration.
| Smith, | Luke | Zettlemoyer, |     | and Tao | Yu. 2023. | One |     |     |     |     |
| ------ | ---- | ------------ | --- | ------- | --------- | --- | --- | --- | --- | --- |
embedder, any task: Instruction-finetuned text em- A AppendixA:GPT-4PromptsUsedfor
| beddings. |         |         |     |          |     |          | DataGeneration |     |     |     |
| --------- | ------- | ------- | --- | -------- | --- | -------- | -------------- | --- | --- | --- |
| James     | Thorne, | Andreas |     | Vlachos, |     | Christos |                |     |     |     |
WepresentthepromptsusedforguidingGPT-4for
| Christodoulopoulos, |               |       | and     | Arpit | Mittal.         | 2018.     |                                               |                             |              |     |
| ------------------- | ------------- | ----- | ------- | ----- | --------------- | --------- | --------------------------------------------- | --------------------------- | ------------ | --- |
|                     |               |       |         |       |                 |           | datageneration.                               | Table7showsthepromptusedfor |              |     |
| Fever:              | a large-scale |       | dataset | for   | fact extraction | and       |                                               |                             |              |     |
| verification.       |               |       |         |       |                 |           | claimgeneration,alongwiththecorrespondingtop- |                             |              |     |
|                     |               |       |         |       |                 |           | icsandentitieswithintheseclaims.              |                             | Table8,Table |     |
| Hugo Touvron,       |               | Louis | Martin, | Kevin | Stone,          | Peter Al- |                                               |                             |              |     |
9,andTable10respectivelyshowthepromptsused
| bert, Amjad |     | Almahairi, | Yasmine |     | Babaei, | Nikolay |     |     |     |     |
| ----------- | --- | ---------- | ------- | --- | ------- | ------- | --- | --- | --- | --- |
Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti forgeneratingmulti-hopqueriesoftheinference,
Bhosale,DanBikel,LukasBlecher,CristianCanton
comparison,andtemporaltypes.
Ferrer,MoyaChen,GuillemCucurull,DavidEsiobu,
JudeFernandes,JeremyFu,WenyinFu,BrianFuller, B AppendixB:DatasetExamples
CynthiaGao,VedanujGoswami,NamanGoyal,An-
thonyHartshorn,SagharHosseini,RuiHou,Hakan
|     |     |     |     |     |     |     | In this appendix, | we present | an example | of each |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | ---------- | ------- |
Inan,MarcinKardas,ViktorKerkez,MadianKhabsa,
IsabelKloumann,ArtemKorenev,PunitSinghKoura, typeofmulti-hopqueryincludedintheMultiHop-
|     |     |     |     |     |     |     | RAGdataset. | Theseexamplesareillustratedinthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------------------------- | --- | --- |
Marie-AnneLachaux,ThibautLavril,JenyaLee,Di-
anaLiskovich,YinghaiLu,YuningMao,XavierMar- respectivetables: Table12forInferenceQueries,
tinet,TodorMihaylov,PushkarMishra,IgorMoly-
|            |      |        |     |          |        |         | Table 13 | for Comparison | Queries, Table | 14 for |
| ---------- | ---- | ------ | --- | -------- | ------ | ------- | -------- | -------------- | -------------- | ------ |
| bog, Yixin | Nie, | Andrew |     | Poulton, | Jeremy | Reizen- |          |                |                |        |
TemporalQueries,andTable15forNullQueries.
stein,RashiRungta,KalyanSaladi,AlanSchelten,
|      |        |              |     |        |        |          | Each query | is paired with | a ground-truth | answer |
| ---- | ------ | ------------ | --- | ------ | ------ | -------- | ---------- | -------------- | -------------- | ------ |
| Ruan | Silva, | Eric Michael |     | Smith, | Ranjan | Subrama- |            |                |                |        |
nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay- for the evaluation of generation accuracy, while
lor, Adina Williams, Jian Xiang Kuan, Puxin Xu, multiplepiecesofsupportingevidenceareincluded
ZhengYan,IliyanZarov,YuchenZhang,AngelaFan,
|         |           |     |        |         |          |     | forassessingretrievalperformance. |     | Additionally, |     |
| ------- | --------- | --- | ------ | ------- | -------- | --- | --------------------------------- | --- | ------------- | --- |
| Melanie | Kambadur, |     | Sharan | Narang, | Aurelien | Ro- |                                   |     |               |     |
metadatasuchasthetitle,source,andpublication
driguez,RobertStojnic,SergeyEdunov,andThomas
Scialom.2023. Llama2: Openfoundationandfine- timeofthenewsarticlesareprovidedasreferences.
tunedchatmodels.
| David Wadden,            |           | Shanchuan |             | Lin, Kyle               | Lo,         | Lucy Lu |     |     |     |     |
| ------------------------ | --------- | --------- | ----------- | ----------------------- | ----------- | ------- | --- | --- | --- | --- |
| Wang,                    | Madeleine | van       | Zuylen,     | Arman                   | Cohan,      | and     |     |     |     |     |
| HannanehHajishirzi.2020. |           |           |             | Factorfiction:Verifying |             |         |     |     |     |     |
| scientific               | claims.   | In        | Proceedings |                         | of the 2020 | Con-    |     |     |     |     |
ferenceonEmpiricalMethodsinNaturalLanguage
Processing(EMNLP),pages7534–7550,Online.As-
sociationforComputationalLinguistics.
| Liang Wang, | Nan | Yang, | Xiaolong |     | Huang, | Binxing |     |     |     |     |
| ----------- | --- | ----- | -------- | --- | ------ | ------- | --- | --- | --- | --- |
Jiao,LinjunYang,DaxinJiang,RanganMajumder,
| and Furu                           | Wei. | 2022. | Text | embeddings | by            | weakly- |     |     |     |     |
| ---------------------------------- | ---- | ----- | ---- | ---------- | ------------- | ------- | --- | --- | --- | --- |
| supervisedcontrastivepre-training. |      |       |      |            | arXivpreprint |         |     |     |     |     |
arXiv:2212.03533.
| Shitao Xiao, | Zheng | Liu,  | Peitian | Zhang,   | and       | Niklas |     |     |     |     |
| ------------ | ----- | ----- | ------- | -------- | --------- | ------ | --- | --- | --- | --- |
| Muennighoff. |       | 2023. | C-pack: | Packaged | resources |        |     |     |     |     |
toadvancegeneralchineseembedding.
| Zhilin Yang, | Peng | Qi, | Saizheng | Zhang, | Yoshua | Ben- |     |     |     |     |
| ------------ | ---- | --- | -------- | ------ | ------ | ---- | --- | --- | --- | --- |
gio,WilliamW.Cohen,RuslanSalakhutdinov,and
| ChristopherD.Manning.2018. |     |     |     | HotpotQA:Adataset |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
fordiverse,explainablemulti-hopquestionanswer-
ing. InConferenceonEmpiricalMethodsinNatural
LanguageProcessing(EMNLP).
PeitianZhang,ShitaoXiao,ZhengLiu,ZhichengDou,
| andJian-YunNie.2023. |     |     |     | Retrieveanythingtoaug- |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
mentlargelanguagemodels.
| Ming Zhong,   | Yang | Liu, | Da        | Yin, Yuning | Mao,      | Yizhu   |     |     |     |     |
| ------------- | ---- | ---- | --------- | ----------- | --------- | ------- | --- | --- | --- | --- |
| Jiao, Pengfei |      | Liu, | Chenguang |             | Zhu, Heng | Ji, and |     |     |     |     |

A"claim"isastatementorassertionmadewithinatextexpressingabelief,opinion,orfact. Given
evidencefromtheoriginalcontext,pleaseextractoneclaimanditsassociatedtopics.
Note: Theclaimshouldnotcontainambiguousreferences,suchas’he’,’she,’and’it’,andshoulduse
completenames. Iftherearemultipletopics,givethemostdominantone. Thetargetoftheclaim(one
entity)isthespecificindividual,group,ororganizationthatthestatementorassertionwithinatextis
directedtowardsoraboutwhichitismakingacase. Thetopicoftheclaimshouldbeasimplephrase
representingtheclaim’scentralargumentconcept. Ifthereisnoclaim,pleaseleaveitblank. Please
generateaclaimbasedonthegivenevidence. Don’tgeneratetheevidenceyourself.
Pleasegivetheresponsefollowingthisformat:
Evidence: [originalcontext]
Claims: [extractclaim]
ClaimTarget: [target]
ClaimTopic: [topic]
Hereareexamples:
<examples>
Now,it’syourturn.
<News>
<evidence>
Table7: ClaimGenerationPrompting
A multi-hop question is a query requiring multiple inferential leaps or accessing several pieces of
informationfromdifferentlocationsorsourcestoarriveatananswer. Thefollowingarenewsarticles’
metadata and claims come from the articles. All the claims from the article are related to a similar
target. Yourtaskistogenerateonemulti-hopinferencequestionbasedontheclaims. Herearesome
instructions:
1. FindtheConnection: Theconnectionbetweenclaimsis<target>,whichishowthesekeypiecesof
informationarerelatedorhowtheycanbecombinedtoformamorecomplexidea.
2. FormulatetheQuestion: Createaquestionthatcannotbeansweredbyrelyingonjustoneofthe
sentencesbutinsteadrequiresunderstandingandlinkingtheinformationfromallofthesources. The
answeris<target>.
3. EnsureCoherence: Makesurethequestionflowslogicallyfromthecombinedinformationandis
clearandunambiguous.
4. Usethekeywords: <keyset>
<examples>
Context:
<Context>
Table8: InferenceQueryGenerationPrompting

<Context>
The above are news articles’ metadata and claims come from the articles. All the claims from the
articlesarerelatedtoasimilartarget. Yourtaskistogenerateonecomparisonquestionbasedonallthe
claimsfromdifferentsources. Thisquestionneedstocomparesomefactualelementsoftheclaimsthat
areexplicitlystatedtofindwheretheyagreeordiffer. Thecorrectanswertothisquestionisexpressed
asacomparativeadjective,astatementofalignment,asimpleyesorno. Togenerateacomparative
questionfromclaims,youneedtousethefollowingkeywords: <keyset>
TheGoodComparisonQuestions:
<examples>
YourComparisonQuestion:
Table9: ComparisonQueryGenerationPrompting
<Context>
Pleasecreateatime-sensitivecomparisonquestionusingmetadataandexcerptsfrommultiplenews
articles. Thatistocomparetheconsistencyorsequenceofreportsonsimilartopicsatmultipledifferent
timepoints. Ifitistocomparetheconsistency,pleaseclearlymentionthenewssourceandtimeinthe
questionusing<timeframe>. Ifitistocomparesequencesofreports,justclearlymentionthenews
sourceanddonotmentionthetimeline. Utilizethefollowingkeywordsprovidedinthe<keyset>to
constructthequestion. Thecorrectanswershouldbasedonthefactualexcerptsandisonlyoneword.
<examples>
Yourtime-sensitivecomparisonquestion:
Table10: TemporalQueryGenerationPrompting
A multi-hop question is a query requiring multiple inferential leaps or accessing several pieces of
information from different locations or sources to arrive at an answer. Considering you have read
atleasttwonewsarticleson<entity>,constructamulti-hopquestionthatincorporatesallthenews
sources. Thesourceofthenewsshouldbestatedinthequestion. Also,ensurethattheanswertothe
questionisasingleword/entity. Donotanswerthisquestiondirectly. Justgivemethequestion:
Table11: NullQueryGenerationPrompting

Query: Which platform is at the center of discussions in articles from Music Business Worldwide,
Polygon,andFOXNews-Health,concerningthepolicingofAI-drivenvoicereplication,thedebate
over"reaction"content,andbeingthemostusedappovernightbyyoungpeople?
Answer: YouTube
EvidenceList:
Title: SonyMusic’sartistsaren’tinvolvedinYouTube’snewvoice-cloningAIexperiment.
Source: MusicBusinessWorldwide
PublishedTime: 2023-11-23T18:48:48+00:00
Fact: During this period of discussion, YouTube has made a number of positive announcements
regardingthebiggestissueforanyrightsholderregardingAI-drivenvoicereplicationofartists: their
abilitytopoliceit.
Title: YouTubedemonetizespopularcontentcreatorSSSniperwolfafterdoxxingaccusations
Source: Polygon
PublishedTime: 2023-10-25T18:18:06+00:00
Fact: Thedebateover"reaction"contentonYouTubehasbeenbrewingforyears,butarecentincident
betweentwocreatorshasrefueledtheurgencyoftheconversation.
Title: Cellphoneshockeras97%ofkidsusetheirdeviceduringschoolhoursandbeyond,saysstudy
Source: FOXNews-Health
PublishedTime: 2023-10-01T09:05:26+00:00
Fact: Overnight phone use was primarily spent engaging with the same media, although YouTube
appearedtobethelongest-runningappbecausevideoswereoftenleftplayingduringthenight.
Table12: Theexampleofinferencequestions
Query: DidtheCnbc|WorldBusinessNewsLeaderreportonNike’snetincomeandthearticlefrom
TheAgeonthe10-yearTreasuryyieldbothreportadecreaseintheirrespectivefinancialmetrics?
Answer: Yes
EvidenceList:
Title: Nike misses revenue expectations for the first time in two years, beats on earnings and gross
margin
Source: Cnbc|WorldBusinessNewsLeader
PublishedTime: 2023-09-28T20:31:00+00:00
Fact: Thecompany’sreportednetincomeforthethree-monthperiodthatendedAugust31was$1.45
billion,or94centspershare,comparedwith$1.47billion,or93centspershare,ayearearlier.
Title: ASXsettoopenhigherasWallStreetrebounds;$Arises
Source: TheAge
PublishedTime: 2023-10-04T21:01:01+00:00
Fact: Theyieldonthe10-yearTreasury,whichisthecentrepieceofthebondmarket,pulledbackfrom
itshighestlevelsince2007,downto4.73percentfrom4.80percentlateonTuesday.
Table13: Theexampleofcomparisonquestions

Query: WastheperformanceoftheChicagoBears’defensereportedasimprovedbyYardbarkerafter
SportingNewshighlightedasackbytheBears’defenseonJoshuaDobbsduringtheNFL’Monday
NightFootball’game?
Answer: Yes
EvidenceList:
Title: Bearsvs. Vikingslivescore,updates,highlightsfromNFL’MondayNightFootball’game
Source: SportingNews
PublishedTime: 2023-11-27T23:32:04+00:00
Fact: TheBearsanswerrightbackandsackDobbs,withSweatandBriskerintheretotakehimdown.
Title: HottestseatoneachNFCteam: Bunsburningforthesefourheadcoaches
Source: Yardbarker
PublishedTime: 2023-11-30T22:29:33+00:00
Fact: InhissecondseasonasHC,thedefensehasimproved,butpositiveresultsarehardtocomeby
behindalacklusteroffenseranked19thinyards(323.2)and21stinpointspergame(20.2).
Table14: Theexampleoftime-sensitivequestions
Query: WhatisthefirstletteroftheCEO’slastnameinthenewsarticlefromBloombergonTomTom,
andwhatisthefirstletterofthecitywherethecompany’sheadquartersislocatedinthenewsarticle
fromReuters?
Answer: Insufficientinformation.
Table15: Theexampleofnegativerejectionquestions