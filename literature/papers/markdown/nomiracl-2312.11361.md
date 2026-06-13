“Knowing When You Don’t Know”: A Multilingual Relevance Assessment
|     | Dataset |     | for | Robust | Retrieval-Augmented |     |     | Generation |     |     |     |     |
| --- | ------- | --- | --- | ------ | ------------------- | --- | --- | ---------- | --- | --- | --- | --- |
NandanThakur1,LuizBonifacio1,3,XinyuZhang1,OdunayoOgundepo1,
EhsanKamalloo1,DavidAlfonso-Hermelo2,XiaoguangLi2,QunLiu2,
BoxingChen2,MehdiRezagholizadeh2,JimmyLin1
1 DavidR.CheritonSchoolofComputerScience,UniversityofWaterloo,Canada
|     |     | 2 HuaweiNoah’sArkLab |     |     |     | 3 FEEC-Unicamp,Brazil |     |     |     |     |     |     |
| --- | --- | -------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
Abstract
|                     |     |     |            |     |       | Non-relevant Subset            |     |     |     | Relevant Subset           |     |     |
| ------------------- | --- | --- | ---------- | --- | ----- | ------------------------------ | --- | --- | --- | ------------------------- | --- | --- |
|                     |     |     |            |     |       | What does the AC button on the |     |     |     | When was the food pyramid |     |     |
| Retrieval-Augmented |     |     | Generation |     | (RAG) |                                |     |     |     |                           |     |     |
|                     |     |     |            |     |       | calculator stand for?          |     |     |     | first introduced?         |     |     |
groundsLargeLanguageModel(LLM)output
4202 voN 01  ]LC.sc[  3v16311.2132:viXra [1] Food pyramid (nutrition):
[1] Power Electronics: AC
by leveraging external knowledge sources Voltage Controller: The purpose A food pyramid represents the
|     |     |     |     |     |     | of an AC Voltage Controller, or |     |     |     | optimal number of servings to |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
to reduce factual hallucinations. However, be eaten each day from each
|     |     |     |     |     |     | AC Regulator, is to vary the RMS |     |     |     | of the food groups. The first |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
voltage across the load while at
prior work lacks a comprehensive evaluation a constant frequency ...  pyramid was published in
Sweden in 1974.
| of different |     | language | families, | making     | it  |                            |     |               |     |                               |               |     |
| ------------ | --- | -------- | --------- | ---------- | --- | -------------------------- | --- | ------------- | --- | ----------------------------- | ------------- | --- |
|              |     |          |           |            |     |                            |     | relevance = 0 |     |                               | relevance = 1 |     |
| challenging  | to  | evaluate | LLM       | robustness |     |                            |     |               |     |                               |               |     |
|              |     |          |           |            |     | [2] Calculator: Electronic |     |               |     | [2] History of USDA nutrition |               |     |
againsterrorsinexternalretrievedknowledge. calculators contain a keyboard guides: The introduction of the
|     |     |     |     |     |     | with buttons for digits and |     |     |     | USDA's food guide pyramid in |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
Toovercomethis,weestablishNoMIRACL,a
|     |     |     |     |     |     | arithmetical operations; some   |     |     |     | 1992 attempted to express the |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
|     |     |     |     |     |     | even contain \"00\" and \"000\" |     |     |     | recommended servings of each  |     |     |
human-annotateddatasetforevaluatingLLM buttons to make larger or food group, which previous
|            |              |            |          |                  |          | smaller numbers easier ...  |     |               |     | guides ... |               |     |
| ---------- | ------------ | ---------- | -------- | ---------------- | -------- | --------------------------- | --- | ------------- | --- | ---------- | ------------- | --- |
| robustness | in           | RAG across |          | 18 typologically |          |                             |     |               |     |            |               |     |
|            |              |            |          |                  |          |                             |     | relevance = 0 |     |            | relevance = 0 |     |
| diverse    | languages.   |            | NoMIRACL |                  | includes |                             |     |               |     |            |               |     |
| both a     | non-relevant |            | and a    | relevant         | subset.  |                             |     |               |     |            |               |     |
Queries in the non-relevant subset contain Yes, Answer is Yes, Answer is
|     |     |     |     |     |     | present |     | I don't know |     | present | I don't know |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | --- | ------- | ------------ | --- |
|     |     |     |     |     |     | LLM     |     |              | LLM |         |              |     |
passages judged as non-relevant, whereas False True True False
queriesintherelevantsubsetincludeatleasta Positive (FP) Negative (TN) Positive (TP) Negative (FN)
| single judged             |     | relevant | passage. | We               | measure |          |                                      |     |     |     |     |     |
| ------------------------- | --- | -------- | -------- | ---------------- | ------- | -------- | ------------------------------------ | --- | --- | --- | --- | --- |
|                           |     |          |          |                  |         | Figure1: | LLMrobustnessevaluationasabinarytree |     |     |     |     |     |
| relevanceassessmentusing: |     |          |          | (i)hallucination |         |          |                                      |     |     |     |     |     |
inNoMIRACL.Whendealingwithqueriesinthenon-
rate,measuringmodeltendencytohallucinate,
|     |     |     |     |     |     | relevant | subset, | the LLM | is expected | to  | disregard | all |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ------- | ----------- | --- | --------- | --- |
when the answer is not present in passages noisypassagesandrefrainfromanswering(TN). Con-
inthenon-relevantsubset,and(ii)errorrate,
|           |          |            |              |              |     | versely,         | for queries | in           | the relevant | subset, | the         | LLM |
| --------- | -------- | ---------- | ------------ | ------------ | --- | ---------------- | ----------- | ------------ | ------------ | ------- | ----------- | --- |
| measuring | model    | inaccuracy |              | to recognize |     |                  |             |              |              |         |             |     |
|           |          |            |              |              |     | should recognize |             | the relevant | passage      |         | and provide | a   |
| relevant  | passages | in         | the relevant | subset.      | In  |                  |             |              |              |         |             |     |
validanswer(TP).
| our work,                          | we  | observe | that | most | models |     |     |     |     |     |     |     |
| ---------------------------------- | --- | ------- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
| struggletobalancethetwocapacities. |     |         |      |      | Models |     |     |     |     |     |     |     |
such as LLAMA-2 and Orca-2 achieve over sages)togenerateaccurateandfaithfulresponses
| 88% hallucination |     | rate | on  | the non-relevant |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(Shusteretal.,2021;Gaoetal.,2023b;Liuetal.,
subset. Mistral and LLAMA-3 hallucinate 2024). Ever since the advent of Large Language
| less but | can achieve | up      | to a     | 74.9% error | rate |          |         |      |          |         |        |         |
| -------- | ----------- | ------- | -------- | ----------- | ---- | -------- | ------- | ---- | -------- | ------- | ------ | ------- |
|          |             |         |          |             |      | Models   | (LLMs), | such | as GPT-3 | (Brown  |        | et al., |
| on the   | relevant    | subset. | Overall, | GPT-4       | is   |          |         |      |          |         |        |         |
|          |             |         |          |             |      | 2020) or | LLAMA-2 |      | (Touvron | et al., | 2023), | they    |
observedtoprovidethebesttradeoffonboth
|          |              |     |        |                |     | are the | de-facto | choice | for answer | generation |     | in  |
| -------- | ------------ | --- | ------ | -------------- | --- | ------- | -------- | ------ | ---------- | ---------- | --- | --- |
| subsets, | highlighting |     | future | work necessary |     |         |          |        |            |            |     |     |
RAG,duetotheirunprecedentedprogressintext
| to improve | LLM | robustness. |     | NoMIRACL |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
dataset and evaluation code are available at: generationandunderstanding(Brownetal.,2020;
https://github.com/project-miracl/nomiracl.
Lietal.,2024;Changetal.,2024;Guoetal.,2023).
RAGgroundstheLLM-generatedanswer,thereby
1 Introduction
avoidingpreviouslyobservedfactualhallucination
Retrieval-Augmented Generation (RAG) (Guu (Maynezetal.,2020;Raunaketal.,2021)andout-
datedknowledge(Caoetal.,2021;Heetal.,2023)
etal.,2020;Lewisetal.,2020;IzacardandGrave,
inLLMs.
| 2021; Borgeaud |     | et al., 2022) |     | is a promising | way |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
toincorporateexternalknowledgeviaafirst-stage A challenging issue in RAG is to provide ro-
retrievalsystem. RAGinstillsinformationfromre- bust and reliable LLM-generated answers. The
liableknowledgecorpora(providedasexternalpas- answergenerationstageisdependentonthefirst-

| stage information |       | retrieval  |     | system.    | The | retrieval  |                |     |              |          |     |
| ----------------- | ----- | ---------- | --- | ---------- | --- | ---------- | -------------- | --- | ------------ | -------- | --- |
|                   |       |            |     |            |     |            | Pred. / Subset |     | Non-Relevant | Relevant |     |
| system            | poses | challenges | in  | accurately |     | retrieving |                |     |              |          |     |
LLM: Yes, answer
| relevantinformationwhenevaluatedeitheronzero- |     |     |     |     |     |     |     |     | FP  |     | TP  |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is present
shotdomains(Thakuretal.,2021)orlow-resource
languages (Zhang et al., 2023). The incorrect or LLM: I don't know TN FN
non-relevantinformationcontainedinretrievedpas-
|     |     |     |     |     |     |     | Hallucination rate |     |     | Error rate =  |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ------------- | --- |
sages can frequently mislead the LLM to hallu-  =  FP / (FP + TN) FN / (FN + TP)
| cinate (Adlakha |            | et al., | 2024; | Chen          | et    | al., 2024; |                     |         |                  |            |             |
| --------------- | ---------- | ------- | ----- | ------------- | ----- | ---------- | ------------------- | ------- | ---------------- | ---------- | ----------- |
|                 |            |         |       |               |       |            | Figure 2: Confusion |         | matrix for       | robustness | evalua-     |
| Shi et          | al., 2023; | Yoran   | et    | al.,          | 2024; | Yu et al., |                     |         |                  |            |             |
|                 |            |         |       |               |       |            | tion with NoMIRACL. |         | More details     | are        | provided in |
| 2023).          | Prior work | lacks   | a     | comprehensive |       | evalu-     |                     |         |                  |            |             |
|                 |            |         |       |               |       |            | (§2.1); (Subset)    | denotes | the ground-truth |            | in NoMIR-   |
ation of LLM reasoning capabilities in multiple ACL;(Pred.) denotestheLLMoutputprediction.
| languages. | Asaresult,itremainsuncleartowhich |     |     |     |     |     |     |     |     |     |     |
| ---------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
extentLLMshallucinateacrossbothhigh-orlow-
|     |     |     |     |     |     |     | naleintheiroutputgenerationbyover88%. |     |     |     | Inad- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ----- |
resourcelanguages.
dition,weconductdifferentpromptingtechniques
| To facilitate |     | research |     | in this | direction, | we  |     |     |     |     |     |
| ------------- | --- | -------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
andobservethatsupervisedfine-tuningLLMson
presentNoMIRACL,alargemultilingualhuman-
theNoMIRACLdevelopmentsetcanbetricky.
annotateddatasetcontainingover56,000(includ-
ingbothnon-relevantandrelevantsamples)toeval- Tosummarize,ourcontributionsare: (i)Wein-
uateLLMrobustnessagainsterrorsinfirst-stageex- troduceNoMIRACL,anovelmultilingualdataset
ternalinformation,i.e.,retrievedpassages,across toevaluateLLMhallucinationsagainstfirst-stage
18 typologically diverse languages. To construct retrieval errors in RAG. (ii) We evaluate several
|     |     |     |     |     |     |     | powerful multilingual |     | LLMs | and observe | chal- |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ---- | ----------- | ----- |
thedataset,wehired31nativespeakersashuman
annotators(Zhangetal.,2023). NoMIRACLcon- lengesinLLMrobustnessbyoftenhallucinatingan
tainstwosubsets,non-relevantandrelevant. The answerwithinnon-answerablepassagesinthenon-
non-relevant subset contains all queries with no relevantsubsetandtheinabilitytorecognizerele-
known answers, i.e., all top-k retrieved passages vantpassagesintherelevantsubset. (iii)Wecon-
manuallyjudgedasnon-relevant. Conversely,the ductthoroughmanualinspectionsonLLM’sgener-
relevant subset contains queries with known an- ationresults,andfindseveralhallucinationpatterns
|        |          |           |     | top-k |          |     | foreachgenreoftheLLM;WehopeNoMIRACL |     |     |     |     |
| ------ | -------- | --------- | --- | ----- | -------- | --- | ----------------------------------- | --- | --- | --- | --- |
| swers, | i.e., at | least one | of  | the   | passages | is  |                                     |     |     |     |     |
manuallyjudgedasrelevant. can serve as a valuable dataset towards a much-
To better understand the LLM robustness in neededLLMrobustnessevaluation.
NoMIRACL,weconductexperimentswithseveral
existingpowerfulandmultilingual-focusedLLMs
2 BackgroundandProblemIdentification
| (e.g., GPT-4, |     | Mistral, | LLAMA-3). |     | We  | conduct |     |     |     |     |     |
| ------------- | --- | -------- | --------- | --- | --- | ------- | --- | --- | --- | --- | --- |
our experiments using the top-k oracle passages AchallengingissueinRAGistoproviderobustand
| retrieved | using | a hybrid | retrieval |     | system | from a |     |     |     |     |     |
| --------- | ----- | -------- | --------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
reliableLLM-generatedoutputagainstafirst-stage
language-specificWikipediacorpus(Zhangetal.,
|     |     |     |     |     |     |     | informationretrievalsystem. |     | Overrelianceofthe |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | ----------------- | --- | --- |
2023). We use a zero-shot “vanilla” prompt tem- LLMonthecontentoftheretrievedpassages(i.e.,
plate for prompting all LLMs. Our key findings tendencytoextractinformationfrompassages)can
are: First,LLMssuchasLLAMA-2,Aya-101,and
belimitingwhenpassagesarenoisyornon-relevant
Orca-2observeasurprisinglyhigh88%hallucina-
(Yuetal.,2023;Yoranetal.,2024;Shietal.,2023).
| tion rate | on the | non-relevant |     | subset. | Second, | the |     |     |     |     |     |
| --------- | ------ | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- |
Mistral and LLAMA-3 series of models halluci- RAGBackground. Retrieval-augmentedgenera-
natelessbutperformworseontherelevantsubset. tion(RAG)(Lewisetal.,2020;Guuetal.,2020)
Overall, GPT-4 is found to provide the optimal involvesatwo-stageinferencepipeline. Inthefirst
performancetradeoffacrossbothsubsets. stage,giventheretrievalsystemandtheuserquery,
Tounderstandourexperimentalfindingsbetter, the retrieval system provides the subset of top-k
weconductanempiricalanalysisonNoMIRACL passagesretrievedfromanexternaldatacorpusC.
(en)toanalyzetheblindspotsinasubsetofLLMs. For the next stage, the user query with the top-k
WeobserveLLAMA-2-7Band13Binterestingly retrievedpassagesisprovidedtotheLLM,which
repeatthequeryandpromptinstructionsonaverage generates an output summarizing the answer for
byatleast25%. Mistral-7Balwaysprovidesaratio- thequeryandcitingtherelevantpassages.

Q: What does the AC button all non-relevant passages Non-relevant subset (Rel = 0)
on a calculator stand for?
Q u e r y
annotator hu m a n   g e n e r a t e d   q u e ry a n n o t a t o r relev a t  l N o n - r e l e v a n t   p a s s a g e
e a
a n s t
|        |     |     |                         |               |                          |                                        |     | t   p o n e |     | R e l e van t   s | u b s e t   ( R e l   = |   1/ 0) |
| ------ | --- | --- | ----------------------- | ------------- | ------------------------ | -------------------------------------- | --- | ----------- | --- | ----------------- | ----------------------- | ------- |
|        |     |     |                         |               | [ 1 ]   P o w e r   E    | l e c t r o n i c s :   A C   V o lt a | g e | a s         |     |                   |                         |         |
|        |     |     |            B M 2 5      |   +   m D P R |                          |                                        |     | s a g       |     |                   |                         |         |
|        |     |     |                         |               | C o n t r o ll e r :     | T h e   p u r p o s e   o f  a n   A   | C   | e           |     | Q u e r y R e     | le v a n t  p a s s a g | e       |
|        |     |     |         +   m C         | o l B E R T   | V o l t a g e   C o n    | t r o l l e r   . .. .                 |     |             |     |                   |                         |         |
| corpus |     |     | hybrid retrieval system |               |                          |                                        |     |             |     |                   |                         |         |
|        |     |     |                         |               | top-k retrieved passages |                                        |     |             |     | NoMIRACL Dataset  |                         |         |
Figure3: Anoverviewofthedataconstructionprocedure(forEnglish)involvedinNoMIRACL.
| 2.1 RobustnessEvaluation |     |            |          |     |           | 3 NoMIRACLDataset |      |             |     |       |            |     |
| ------------------------ | --- | ---------- | -------- | --- | --------- | ----------------- | ---- | ----------- | --- | ----- | ---------- | --- |
| We conduct               | our | evaluation | strategy | as  | a contin- |                   |      |             |     |       |            |     |
|                          |     |            |          |     |           | As the            | goal | of NoMIRACL |     | is to | understand | to  |
gencytable(asshowninFigure2)torobustlyeval-
whichextentLLMstendtohallucinateacrossdif-
| uate the | LLM | behavior | in both | answerable | and |                   |     |     |         |          |            |     |
| -------- | --- | -------- | ------- | ---------- | --- | ----------------- | --- | --- | ------- | -------- | ---------- | --- |
|          |     |          |         |            |     | ferent languages, |     | our | dataset | contains | 18 diverse |     |
non-answerablescenariosusingabinaryclassifica-
|     |     |     |     |     |     | languages | with | a myriad |     | of both | correct | or an- |
| --- | --- | --- | --- | --- | --- | --------- | ---- | -------- | --- | ------- | ------- | ------ |
tiontask,bycomparingLLMpredictionsagainst
swerablequeries(relevant)subsetandhallucinated
thegroundtruthprovidedbyhumanannotators.
|              |                               |     |     |     |     | or unanswerable |     | queries | (non-relevant). |     | We  | de- |
| ------------ | ----------------------------- | --- | --- | --- | --- | --------------- | --- | ------- | --------------- | --- | --- | --- |
| Definitions. | NoMIRACLcontainstwosubsets,we |     |     |     |     |                 |     |         |                 |     |     |     |
scribeourdatasetconstructionprocedurein(§3.1),
denotethemaseithernon-relevant(F)orrelevant
foldcreationin(§3.2)andlanguagescoveredand
(T). Thenon-relevantsubsetcontainsquerieswith
|                               |     |     |     |                 |     | dataset | usage | in (§3.3). | An  | overview | of our | data |
| ----------------------------- | --- | --- | --- | --------------- | --- | ------- | ----- | ---------- | --- | -------- | ------ | ---- |
| no-knownanswers,i.e.,alltop-k |     |     |     | passagesarenon- |     |         |       |            |     |          |        |      |
constructionprocedureisshowninFigure3.
relevant,whiletherelevantsubsetcontainsqueries
| with known | answers, |     | i.e., at least | one | of the top- |     |     |     |     |     |     |     |
| ---------- | -------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
3.1 DataConstructionProcedure
| k passages | is relevant. |     | Similarly, | we  | denote the |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
LLM prediction as either positive (P) indicating NoMIRACLisconstructedusingthesameproce-
|     |     |     |     |     |     | dure utilized |     | to develop | MIRACL |     | (Zhang | et al., |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------ | --- | ------ | ------- |
themodelfindsthepassagerelevanttoanswerthe
queryandsimilarlynegative(N)denotesthemodel 2023). Thedataconstructionoccursintwostages,
doesnotfindanypassagerelevant(i.e.,containing following(Zhangetal.,2023;Clarketal.,2020).
theanswer)forthequery. Inthefirststage,theannotator(anativelanguage
speaker)writesawell-formedqueryforeachindi-
| Confusion  | Matrix. | In           | our confusion |         | matrix (cf. |                   |     |                             |     |     |     |     |
| ---------- | ------- | ------------ | ------------- | ------- | ----------- | ----------------- | --- | --------------------------- | --- | --- | --- | --- |
|            |         |              |               |         |             | vidualprompttext. |     | Eachpromptisashorttextsnip- |     |     |     |     |
| Figure 2), | for our | non-relevant |               | subset, | True Neg-   |                   |     |                             |     |     |     |     |
ative(TN)denoteswhenthemodelcorrectlypre- petcontainingthefirst100wordsfromalanguage-
|     |     |     |     |     |     | specificWikipediacorpus. |     |     |     | Next,foreachhuman- |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | ------------------ | --- | --- |
dictsquerieswithno-knownanswersusingthenon-
|     |     |     |     |     |     | generatedquery,top-k |     |     | passagesareretrievedfrom |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------ | --- | --- | --- |
relevantretrievedpassages,whereasFalsePositive
thecorpususingahybridmultilingualretrievalsys-
(FP)denoteswhenthemodelpredictionisincor-
rectonthenon-relevantsubset. Similarly,TruePos- tem (more details in §4.1). In the second stage,
|            |            |         |        |           |           | annotators   | assess | the           | binary | relevance     | judgment |     |
| ---------- | ---------- | ------- | ------ | --------- | --------- | ------------ | ------ | ------------- | ------ | ------------- | -------- | --- |
| itive (TP) | denotes    | when    | LLM    | correctly | predicts  |              |        |               |        |               |          |     |
|            |            |         |        |           |           | of the top-k |        | query–passage |        | pairs, either | relevant |     |
| queries    | with known | answers | within | the       | retrieved |              |        |               |        |               |          |     |
passages, whereas False Negative (FN) denotes (relevance = 1) or non-relevant (relevance = 0).
Foradditionaldetailsindataconstruction,suchas
| when the | model | prediction | is  | incorrect | (i.e., the |         |          |          |     |               |     |        |
| -------- | ----- | ---------- | --- | --------- | ---------- | ------- | -------- | -------- | --- | ------------- | --- | ------ |
|          |       |            |     |           |            | quality | control, | we would |     | like to refer | the | reader |
modelfindsnoanswer)ontherelevantsubset.
toAppendixC.
| EvaluationMetrics. |     | Followingpriorworks(Ad- |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lakha et al., 2024; Chen et al., 2024), we assess Non-relevantSubset. Annotatorsgeneratequeries
LLMrobustnessasabinaryclassificationtaskus- based on certain dataset guidelines, however, oc-
ingtwometrics: (i)hallucinationrateand(ii)error casionallythehuman-generatedqueriescannotbe
rate. First,wecomputethehallucinationrate(in%) answered with the external corpus, which leads
= FP/(FP+TN)whichmeasuresthemodel’sten- to the scenario where none of the top-k passages
dencytohallucinateananswer,whennoansweris arerelevant,i.e.,nonecontainstheanswer. These
availableinallofthepassagesinthenon-relevant querieswithunknownanswersmayoccurdueto
subset. Next, we measure the error rate (in %) the following reasons: (i) queries can be either
= FN/(FN+TP) which measures the model’s genericorspecificforinformationtobepresentin
ability to identify the answer present within the Wikipedia, for e.g. “What does the AC button on
passagesintherelevantsubset. a calculator stand for?” retrieves the Wikipedia

Split/ISO ar bn de en es fa fi fr hi id ja ko ru sw te th yo zh Total
Non-relevantSubset:Querieswithallhuman-judgednon-relevantpassages
Development 228 495 171 289 245 760 98 1,016 1,016 474 211 1,577 268 508 480 323 1,678 1,085 10,922
Test 291 630 218 367 311 968 125 1,294 1294 603 269 2,006 342 646 610 412 2,136 1,381 13,903
RelevantSubset:Querieswithatleastonehuman-judgedrelevantpassage
Development 2,896 411 305 799 648 632 1,271 343 350 960 860 213 1,252 482 828 733 119 393 13,495
Test 1,405 1,130 712 1,790 1,515 1,476 801 711 819 611 1,141 1,417 718 465 793 650 663 920 17,737
Table1: DatasetStatisticsforNoMIRACL.Thedatasetcontainstwosubsetsforall18languages: (i)Non-relevant
subset,wherequeriescontainallhuman-judgednon-relevantpassages. (ii)Relevantsubset,wherequeriescontain
atleastonerelevanthuman-judgedpassage. Bothsubsetsaresplitintodisjointdevelopmentandtestsplits.
pageonCalculator,1 butitdoesnotcontaininfor- (fa),Finnish(fi),French(fr),Hindi(hi),Indone-
mationabouttheACbutton;(ii)spellingmistakes sian(id),Japanese(ja),Korean(ko),Russian(ru),
inquerygeneration. Weconstructthenon-relevant Swahili(sw),Thai(th),Yoruba(yo),Chinese(zh).
subsetwithquerieswithalltop-k passagesjudged From Table 1, we observe an uneven amount
asnon-relevant,i.e.,witharelevanceof0. ofqueriespresentineachlanguage. Toavoidthis
Relevant Subset. Queries with known answers, non-uniformityandbudgetconstraints(seesubsec-
|                        |     |                         |     |     |     | tion | 4.3), | in our | experiments, |     | we limit | the maxi- |
| ---------------------- | --- | ----------------------- | --- | --- | --- | ---- | ----- | ------ | ------------ | --- | -------- | --------- |
| i.e. atleastoneoftop-k |     | retrievedpassagesmarked |     |     |     |      |       |        |              |     |          |           |
mumnumberof250queriesforeachlanguageand
| by the annotator | as relevant | to  | provide | sufficient |     |     |     |     |     |     |     |     |
| ---------------- | ----------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
informationtoanswerthequery. Weconstructthe subset(ifavailable)inNoMIRACL.
| NoMIRACL                 | relevant subset | with      | queries          |     | with at |     |                           |     |     |     |     |     |
| ------------------------ | --------------- | --------- | ---------------- | --- | ------- | --- | ------------------------- | --- | --- | --- | --- | --- |
|                          |                 |           |                  |     |         | 4   | ExperimentalSetup         |     |     |     |     |     |
| leastonerelevantpassage, |                 | i.e.,     | allquery-passage |     |         |     |                           |     |     |     |     |     |
| pairs have               | been judged     | as either | relevant         |     | with a  |     |                           |     |     |     |     |     |
|                          |                 |           |                  |     |         | 4.1 | EvaluationSetupandMetrics |     |     |     |     |     |
relevanceof1ornon-relevantwithrelevanceof0.
|     |     |     |     |     |     | In NoMIRACL, |               |     | we assess | LLM   | relevance | as ei- |
| --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --------- | ----- | --------- | ------ |
|     |     |     |     |     |     | ther         | hallucination |     | or error, | using | an input  | query, |
3.2 FoldCreation
|     |     |     |     |     |     | avanillapromptingtechnique,andtop-k |     |     |     |     |     | (oracle) |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | -------- |
InNoMIRACL,wesplitthenon-relevantandrele-
retrievedandrelevancejudgedpassages.
vantsubsetstoformdisjointdevelopmentandtest
|     |     |     |     |     |     | Retrieved |     | Passages. | For | each | query in | NoMIR- |
| --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --- | ---- | -------- | ------ |
splits. DetailedstatisticscanbefoundinTable1.
|                   |                             |     |     |     |     | ACL,amaximumofk |        |        | =           | 10passagesareretrieved |           |         |
| ----------------- | --------------------------- | --- | --- | --- | --- | --------------- | ------ | ------ | ----------- | ---------------------- | --------- | ------- |
| DevelopmentSplit. | Forqueriespresentintherele- |     |     |     |     |                 |        |        |             |                        |           |         |
|                   |                             |     |     |     |     | and             | judged | by our | annotators. |                        | We follow | the hy- |
vantsubset,wereusethequeriesfromtheMIRACL
|             |              |         |       |     |        | brid | retrieval | setup | in Zhang |     | et al. (2023), | which |
| ----------- | ------------ | ------- | ----- | --- | ------ | ---- | --------- | ----- | -------- | --- | -------------- | ----- |
| development | split (Zhang | et al., | 2023) | for | all 18 |      |           |       |          |     |                |       |
includesthreedifferentmultilingualretrievermod-
| languages. | Forqueriesinthenon-relevantsubset, |     |     |     |     |      |          |     |            |     |           |        |
| ---------- | ---------------------------------- | --- | --- | --- | --- | ---- | -------- | --- | ---------- | --- | --------- | ------ |
|            |                                    |     |     |     |     | els: | (i) BM25 |     | (Robertson | and | Zaragoza, | 2009), |
werandomlysampleadisjointsetcontaining44%
|     |     |     |     |     |     | a lexical |     | retriever, | previously |     | shown to | be robust |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ---------- | --- | -------- | --------- |
ofthequeriesfromthewholenon-relevantsubset.
acrossdomainsandlanguages(Thakuretal.,2021;
| TestSplit. | Forqueriespresentintherelevantsub- |     |     |     |     |                   |     |     |                         |     |     |     |
| ---------- | ---------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | ----------------------- | --- | --- | --- |
|            |                                    |     |     |     |     | Zhangetal.,2022). |     |     | WeusetheBM25implementa- |     |     |     |
set,wereusethequeriesfromtheMIRACLtest-B tionavailableinAnserini(Yangetal.,2018)with
split(Zhangetal.,2023)forall18languages.2
|     |     |     |     |     | For | default | parameters |     | (k  | = 0.9 | and b = | 0.4) and |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --- | ----- | ------- | -------- |
1
queries in the non-relevant subset, we utilize the thecorrespondinglanguage-specificanalyzer. (ii)
| other disjoint | set, containing |     | 56% | of the | queries |     |     |     |     |     |     |     |
| -------------- | --------------- | --- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
mDPR(Karpukhinetal.,2020),adenseretriever,
fromthewholenon-relevantsubset. usingmBERT(Devlinetal.,2018)asthebackbone
andfine-tunedonMSMARCOwiththeTevatron
3.3 LanguagesCoveredandDatasetUsage
|     |     |     |     |     |     | toolkit(Gaoetal.,2023a). |     |     |     | (iii)mColBERT(Khat- |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | ------------------- | --- | --- |
NoMIRACL covers 18 diverse typological lan- tab and Zaharia, 2020), a multi-vector retriever,
guages(Zhangetal.,2023).3 Thelanguagesalong fine-tuned following Khattab and Zaharia (2020)
withtheirISOcodesare: Arabic(ar),Bengali(bn), usingmBERTasbackboneandfine-tunedonMS
German(de),English(en),Spanish(es),Persian
|     |     |     |     |     |     | MARCO. |     | The | top-k passages |     | are ranked | using |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | -------------- | --- | ---------- | ----- |
anensemblefusionbynormalizingandaveraging
1https://en.wikipedia.org/wiki/Calculator
eachmodelscorewithintherangeof[0,1].
2WeleftouttheMIRACLtest-Asplit,asitcontainsqueries
foronly10outofthe18languagesavailable. EvaluationObjective. Inourwork, weevaluate
3NoMIRACLcovers10families(fromNiger-CongotoIndo-
|     |     |     |     |     |     | LLMrelevanceasaresponsestringy |     |     |     |     | inabinary |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --------- | --- |
European)and11scripts(fromLatintoDevanagari)covering
diversityfromtheperspectiveoflinguisticcharacteristics. classification setup. Following prior evaluation

strategiesin(Adlakhaetal.,2024;Yuetal.,2023), I will give you a question and several
weusetheinputqueryq ,avanillaprompttemplate contexts containing information about the
i
|        |       |          |           |     |          |        | question. | Read | the      | contexts | carefully. |           | If  |
| ------ | ----- | -------- | --------- | --- | -------- | ------ | --------- | ---- | -------- | -------- | ---------- | --------- | --- |
| Q, and | a set | of top-k | annotated |     | passages | P . We |           |      |          |          |            |           |     |
|        |       |          |           |     |          | k      | any of    | the  | contexts | answers  | the        | question, |     |
prompttheLLMtoevaluateifq canbeanswered respond as either “Yes, answer is present”
i
| usinganypassageinP |     |     | . TheLLMgeneratesanan- |     |     |     | or “I | don’t | know”: |     |     |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | --- | ----- | ----- | ------ | --- | --- | --- | --- |
k
| sweroutputcontainingeithery |     |     |        | =“I | don’t         | know” |           |         |     |     |     |     |     |
| --------------------------- | --- | --- | ------ | --- | ------------- | ----- | --------- | ------- | --- | --- | --- | --- | --- |
|                             |     |     |        |     |               |       | QUESTION: | {query} |     |     |     |     |     |
| asnegative(N)or“Yes,        |     |     | answer |     | is present”as |       |           |         |     |     |     |     |     |
CONTEXTS:
| positive                                      | (P).     | The output | is  | tagged | “Invalid” | if     |              |          |         |          |       |     |     |
| --------------------------------------------- | -------- | ---------- | --- | ------ | --------- | ------ | ------------ | -------- | ------- | -------- | ----- | --- | --- |
|                                               |          |            |     |        |           |        | [1] {Passage |          | title}: | {Passage | text} |     |     |
| it does                                       | not fall | in either  | one | of the | above.    | Recall |              |          |         |          |       |     |     |
|                                               |          |            |     |        |           |        | [2] {Passage |          | title}: | {Passage | text} |     |     |
| from(§2.1),wecalculatethehallucinationrate(in |          |            |     |        |           |        | ...          |          |         |          |       |     |     |
|                                               |          |            |     |        |           |        | [10]         | {Passage | title}: | {Passage | text} |     |     |
%)=FP/(FP+TN),whichmeasurestheerrorin
rejectinginformationfromnon-relevantpassages
OUTPUT:
andtheerrorrate(in%)=FN/(FN+TP),which
measurestheerrorinidentifyingrelevantpassages Figure4: Vanillazero-shotprompttemplateusedinour
amongstnoisyones. experimentsforLLMhallucinationevaluationforall18
languagesinNoMIRACL.Theinstructionisprovided
4.2 EvaluationModels
inEnglish,similartoAhujaetal.(2023).
| We evaluate |     | eleven | state-of-the-art |     | LLMs | with a |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ---------------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
strongfocusofmultilingualinstructioncapabilities,
andLLAMA-3seriesusingtheAnyScaleAPIser-
| includingbothopenandclosed-sourced. |     |     |     |     |     | Allmodel |          |          |     |           |     |       |          |
| ----------------------------------- | --- | --- | --- | --- | --- | -------- | -------- | -------- | --- | --------- | --- | ----- | -------- |
|                                     |     |     |     |     |     |          | vice. We | maintain |     | a maximum |     | input | sequence |
checkpointscanbefoundinTable5.
lengthof4096tokensforafairevaluationamongst
(1) OpenAI: We include three closed-book allmodels. Wesetalow-temperaturescore=0.1
| LLM | variants: | GPT-3.5-turbo, |     |     | GPT-4, | and |                     |     |         |     |       |       |          |
| --- | --------- | -------------- | --- | --- | ------ | --- | ------------------- | --- | ------- | --- | ----- | ----- | -------- |
|     |           |                |     |     |        |     | for a deterministic |     | output, |     | and a | top-p | sampling |
GPT-4o(OpenAI,2023)usingtheAzureOpenAI
|          |     |          |     |         |     |           | ratio=0.95.       | Weoutputamaximumof50tokens. |     |                           |     |     |     |
| -------- | --- | -------- | --- | ------- | --- | --------- | ----------------- | --------------------------- | --- | ------------------------- | --- | --- | --- |
| service. | (2) | Mistral: | We  | include | two | variants: |                   |                             |     |                           |     |     |     |
|          |     |          |     |         |     |           | VanillaPrompting. |                             |     | Thechoiceofpromptsignifi- |     |     |     |
Mistral-7B-Instruct-v0.3,
| (i) |     |     |     |     | the | latest 7B |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
cantlyinfluencestheperformanceandLLMshave
| instruction-tuned |          | parameter          |       | model | (Jiang | et al.,  |               |         |         |           |             |      |         |
| ----------------- | -------- | ------------------ | ----- | ----- | ------ | -------- | ------------- | ------- | ------- | --------- | ----------- | ---- | ------- |
|                   |          |                    |       |       |        |          | been shown    | brittle | to      | prompting | variations, |      | train-  |
| 2023)             | and (ii) | Mixtral-8x7B-v0.1, |       |       |        | a sparse |               |         |         |           |             |      |         |
|                   |          |                    |       |       |        |          | ing examples, |         | or long | context   | setups      | (Liu | et al., |
| Mixture-of-Expert |          |                    | (MoE) | model | (Jiang | et al.,  |               |         |         |           |             |      |         |
2024). Inourwork,weevaluateallbaselinesusing
| 2024).  | (3) Orca-2: |            | In the | Orca-2 | series    | (Mitra |             |             |     |          |           |     |        |
| ------- | ----------- | ---------- | ------ | ------ | --------- | ------ | ----------- | ----------- | --- | -------- | --------- | --- | ------ |
|         |             |            |        |        |           |        | a zero-shot | monolingual |     | listwise | prompting |     | strat- |
| et al., | 2023),      | we include |        | both   | Orca-2-7B | and    |             |             |     |          |           |     |        |
egy. Weconstructavanillaprompttemplateusing
| Orca-2-13B. |              | (4) Aya: | Aya-101    |            | (Üstün       | et al.,    |                              |          |                            |     |            |               |           |
| ----------- | ------------ | -------- | ---------- | ---------- | ------------ | ---------- | ---------------------------- | -------- | -------------------------- | --- | ---------- | ------------- | --------- |
|             |              |          |            |            |              |            | all top-k                    | (oracle) | passages                   |     | (available | in            | NoMIR-    |
| 2024)       | is a         | recently | introduced |            | multilingual |            |                              |          |                            |     |            |               |           |
|             |              |          |            |            |              |            | ACL) as                      | a list   | of contexts                |     | along      | with          | the input |
| LLM         | containing   | 13B      | parameters |            | and          | trained    |                              |          |                            |     |            |               |           |
|             |              |          |            |            |              |            | query,bothinthesamelanguage. |          |                            |     |            | Weevaluateall |           |
| with 101    | languages    |          | and        | Aya-23-35B |              | finetuned  |                              |          |                            |     |            |               |           |
|             |              |          |            |            |              |            | LLMszero-shot,               |          | aswecannotfitfew-shotexem- |     |            |               |           |
| across      | 23 languages |          | (Aryabumi  |            | et al.,      | 2024). (5) |                              |          |                            |     |            |               |           |
plarsduetoinsufficientcontextlength(maximum
| LLAMA-2:            |        | In the | LLAMA-2              |       | series | (Touvron  |                        |             |     |                          |            |     |          |
| ------------------- | ------ | ------ | -------------------- | ----- | ------ | --------- | ---------------------- | ----------- | --- | ------------------------ | ---------- | --- | -------- |
|                     |        |        |                      |       |        |           | of4096sequencelength). |             |     | Ourtemplateprovides      |            |     |          |
| et al.,             | 2023), | we     | include              | three | chat   | variants: |                        |             |     |                          |            |     |          |
|                     |        |        |                      |       |        |           | a short                | description | in  | English                  | describing |     | the task |
| Llama-2-7b-chat-hf, |        |        | Llama-2-13b-chat-hf, |       |        |           |                        |             |     |                          |            |     |          |
|                     |        |        |                      |       |        |           | (Ahujaetal.,2023).     |             |     | Ourvanillaprompttemplate |            |     |          |
Llama-2-70b-chat-hf
| and |     |     |     | instruction |     | tuned |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
usedinourexperimentsisshowninFigure4.
| chat models.    |         | (6)   | LLAMA-3: |     | Following | up      |                                        |        |         |     |       |              |     |
| --------------- | ------- | ----- | -------- | --- | --------- | ------- | -------------------------------------- | ------ | ------- | --- | ----- | ------------ | --- |
|                 |         |       |          |     |           |         | Reducing                               | Costs. | Running |     | GPT-4 | is expensive |     |
| on the          | LLAMA-2 |       | series,  | we  | include   | both    |                                        |        |         |     |       |              |     |
|                 |         |       |          |     |           |         | andLLAMA-3-70Bisratherslowatinference. |        |         |     |       |              | For |
| the instruction |         | tuned | models   |     | (Dubey    | et al., |                                        |        |         |     |       |              |     |
longcontextsandlow-resourcelanguages,thecosts
| 2024): | Meta-Llama-3-8B-Instruct |     |     |     |     | and |          |           |     |           |     |         |        |
| ------ | ------------------------ | --- | --- | --- | --- | --- | -------- | --------- | --- | --------- | --- | ------- | ------ |
|        |                          |     |     |     |     |     | can even | multiply. |     | To limit, | we  | did not | exceed |
Meta-Llama-3-70B-Instruct.
|                          |     |     |     |     |     |     | our prompt | above       | 4096 | tokens.      | To          | effectively | fit       |
| ------------------------ | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- | ------------ | ----------- | ----------- | --------- |
| 4.3 ExperimentalSettings |     |     |     |     |     |     | k =        | 10          |      |              |             |             |           |
|                          |     |     |     |     |     |     | all        | passages    |      | within       | the vanilla | zero-shot   |           |
|                          |     |     |     |     |     |     | prompt,    | we truncate |      | each passage |             | to use      | the first |
WeexecutethegenerationofGPT-4o,GPT-4,and
|     |     |     |     |     |     |     | 375 tokens. | Next, | due | to budget |     | constraints, | we  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | --------- | --- | ------------ | --- |
GPT-3.5-turbo,usingtheOpenAIservice(APIver-
sion2023-05-15)deployedonMicrosoftAzure4 keepourevaluationtoamaximumof250randomly
sampledqueriesforalllanguagesinbothNoMIR-
4WecomparedAzureAPIwithOpenAIAPIacrossfourlan-
guagesinNoMIRACLandobservednonoticeabledifference betweendifferentGPT-4APIversionproviders.

100%
80%
60%
40%
20%
0%
ar bn de en es fa fr fi hi id ja ko ru sw te th yo zh
)%
ni(
etar
noitanicullaH
GPT-4 Mixtral-7x8B Orca-2-13B Aya-23-35B LLAMA-2-13B LLAMA-3-8B
Figure5: Hallucinationrate(in%)=FP/(FP+TN)onthenon-relevantsubset(F)inNoMIRACLtestsplit. The
non-relevantsubsetcontainsquerieswithnoknownanswers,i.e.,alltop-k(wherek =10)passagesarejudgedby
ahumanannotatorasnon-relevant. AmajorityofLLMs(exceptMistral)hallucinateonthenon-relevantsubset.
Lowerthehallucinationrateisbetter. Thebestmodelineachcategoryisplotted(seeFigure8forallmodels).
80%
60%
40%
20%
0%
ar bn de en es fa fr fi hi id ja ko ru sw te th yo zh
)%
ni(
etar
rorrE
GPT-4o Mistral-7B Orca-2-13B Aya-23-35B LLAMA-2-70B LLAMA-3-70B
Figure6: Errorrate(in%)=FN/(FN+TP)ontherelevantsubset(T)inNoMIRACLtestsplit. Therelevant
subsetcontainsquerieswithknownanswers,i.e.,atleastoneofthetop-k(wherek =10)passagesarejudgedbya
humanannotatorasrelevant. Onaverage,amajorityofLLMs(exceptMistralandAya-101)havealowererrorrate
byaccuratelyidentifyingtheanswer. Lowertheerrorrateisbetter. Thebestmodelineachcategoryisplotted(see
Figure9forallmodels).
ACL relevant and non-relevant split. We end up lightsthechallengeofidentifyingnon-relevantpas-
providing≈20KAPIcallsproducinganexpense sages. LLAMA-2, Orca-2, andAya-101perform
of$1,474(inUSD)includingmiscellaneouscosts. much worse on average across all languages, by
achieving a hallucination rate of more than 80%.
5 ExperimentalResults
WehypothesizethatLLMsperformpoorlytoiden-
WediscussourLLMrobustnessevaluationresults tifynon-relevantpassagesastheyarehighlysimilar
using the hallucination rate on the non-relevant tothequery,butdonotcontaintheexactanswer.
subset in (§5.1) and using the error rate on the Overall, the lowest hallucination rates are ob-
relevantsubsetin(§5.2),andcompareoverallboth served in Swahili and Yoruba. We hypothesize
therelevantandnon-relevantcapacitiesin(§5.3). that queries in low-resource languages (smaller
Wikipedia corpus) contain retrieved information,
5.1 NoMIRACLNon-relevantSubset
likelytobenon-relevant(easiernegative),thereby
Figure5showshallucinationratesontheNoMIR- makingiteasierfortheLLMtojudgeas“Idon’t
ACL non-relevant subset for a maximum of 250 know”. GPT-3.5(cf.Figure8)isobservedwiththe
queries evaluated (each language) on all 18 lan- highestdeviationacrosslanguageswithahallucina-
guages for best LLM in each category (for all tionrateaslowas25.2%onSwahili(sw)to95.2%
modelresults,pleaserefertoFigure8). Ourfind- on Bengali (bn). Overall, all LLMs are found to
ingsindicatethatallLLMs(exceptMistral)halluci- performpoorlyonNoMIRACLnon-relevantsub-
natethatananswerispresentacrossalllanguages, set, indicating our dataset is very challenging in
therebyindicatingtheirpoorabilitytoabstainfrom robustnessevaluationforLLMs.
answering. On average, the lowest hallucination
5.2 NoMIRACLRelevantSubset
rate of 17.4% is observed by Mixtral-7x8B, fol-
lowedbyLLAMA-3-8B-Instructwith26.8%. GPT- Figure 6 shows error rates on NoMIRACL rele-
4achievesa35.5%hallucinationrate,whichhigh- vant subset for a maximum of 250 queries (each

| language) | on  | 18 languages |     | for best | LLM | in each |     |     |        |        |     |         |     |
| --------- | --- | ------------ | --- | -------- | --- | ------- | --- | --- | ------ | ------ | --- | ------- | --- |
|           |     |              |     |          |     |         |     |     | OpenAI | Orca-2 |     | LLAMA-2 |     |
categoryOurfindingsindicatethatallLLMs(ex-
|     |     |     |     |     |     |     | tnaveleR LCARIMoN no )% ni( ycaruccA |     | Mistral | Aya |     | LLAMA-3 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | ------- | --- | --- | ------- | --- |
ceptMistral)identifytheanswerpresentwithinthe
100
|             |          |      |           |         |          |       |     |  LLAMA-2-70B |             |  GPT-4o     |              |     |     |
| ----------- | -------- | ---- | --------- | ------- | -------- | ----- | --- | ------------ | ----------- | ----------- | ------------ | --- | --- |
| relevant    | passage. | On   | average,  | Aya-101 | achieves |       |     |              |             |             |              |     |     |
|             |          |      |           |         |          |       |     |              |             |  GPT-3.5    |  GPT-4       |     |     |
| the highest | error    | rate | of 62.5%. | The     | lowest   | error |     |              |  Orca-2-13B |             |              |     |     |
|             |          |      |           |         |          |       |     | 80           |             |  Aya-23-35B |  LLAMA-3-70B |     |     |
 Orca-2-7B
rates are observed by LLAMA-2-70B and GPT-  LLAMA-2-7B  Mistral-7B
4o which are lower than 10%. Overall, Aya-101, 60  LLAMA-2-13B  Mixtral-7x8B
 LLAMA-3-8B
Mixtral-7x8B,andLLAMA-3-8Bperformworse
| on average | by  | observing |     | more than | a 40% | error |     | 40  |  Aya-101 |     |     |     |     |
| ---------- | --- | --------- | --- | --------- | ----- | ----- | --- | --- | -------- | --- | --- | --- | --- |
rate. Overall,LLMs(exceptMistralandAya-101)
| performwellanddonotsufferfromerrorsiniden- |     |     |     |     |     |     |     | 20  |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tifyinganswersintheNoMIRACLrelevantsubset.
0
|     |     |     |     |     |     |     |     | 0   | 20  | 40  | 60  | 80  | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.3 NoMIRACLOverallComparison Accuracy (in %) on NoMIRACL Non-Relevant
| A robust | LLM | should | be  | able to | identify | the an- |     |     |     |     |     |     |     |
| -------- | --- | ------ | --- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Figure7:Plotmeasuringaveragemodelaccuracyacross
swercapturedwithinretrievedpassagesintherele- alllanguagesonrelevant(y-axis)andnon-relevantsub-
vantsubsetandabstainfromansweringwhennone set(x-axis)inNoMIRACL.Performancetowardsthe
of the retrieved passages contain the answer in top-rightcorner(denotedbythearrow)isbetter.
| thenon-relevantsubset. |     |     | Tomeasureperformance |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
across both dimensions in NoMIRACL, we plot Non-relevant Subset. As shown in Table 2
the average model accuracy across both the non- (above),weobserveauniformdistributionofthe
| relevant | (x-axis) | and | relevant | subset | (y-axis) | for |     |     |     |     |     |     |     |
| -------- | -------- | --- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
hallucinationpatternoffailedsamplesforamajor-
all tested models in Figure 7. Overall, LLMs po- ityofLLMsbyanswering“Yes,answerispresent”
sitionedinthetop-rightcornerprovideanoptimal withorwithoutadditionalexplanation. LLMssuch
| performanceonbothsubsets. |     |     |     | AmajorityofLLMs |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
asLLAMA-2-7BandLLAMA-2-13Bsufferfrom
| (such as | LLAMA-2, |     | and | Orca-2) | in the | top-left |                |     |     |                 |     |              |     |
| -------- | -------- | --- | --- | ------- | ------ | -------- | -------------- | --- | --- | --------------- | --- | ------------ | --- |
|          |          |     |     |         |        |          | hallucinations |     | by  | often repeating |     | the question | or  |
corner perform well on the relevant subset, how- instructionintheirgenerationoutput. Mistral-7B
ever, hallucinate and struggle to perform well on interestinglyalwaysprovidesarationaleorexpla-
thenon-relevantsubset,indicatingtheirinabilityto
nationintheirmodelresponse,whereasAya-101,
accuratelyjudgenon-relevantpassages. uses implicit memory heavily to directly provide
Ontheotherhand,MistralandLLAMA-3suffer an answer instead of grounding the answer from
less from hallucination on the non-relevant sub- withintheretrievedpassages. Lastly,modelssuch
| set but | observe | a higher | error | rate | (over 40%) | on  |     |     |     |     |     |     |     |
| ------- | ------- | -------- | ----- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
asOrca-2-7Btendtochangetheoutputgeneration
the relevant subset, indicating they are not confi- styleandoftenusesynonymssuchas“No,answer
dentinidentifyingpassagescontainingtheanswer. isnotpresent”insteadof“Idon’tknow”.
Aya-101isunabletoperformwellineitherofthe
|     |     |     |     |     |     |     | Relevant |     | Subset. | As shown | in  | Table 2 | (below), |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | -------- | --- | ------- | -------- |
subsets. GPT-4providesagoodtradeoffbalancing
similartothenon-relevantsubset,weobserveauni-
bothalowhallucinationanderrorrateonNoMIR-
|     |     |     |     |     |     |     | formdistributionofaccurateLLMresponses. |     |     |     |     |     | Inter- |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ------ |
ACLrelevantandnon-relevantsubsets,howeveris estingly,GPT-4andOrca-2-13Boverallonlypro-
expensivetocomputeatscaleforinference.
videasingleoutputclassificationtoken,whereas
modelssuchasGPT-3.5orMixtral-8x7Bprovide
6 EmpiricalAnalysis
|                  |     |            |     |              |          |     | anadditionalrationaleorexplanation. |              |     |                    |     | Similarto    |     |
| ---------------- | --- | ---------- | --- | ------------ | -------- | --- | ----------------------------------- | ------------ | --- | ------------------ | --- | ------------ | --- |
|                  |     |            |     |              |          |     | the                                 | non-relevant |     | subset, LLAMA-2-7B |     | and          | 13B |
| In this section, |     | we conduct |     | an empirical | analysis |     |                                     |              |     |                    |     |              |     |
|                  |     |            |     |              |          |     | models                              | repeat       | the | instruction        | in  | their output | and |
ofLLMoutputs,withboththenon-relevantsubset
Aya-101sometimesusesimplicitmemory.
(containinghallucinations)andtherelevantsubset
| (containingerrors). |     | Weconductourablationstudy |     |     |     |     |     |                |     |     |     |     |     |
| ------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
|                     |     |                           |     |     |     |     | 7   | FurtherStudies |     |     |     |     |     |
ontheEnglish(en)subsetinNoMIRACL.Wecat-
egorizeeachLLMoutputpatternaseitherpositive Prompt Optimization. Prompting is crucial in
oraccurate(highlightedin green),unabletounder- handlingtherobustnessevaluationofmultilingual-
standinstruction(highlightedin orange),oreither focused LLMs. Techniques such as Chain-of-
ahallucinationorerror(highlightedin red). Thought (CoT) (Wei et al., 2022) or algorithmi-

OpenAI Mistral Orca-2 Aya LLAMA-2
GPT-4 GPT-3.5 8x7B 7B 13B 7B Aya-101 70B 13B 7B
Empiricalresultsonthenon-relevantsubset:Querieswithallhuman-judgednon-relevantpassages
(i)Perfectlyanswers“Idon’tknow” 56.8% 54.8% 67.2% 1.6% 3.2% 9.2% 15.6% 0.0% 0.0% 0.8%
(ii)“Idon’tknow”withexplanation 0.0% 0.0% 3.6% 88.4% 0.0% 2.0% 0.0% 0.0% 0.0% 0.0%
(iii)Usesasynonymof“Idon’tknow” 0.4% 0.0% 1.6% 1.2% 6.0% 7.6% 0.0% 0.4% 0.0% 2.4%
(iv)Refusestoanswer 0.4% 0.8% 0.0% 0.8% 3.2% 0.0% 6.4% 0.0% 0.0% 0.0%
(v)Repeatsquestionorinstruction 0.0% 0.0% 0.0% 0.0% 0.0% 3.2% 0.0% 2.0% 64.8% 30.8%
(vi)Conversation 0.0% 0.0% 0.4% 0.0% 0.0% 0.4% 0.0% 0.0% 0.0% 0.4%
(vii)Answers"Yes"w.orw.o.explanation 42.4% 44.4% 27.2% 8.0% 87.6% 68.4% 67.2% 97.6% 34.8% 65.6%
(viii)Usesimplicitmemorytoanswer 0.0% 0.0% 0.0% 0.0% 0.0% 8.8% 10.8% 0.0% 0.0% 0.0%
Empiricalresultsontherelevantsubset:Querieswithatleastonehuman-judgedrelevantpassage
(i)Perfectlyanswers“Yes,answerispresent” 94.8% 45.2% 22.8% 5.2% 97.2% 71.2% 51.6% 1.2% 3.6% 7.2%
(ii)"Yes,answerispresent"withexplanation 0.0% 46.0% 56.0% 31.6% 0.8% 11.2% 0.0% 98.8% 46.8% 63.2%
(iii)Refusestoanswer 0.4% 0.8% 0.0% 0.0% 0.0% 0.0% 1.2% 0.0% 0.0% 0.0%
(iv)Repeatsquestionorinstruction 0.0% 0.0% 0.4% 0.0% 0.0% 0.4% 0.0% 0.0% 48.8% 24.8%
(v)Conversation 0.0% 0.0% 0.0% 0.0% 0.0% 0.0% 0.0% 0.0% 0.0% 1.6%
(vi)Answers"No"w.orw.o.explanation 4.8% 8.0% 20.8% 60.8% 0.8% 2.8% 4.0% 0.0% 0.0% 1.2%
(vii)Usesimplicitmemorytoanswer 0.0% 0.0% 0.0% 2.4% 1.2% 14.4% 42.0% 0.0% 0.0% 0.4%
Table2: EmpiricalresultsonthecompleteNoMIRACLEnglish(en)non-relevant(above)andrelevant(below)
subsets. Theanalysisisbracketedintothreecategories,where green categorydenotesanaccurateresponse, orange
denoteslimitationsinunderstandingtheinstructionand red denotesmodelhallucinationorerrorrespectively.
cally optimizing prompts using DSPy (Khattab (CoN;Yuetal.,2023),weinvestigatethefollowing
etal.,2023)highlightthenecessityofpromptop- researchquestion: Doesfine-tuningontheNoMIR-
timization. Although optimizing for the prompt ACLdevelopmentsethelpincreaserobustness?
iscertainlychallengingandexpensivetoevaluate We experiment with two open-sourced LLMs:
all LLMs across 18 languages relevant and non- Mistral-7B and LLAMA-3 (8B). We Supervised
relevantsubsets,weexperimentwiththreelistwise Fine-Tune(SFT)LoRAadapters(Huetal.,2022)
variations techniques inspired by Thomas et al. onthedevelopmentsetofNoMIRACLforall18
(2024). The prompt template changes are listed languages(randomlysampled90%train,10%de-
inFigure10: (i)role,wehighlighttheroleofLLM velopment)using4-A6000GPUseachcontaining
asanevaluatorwithinthepromptatthebeginning, 48GBRAMwithPEFT.5 Ourhyperparameterset-
(ii) repeat, we repeat the task instructions at the tingsarelistedinTable6. Wewereunabletofine-
end of the prompt to remind the LLM, and (iii) tune larger models (greater than 8B parameters)
explanation, we ask the LLM model to provide duetocomputationalbudgetrestrictions.
a step-by-step explanation and then answer and As shown in Table 4, we observe LLAMA-3
require400outputtokenstofitboththeLLMrea- (8B) to be quite unstable after SFT. Fine-tuning
soningandtheanswer. helps to reduce the error rate of LLAMA-3 (8B)
WeevaluateMistral-7Bwiththreepromptvaria- (animprovementof10.6%)butcanhurtitsperfor-
tionsindependentlyonNoMIRACL.Thecomplete manceonthehallucinationrate(dropupto17.9%).
resultsarelistedinTable3. Onaverage,bothrole ForafewlanguagesmentionedinTable7suchas
and repeat techniques help reduce the error rate Arabic(ar)theLLMalwaysoutputs“Yes,answer
in the NoMIRACL relevant subset by 6.3% and ispresent”,whereasforBengali(bn)heavilyrelies
15.2%butoverallincreasethehallucinationrateby on“Idon’tknow”. Ontheotherhand,SFTdeterio-
8.7%and15.9%respectively. Ontheotherhand, ratesMistral-7Bonbothrelevantandnon-relevant
promptingwithexplanationdecreasesthehalluci- datasets. Overall,wedemonstrateSFTistrickyand
nationrateby9.7%butincreasestheerrorrateby carefulexperimentationisrequiredtoachievethe
8.3%. These results show that prompting is user bestoutoffine-tuningontheNoMIRACLdevelop-
dependent,theuserwillberequiredtochoosetheir mentsubsetforabinaryclassificationtaskoutput
technique depending on whether they wish to be (“Yes,answerispresent”or“Idon’tknow”).
better on the non-relevant subset by reducing the
8 RelatedWork
hallucinationrateortherelevantsubsetbyreducing
theerrorrate. Retrieval-Augmented Generation. The knowl-
edge stored in a large language model (LLM) is
Fine-tuningonNoMIRACL.Inthissection,fol-
commonly outdated (He et al., 2023), and prone
lowingpriorworkssuchasChain-of-Verification
(CoVe;Dhuliawalaetal.,2024)orChain-of-Noting 5https://github.com/huggingface/alignment-handbook

|     |     | ar bn | de  | en es | fa fr | fi hi | id  | ja ko | ru sw | te  | th yo | zh Avg. |
| --- | --- | ----- | --- | ----- | ----- | ----- | --- | ----- | ----- | --- | ----- | ------- |
HallucinationRates(in%)onNoMIRACLtestsplit(non-relevantsubset)
Original 40.0 63.2 38.2 42.8 17.2 52.4 47.6 16.1 39.6 30.8 44.4 28.8 41.6 14.8 74.0 58.8 23.6 45.2 40.0
(+Role) 35.6 60.0 53.5 62.4 40.4 38.0 71.2 29.8 38.4 49.2 59.2 41.2 55.6 21.2 72.0 54.4 32.4 62.8 48.7
(+Repeat) 47.2 72.4 56.7 50.8 35.2 69.2 70.0 50.0 49.6 48.8 65.2 48.4 56.0 35.2 78.4 72.0 43.6 58.4 55.9
(+Explanation) 28.0 33.6 30.4 34.8 16.8 39.6 42.4 31.5 18.0 27.2 32.8 26.8 31.6 22.8 36.4 34.0 27.2 31.6 30.3
ErrorRates(in%)onNoMIRACLtestsplit(relevantsubset)
Original 14.4 20.4 21.6 8.0 28.0 22.4 15.6 38.0 30.8 43.6 16.0 30.0 18.0 57.6 17.6 13.6 50.0 13.2 25.5
(+Role) 15.2 23.6 10.0 3.2 14.4 23.2 7.2 29.2 25.2 32.8 9.6 21.6 10.8 47.2 17.6 17.2 33.8 4.4 19.2
(+Repeat) 8.4 12.4 9.2 5.2 12.4 4.8 5.6 6.0 16.4 16.8 1.6 12.0 6.8 22.8 14.0 6.0 21.6 3.6 10.3
(+Explanation) 28.8 39.6 26.0 16.8 35.6 35.6 20.0 32.0 46.8 46.8 24.4 33.6 24.8 50.4 48.8 31.2 48.0 18.8 33.8
Table3: HallucinationanderrorratesontheNoMIRACLtestsplit(non-relevantandrelevantsubsets)withthree
typesofpromptingtechniquesonMistral-7B(v0.3). ThechangesintheprompttemplatearelistedinFigure10.
|       |     |     |     |        |       |     | sages in     | QA datasets                  | such | as  | NQ (Kwiatkowski |     |
| ----- | --- | --- | --- | ------ | ----- | --- | ------------ | ---------------------------- | ---- | --- | --------------- | --- |
| Model |     |     |     | w/oSFT | w/SFT |     |              |                              |      |     |                 |     |
|       |     |     |     |        |       |     | etal.,2019). | KnowingthatpromptingLLMswith |      |     |                 |     |
Non-RelevantSubset:HallucinationRates(in%)
non-relevantdatacanresultinmisguidedresponses,
| Meta-Llama-3-8B-Instruct |     |     |     | 26.8 | 44.7(–17.9) |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Yuetal.(2023)recentlyintroducedanewprompt-
| Mistral-Instruct-7B-v0.3 |     |     |     | 40.0 | 44.3(–4.3) |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ingtechnique,Chain-of-Noting(CON)andYoran
RelevantSubset:ErrorRates(in%)
|                          |     |     |     |      |             |     | et al. (2024) | fine-tuned |     | the LLM | explicitly, | both |
| ------------------------ | --- | --- | --- | ---- | ----------- | --- | ------------- | ---------- | --- | ------- | ----------- | ---- |
| Meta-Llama-3-8B-Instruct |     |     |     | 45.3 | 34.7(+10.6) |     |               |            |     |         |             |      |
Mistral-Instruct-7B-v0.3 25.5 46.1(–20.6) aimedtoimproveLLMrobustnessinRAGwhen
non-relevantinformationisprovided.
Table 4: Supervised fine-tuning on the NoMIRACL Related Datasets. Datasets focused on address-
| development | split | with | Llama-3 | (8B) | and Mistral-7B |     |     |     |     |     |     |     |
| ----------- | ----- | ---- | ------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
ingunanswerablequeriessuchasSQuAD2.0(Ra-
(v0.3)LLMs.
jpurkaretal.,2018)werecreatedadversariallyto
|                   |         |     |            |           |        |         | look similar | to             | datasets | with | answerable | queries. |
| ----------------- | ------- | --- | ---------- | --------- | ------ | ------- | ------------ | -------------- | -------- | ---- | ---------- | -------- |
| to hallucinations |         | by  | generating | factually |        | incor-  |              |                |          |      |            |          |
|                   |         |     |            |           |        |         | Similarly,   | Conversational |          | QA   | datasets   | such as  |
| rect output       | (Maynez |     | et al.,    | 2020;     | Raunak | et al., |              |                |          |      |            |          |
CoQA(Reddyetal.,2019)andQuAC(Choietal.,
| 2021). | By grounding |     | on  | external | knowledge, | a   |            |         |              |     |          |        |
| ------ | ------------ | --- | --- | -------- | ---------- | --- | ---------- | ------- | ------------ | --- | -------- | ------ |
|        |              |     |     |          |            |     | 2018) also | contain | unanswerable |     | queries. | A con- |
retrieval-augmentedLLMcangeneratebetterand
currentworkproposesRGB,aRAGbenchmarkto
moretrustworthyoutput(Guuetal.,2020;Lewis
evaluateLLMrobustnessinEnglishandChinese
| et al., 2020; | Izacard |     | and Grave, | 2021; | Borgeaud |     |     |     |     |     |     |     |
| ------------- | ------- | --- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
(Chenetal.,2024).
| etal.,2022).                                  | Retrieval-augmentedgenerationhas |     |     |     |     |     |              |     |     |     |     |     |
| --------------------------------------------- | -------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
| achievedremarkableresultsinvarioustaskssuchas |                                  |     |     |     |     |     | 9 Conclusion |     |     |     |     |     |
open-domainquestionanswering(ODQA)(Lewis
WeintroduceNoMIRACL,amultilingualhuman-
etal.,2020;IzacardandGrave,2021;Trivedietal.,
|     |     |     |     |     |     |     | labeleddatasetforrelevanceassessmentof |     |     |     |     | LLM |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
2023),argumentextraction(DuandJi,2022)and
robustnessasabinaryrelevanceidentificationtask
| code generation |     | (Zhou | et  | al., 2023). | Real-world |     |                |     |                                |     |     |     |
| --------------- | --- | ----- | --- | ----------- | ---------- | --- | -------------- | --- | ------------------------------ | --- | --- | --- |
|                 |     |       |     |             |            |     | in18languages. |     | Ourmultilingualdatasetishuman- |     |     |     |
productssuchasBingSearchandLangChainhave
annotatedandconstructedwith31nativespeakers.
incorporatedRAGapplications.
|     |     |     |     |     |     |     | We provide | two | subsets | in NoMIRACL, |     | the non- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ------------ | --- | -------- |
LLM Evaluation. Prior work explores adding relevant subset, where queries contain all judged
perturbationinpassagesandshowsthatLLMper- non-relevant passages, and the relevant subset,
formancecanbeinfluencedwhenexposedtodif- wherequeriescontainatleastonerelevantjudged
ferenttasks,suchasquestionanswering(QA) (Jia passage to measure the hallucination on the non-
and Liang, 2017; Petroni et al., 2020; Creswell relevantanderrorontherelevantsubset. Ourex-
etal.,2023),logicalreasoning (Misraetal.,2023) perimentalresultsindicatethatexistingLLMsare
or arithmetic reasoning (Shi et al., 2023; Kumar not robust, as we observe challenges in LLM ro-
etal.,2021). Inexaminingcontrollabilityandro- bustness in either hallucination or error. GPT-4
bustness,Lietal.(2023)observesthatLLMsdis- achievesthebestmodelandperformancetradeoff
regardcontextualinformation,showingthatLLM acrossbothsubsets. NoMIRACLcanfacilitatere-
outputcanbeinfluencedbynon-relevantcontext. searchinunderstandingtowhichextentLLMstend
Adlakhaetal.(2024)observescomplementaryre- tohallucinate,ultimatelypavingthewayforbuild-
sultsfromourwork,wheretheyobserveLLMcan ingmoreeffectiveandrobustmultilingual-focused
| beratherfaithfulwhenprovidednon-relevantpas- |     |     |     |     |     |     | LLMsinthefuture. |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |

10 Limitations
|     |     |     |     |     |     | providing                  | the necessary |     | Microsoft |                 | Azure | credits |
| --- | --- | --- | --- | --- | --- | -------------------------- | ------------- | --- | --------- | --------------- | ----- | ------- |
|     |     |     |     |     |     | forevaluatingOpenAImodels. |               |     |           | Thisresearchwas |       |         |
NoMIRACLisnotperfectandlikeotherdatasets
supportedinpartbytheNaturalSciencesandEn-
| havelimitations. |     | Wedescribeourlimitationsbelow |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gineeringResearchCouncil(NSERC)ofCanada,
andkeepitasfutureworktoimproveourdataset.
agiftfromHuawei,andCloudTPUsupportfrom
1. HumanErrorsinDatasetConstruction. Our Google’sTPUResearchCloud(TRC).
| dataset                         | has been | fully | constructed | using       | humans, |     |     |     |     |     |     |     |
| ------------------------------- | -------- | ----- | ----------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| therebyitmaycontainhumanerrors. |          |       |             | Weconducted |         |     |     |     |     |     |     |     |
References
additionalqualitychecksonasubsetoftheNoMIR-
ACL dataset to validate its question quality and VaibhavAdlakha,ParishadBehnamGhader,XingHan
|     |     |     |     |     |     | Lu, Nicholas | Meade, |     | and Siva | Reddy. | 2024. | Eval- |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | --- | -------- | ------ | ----- | ----- |
relevancejudgmentasexplainedinAppendixC.
|               |     |        |        |       |             | uating correctness |        | and | faithfulness |            | of instruction- |        |
| ------------- | --- | ------ | ------ | ----- | ----------- | ------------------ | ------ | --- | ------------ | ---------- | --------------- | ------ |
| 2. Evaluation |     | Setup. | In our | work, | we evaluate |                    |        |     |              |            |                 |        |
|               |     |        |        |       |             | following          | models | for | question     | answering. |                 | Trans. |
whether a passage is relevant or non-relevant for Assoc.Comput.Linguistics,12:681–699.
agivenquery,insteadofevaluatingactualanswer
KabirAhuja,HarshitaDiddee,RishavHada,Millicent
| spans. | Reliable | and accurate | answers |     | for a given |     |     |     |     |     |     |     |
| ------ | -------- | ------------ | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Ochieng,KrithikaRamesh,PrachiJain,AkshayUt-
query require domain experts as annotators. An- tamaNambi,TanujaGanu,SameerSegal,Mohamed
|     |     |     |     |     |     | Ahmed, | Kalika | Bali, | and Sunayana |     | Sitaram. | 2023. |
| --- | --- | --- | --- | --- | --- | ------ | ------ | ----- | ------------ | --- | -------- | ----- |
notatorscanpotentiallyhighlightshortextractive
|     |     |     |     |     |     | MEGA:multilingualevaluationofgenerativeAI. |     |     |     |     |     | In  |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
spansofanswerswithinrelevantpassages,however,
|     |     |     |     |     |     | Proceedings | of  | the 2023 | Conference |     | on  | Empirical |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ---------- | --- | --- | --------- |
non-extractivequeriescaneithercontainmultiple
MethodsinNaturalLanguageProcessing,EMNLP
answersoralong-formanswer,makingitdifficult 2023,Singapore,December6-10,2023,pages4232–
tohighlightarelevantanswerspan. Therefore,for 4267.AssociationforComputationalLinguistics.
| NoMIRACL, |     | we focus | on evaluating |     | top-k pas- |                  |     |      |       |        |     |           |
| --------- | --- | -------- | ------------- | --- | ---------- | ---------------- | --- | ---- | ----- | ------ | --- | --------- |
|           |     |          |               |     |            | Viraat Aryabumi, |     | John | Dang, | Dwarak |     | Talupuru, |
sagesasinformationcontexts,whicharejudgedfor Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
|     |     |     |     |     |     | Venkitesh, | Madeline |     | Smith, | Jon | Ander | Campos, |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------ | --- | ----- | ------- |
theirrelevancybyadataannotator.
|                        |     |     |                     |     |     | Yi Chern | Tan, | Kelly | Marchisio, | Max | Bartolo, | Se- |
| ---------------------- | --- | --- | ------------------- | --- | --- | -------- | ---- | ----- | ---------- | --- | -------- | --- |
| 3. LimitedtoWikipedia. |     |     | NoMIRACLiscurrently |     |     |          |      |       |            |     |          |     |
bastianRuder,AcyrLocatelli,JuliaKreutzer,Nick
developedusinglanguage-specificWikipediaasthe Frosst, Aidan N. Gomez, Phil Blunsom, Marzieh
corpora. Wikipediamaynotbetheidealchoicefor Fadaee,AhmetÜstün,andSaraHooker.2024. Aya
|                                        |     |     |     |     |        | 23: Open | weight | releases |     | to further | multilingual |     |
| -------------------------------------- | --- | --- | --- | --- | ------ | -------- | ------ | -------- | --- | ---------- | ------------ | --- |
| real-worldapplicationsacrosslanguages. |     |     |     |     | Forex- |          |        |          |     |            |              |     |
CoRR,abs/2405.15032.
progress.
ample,theEnglishBEIRbenchmark(Thakuretal.,
SebastianBorgeaud,ArthurMensch,JordanHoffmann,
2021)includesdiversitywithinitsdomains(allEn-
glish)andcontainsmorereal-worlddomainssuch TrevorCai,ElizaRutherford,KatieMillican,George
|                |     |                              |     |     |     | vandenDriessche, |     | Jean-BaptisteLespiau, |     |     |     | Bogdan |
| -------------- | --- | ---------------------------- | --- | --- | --- | ---------------- | --- | --------------------- | --- | --- | --- | ------ |
| asMedical,etc. |     | However,wekeepitasfuturework |     |     |     |                  |     |                       |     |     |     |        |
Damoc,AidanClark,DiegodeLasCasas,Aurelia
toextendNoMIRACLtodiversedomainsforthe Guy, Jacob Menick, Roman Ring, Tom Hennigan,
following reasons: (i) scarcity of corpora across SaffronHuang,LorenMaggiore,ChrisJones,Albin
languages: for low-resource languages such as Cassirer, AndyBrock, MichelaPaganini, Geoffrey
|     |     |     |     |     |     | Irving, | Oriol | Vinyals, | Simon | Osindero, |     | Karen Si- |
| --- | --- | --- | --- | --- | --- | ------- | ----- | -------- | ----- | --------- | --- | --------- |
BengaliorYoruba,findingasuitablelargeenough
monyan,JackW.Rae,ErichElsen,andLaurentSifre.
text corpora is difficult with limited choices. (ii) 2022. Improvinglanguagemodelsbyretrievingfrom
no uniformity across domains: certain European trillionsoftokens. InInternationalConferenceon
MachineLearning,ICML2022,17-23July2022,Bal-
| languages | have | more | legal domain | corpora | avail- |     |     |     |     |     |     |     |
| --------- | ---- | ---- | ------------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
timore,Maryland,USA,volume162ofProceedings
able,whereasnewsarticlesforAfricanlanguages.
|     |     |     |     |     |     | of Machine | Learning |     | Research, | pages | 2206–2240. |     |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | --------- | ----- | ---------- | --- |
Thiswillintroducenon-uniformityininformation
PMLR.
| acrosslanguages. |     | (iii)limitedbudget: |     |     | constructing |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
TomB.Brown,BenjaminMann,NickRyder,Melanie
| NoMIRACL |     | was expensive | involving |     | several an- |          |       |         |          |           |     |        |
| -------- | --- | ------------- | --------- | --- | ----------- | -------- | ----- | ------- | -------- | --------- | --- | ------ |
|          |     |               |           |     |             | Subbiah, | Jared | Kaplan, | Prafulla | Dhariwal, |     | Arvind |
notatorsinvolvedforabout4–6months. Extending Neelakantan,PranavShyam,GirishSastry,Amanda
tomoredomainswouldrequireadditionalbudgets Askell, Sandhini Agarwal, Ariel Herbert-Voss,
andhumanefforttobeabletoimplement. Gretchen Krueger, Tom Henighan, Rewon Child,
|     |     |     |     |     |     | Aditya | Ramesh, | Daniel | M.  | Ziegler, | Jeffrey | Wu, |
| --- | --- | --- | --- | --- | --- | ------ | ------- | ------ | --- | -------- | ------- | --- |
ClemensWinter,ChristopherHesse,MarkChen,Eric
Acknowledgements
Sigler,MateuszLitwin,ScottGray,BenjaminChess,
|                                    |      |          |                 |     |         | Jack Clark,                              | Christopher |                 | Berner, | Sam | McCandlish, |         |
| ---------------------------------- | ---- | -------- | --------------- | --- | ------- | ---------------------------------------- | ----------- | --------------- | ------- | --- | ----------- | ------- |
| We would                           | like | to thank | our annotators, |     | without |                                          |             |                 |         |     |             |         |
|                                    |      |          |                 |     |         | Alec Radford,                            |             | Ilya Sutskever, |         | and | Dario       | Amodei. |
| whomNoMIRACLcouldnothavebeenbuilt. |      |          |                 |     | We      |                                          |             |                 |         |     |             |         |
|                                    |      |          |                 |     |         | 2020. Languagemodelsarefew-shotlearners. |             |                 |         |     |             | InAd-   |
would also like to thank Akintunde Oladipo for vancesinNeuralInformationProcessingSystems33:

AnnualConferenceonNeuralInformationProcess- Xinya Du and Heng Ji. 2022. Retrieval-augmented
ing Systems 2020, NeurIPS 2020, December 6-12, generative question answering for event argument
| 2020,virtual. |     |     |     |     |     | extraction. | InProceedingsofthe2022Conferenceon |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | --- |
EmpiricalMethodsinNaturalLanguageProcessing,
| NicolaDeCao,WilkerAziz,andIvanTitov.2021. |     |     |     |     | Edit- |       |       |            |        |      |           |     |
| ----------------------------------------- | --- | --- | --- | --- | ----- | ----- | ----- | ---------- | ------ | ---- | --------- | --- |
|                                           |     |     |     |     |       | EMNLP | 2022, | Abu Dhabi, | United | Arab | Emirates, |     |
InPro-
ingfactualknowledgeinlanguagemodels. December7-11,2022,pages4649–4666.Association
ceedingsofthe2021ConferenceonEmpiricalMeth- forComputationalLinguistics.
odsinNaturalLanguageProcessing,EMNLP2021,
VirtualEvent/PuntaCana,DominicanRepublic,7-
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,
11November,2021,pages6491–6506.Association
AbhishekKadian,AhmadAl-Dahle,AieshaLetman,
forComputationalLinguistics.
|     |     |     |     |     |     | Akhil Mathur, |     | Alan Schelten, |     | Amy | Yang, | Angela |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | --- | ----- | ------ |
Fan,AnirudhGoyal,AnthonyHartshorn,AoboYang,
| Yupeng Chang, | Xu           | Wang, | Jindong   | Wang,    | Yuan Wu, |             |                    |     |     |               |     |     |
| ------------- | ------------ | ----- | --------- | -------- | -------- | ----------- | ------------------ | --- | --- | ------------- | --- | --- |
|               |              |       |           |          |          | ArchiMitra, | ArchieSravankumar, |     |     | ArtemKorenev, |     |     |
| Linyi         | Yang, Kaijie | Zhu,  | Hao Chen, | Xiaoyuan | Yi,      |             |                    |     |     |               |     |     |
ArthurHinsvark,ArunRao,AstonZhang,Aurélien
CunxiangWang,YidongWang,WeiYe,YueZhang,
|     |     |     |     |     |     | Rodriguez, | Austen | Gregerson, |     | Ava | Spataru, | Bap- |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ---------- | --- | --- | -------- | ---- |
YiChang,PhilipS.Yu,QiangYang,andXingXie.
|     |     |     |     |     |     | tiste Rozière, | Bethany |     | Biron, | Binh | Tang, | Bobbie |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | --- | ------ | ---- | ----- | ------ |
2024. Asurveyonevaluationoflargelanguagemod-
Chern,CharlotteCaucheteux,ChayaNayak,Chloe
| ACM  | Trans. | Intell. | Syst. Technol., |     |             |     |     |     |     |     |     |     |
| ---- | ------ | ------- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| els. |        |         |                 |     | 15(3):39:1– |     |     |     |     |     |     |     |
Bi,ChrisMarra,ChrisMcConnell,ChristianKeller,
39:45.
|     |     |     |     |     |     | Christophe | Touret, | Chunyang |     | Wu, Corinne |     | Wong, |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | --- | ----------- | --- | ----- |
CristianCantonFerrer,CyrusNikolaidis,DamienAl-
| Jiawei Chen, | Hongyu | Lin, | Xianpei | Han, and | Le Sun. |     |     |     |     |     |     |     |
| ------------ | ------ | ---- | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
lonsius,DanielSong,DaniellePintz,DannyLivshits,
| 2024.               | Benchmarking |             | large language |                  | models in |               |     |                  |     |       |          |     |
| ------------------- | ------------ | ----------- | -------------- | ---------------- | --------- | ------------- | --- | ---------------- | --- | ----- | -------- | --- |
|                     |              |             |                |                  |           | David Esiobu, |     | Dhruv Choudhary, |     | Dhruv | Mahajan, |     |
| retrieval-augmented |              | generation. |                | In Thirty-Eighth |           |               |     |                  |     |       |          |     |
AAAI Conference on Artificial Intelligence, AAAI DiegoGarcia-Olano,DiegoPerino,DieuwkeHupkes,
EgorLakomkin,EhabAlBadawy,ElinaLobanova,
2024,Thirty-SixthConferenceonInnovativeApplica-
EmilyDinan,EricMichaelSmith,FilipRadenovic,
tionsofArtificialIntelligence,IAAI2024,Fourteenth
FrankZhang,GabrielSynnaeve,GabrielleLee,Geor-
| Symposium | on Educational |     | Advances | in  | Artificial |     |     |     |     |     |     |     |
| --------- | -------------- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
giaLewisAnderson,GraemeNail,GrégoireMialon,
Intelligence,EAAI2014,February20-27,2024,Van-
couver,Canada,pages17754–17762.AAAIPress. GuanPang,GuillemCucurell,HaileyNguyen,Han-
nahKorevaar,HuXu,HugoTouvron,IliyanZarov,
|     |     |     |     |     |     | Imanol Arrieta |     | Ibarra, Isabel |     | M. Kloumann, |     | Ishan |
| --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | ------------ | --- | ----- |
EunsolChoi,HeHe,MohitIyyer,MarkYatskar,Wen-
Misra,IvanEvtimov,JadeCopet,JaewonLee,Jan
| tauYih, | YejinChoi, | PercyLiang, |     | andLukeZettle- |     |     |     |     |     |     |     |     |
| ------- | ---------- | ----------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Geffert,JanaVranes,JasonPark,JayMahadeokar,
| moyer.2018. | QuAC:Questionansweringincontext. |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In Proceedings of the 2018 Conference on Empiri- Jeet Shah, Jelmer van der Linde, Jennifer Billock,
calMethodsinNaturalLanguageProcessing,pages Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi,
2174–2184,Brussels,Belgium.AssociationforCom- Jianyu Huang, Jiawen Liu, Jie Wang, Jiecao Yu,
|     |     |     |     |     |     | Joanna Bitton, |     | Joe Spisak, | Jongsoo |     | Park, | Joseph |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------- | --- | ----- | ------ |
putationalLinguistics.
|     |     |     |     |     |     | Rocca, Joshua  |     | Johnstun, | Joshua    | Saxe,    | Junteng | Jia, |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --------- | -------- | ------- | ---- |
|     |     |     |     |     |     | Kalyan Vasuden |     | Alwala,   | Kartikeya | Upasani, |         | Kate |
JonathanH.Clark,JennimariaPalomaki,VitalyNiko-
laev, Eunsol Choi, Dan Garrette, Michael Collins, Plawiak,KeLi,KennethHeafield,KevinStone,and
and Tom Kwiatkowski. 2020. Tydi QA: A bench- et al. 2024. The llama 3 herd of models. CoRR,
| markforinformation-seekingquestionansweringin |     |     |     |                  |     | abs/2407.21783. |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| typologicallydiverselanguages.                |     |     |     | Trans.Assoc.Com- |     |                 |     |     |     |     |     |     |
put.Linguistics,8:454–470. LuyuGao,XueguangMa,JimmyLin,andJamieCallan.
|     |     |     |     |     |     | 2023a. Tevatron: |     | An efficient |     | and flexible |     | toolkit |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ------------ | --- | ------- |
AntoniaCreswell,MurrayShanahan,andIrinaHiggins. forneuralretrieval. InProceedingsofthe46thInter-
2023. Selection-inference:Exploitinglargelanguage
nationalACMSIGIRConferenceonResearchand
| models | for interpretable |     | logical | reasoning. | In The |     |     |     |     |     |     |     |
| ------ | ----------------- | --- | ------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
DevelopmentinInformationRetrieval,SIGIR2023,
EleventhInternationalConferenceonLearningRep-
Taipei,Taiwan,July23-27,2023,pages3120–3124.
| resentations,ICLR2023,Kigali,Rwanda,May1-5, |     |     |     |     |     | ACM. |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
2023.OpenReview.net.
TianyuGao,HowardYen,JiatongYu,andDanqiChen.
| Jacob Devlin, | Ming-Wei   |       | Chang, | Kenton       | Lee, and |        |          |       |          |        |     |        |
| ------------- | ---------- | ----- | ------ | ------------ | -------- | ------ | -------- | ----- | -------- | ------ | --- | ------ |
|               |            |       |        |              |          | 2023b. | Enabling | large | language | models | to  | gener- |
| Kristina      | Toutanova. | 2018. | BERT:  | pre-training | of       |        |          |       |          |        |     |        |
InProceedingsofthe2023
| deepbidirectionaltransformersforlanguageunder- |     |     |     |     |     | atetextwithcitations. |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
CoRR,abs/1810.04805. Conference on Empirical Methods in Natural Lan-
standing.
guageProcessing,EMNLP2023,Singapore,Decem-
|          |             |         |     |          |          | ber 6-10, | 2023, | pages 6465–6488. |     | Association |     | for |
| -------- | ----------- | ------- | --- | -------- | -------- | --------- | ----- | ---------------- | --- | ----------- | --- | --- |
| Shehzaad | Dhuliawala, | Mojtaba |     | Komeili, | Jing Xu, |           |       |                  |     |             |     |     |
ComputationalLinguistics.
RobertaRaileanu,XianLi,AsliCelikyilmaz,andJa-
| sonWeston.2024. |     | Chain-of-verificationreduceshal- |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lucinationinlargelanguagemodels. InFindingsof Biyang Guo, Xin Zhang, Ziyuan Wang, Minqi Jiang,
theAssociationforComputationalLinguistics,ACL JinranNie,YuxuanDing,JianweiYue,andYupeng
2024, Bangkok, Thailand and virtual meeting, Au- Wu.2023. HowcloseisChatGPTtohumanexperts?
gust11-16,2024,pages3563–3578.Associationfor comparisoncorpus,evaluation,anddetection. CoRR,
| ComputationalLinguistics. |     |     |     |     |     | abs/2301.07597. |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |

KelvinGuu,KentonLee,ZoraTung,PanupongPasupat, Joshi,HannaMoazam,HeatherMiller,MateiZaharia,
and Ming-Wei Chang. 2020. Retrieval augmented and Christopher Potts. 2023. DSPy: Compiling
languagemodelpre-training. InProceedingsofthe declarativelanguagemodelcallsintoself-improving
37thInternationalConferenceonMachineLearning, pipelines. CoRR,abs/2310.03714.
ICML2020,13-18July2020,VirtualEvent,volume
119ofProceedingsofMachineLearningResearch, Omar Khattab and Matei Zaharia. 2020. ColBERT:
pages3929–3938.PMLR. Efficientandeffectivepassagesearchviacontextu-
|     |     |     |     |     | alized | late interaction |     | over BERT. | In Proceedings |     |
| --- | --- | --- | --- | --- | ------ | ---------------- | --- | ---------- | -------------- | --- |
HangfengHe,HongmingZhang,andDanRoth.2023. ofthe43rdInternationalACMSIGIRconferenceon
Rethinking with retrieval: Faithful large language researchanddevelopmentinInformationRetrieval,
modelinference. CoRR,abs/2301.00303. SIGIR2020,VirtualEvent,China,July25-30,2020,
pages39–48.ACM.
EdwardJHu,yelongshen,PhillipWallis,ZeyuanAllen-
Zhu,YuanzhiLi,SheanWang,LuWang,andWeizhu
VivekKumar,RishabhMaheshwary,andVikramPudi.
| Chen. 2022. | LoRA: | Low-rank | adaptation | of large |       |             |          |     |                |      |
| ----------- | ----- | -------- | ---------- | -------- | ----- | ----------- | -------- | --- | -------------- | ---- |
|             |       |          |            |          | 2021. | Adversarial | examples |     | for evaluating | math |
language models. In International Conference on word problem solvers. In Findings of the Associ-
LearningRepresentations. ationforComputationalLinguistics: EMNLP2021,
VirtualEvent/PuntaCana,DominicanRepublic,16-
| GautierIzacardandEdouardGrave.2021. |     |     |     | Leveraging |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
20November,2021,pages2705–2712.Association
passageretrievalwithgenerativemodelsforopendo-
forComputationalLinguistics.
| mainquestionanswering. |     | InProceedingsofthe16th |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ConferenceoftheEuropeanChapteroftheAssoci-
|                                   |     |     |     |             | TomKwiatkowski, |     | JennimariaPalomaki, |     | OliviaRed- |     |
| --------------------------------- | --- | --- | --- | ----------- | --------------- | --- | ------------------- | --- | ---------- | --- |
| ationforComputationalLinguistics: |     |     |     | MainVolume, |                 |     |                     |     |            |     |
field,MichaelCollins,AnkurP.Parikh,ChrisAlberti,
EACL2021,Online,April19-23,2021,pages874– DanielleEpstein,IlliaPolosukhin,JacobDevlin,Ken-
880.AssociationforComputationalLinguistics.
tonLee,KristinaToutanova,LlionJones,Matthew
|           |           |              |             |       | Kelcey,    | Ming-Wei | Chang,  | Andrew | M. Dai,       | Jakob |
| --------- | --------- | ------------ | ----------- | ----- | ---------- | -------- | ------- | ------ | ------------- | ----- |
| Robin Jia | and Percy | Liang. 2017. | Adversarial | exam- |            |          |         |        |               |       |
|           |           |              |             |       | Uszkoreit, | Quoc     | Le, and | Slav   | Petrov. 2019. | Natu- |
plesforevaluatingreadingcomprehensionsystems.
|                |     |          |            |            | ralQuestions: |                                       | abenchmarkforquestionanswering |     |     |     |
| -------------- | --- | -------- | ---------- | ---------- | ------------- | ------------------------------------- | ------------------------------ | --- | --- | --- |
| In Proceedings | of  | the 2017 | Conference | on Empiri- |               |                                       |                                |     |     |     |
|                |     |          |            |            | research.     | Trans.Assoc.Comput.Linguistics,7:452– |                                |     |     |     |
calMethodsinNaturalLanguageProcessing,pages
| 2021–2031,Copenhagen,Denmark.Associationfor |     |     |     |     | 466. |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
ComputationalLinguistics.
|     |     |     |     |     | Patrick | S. H. | Lewis, Ethan | Perez, | Aleksandra | Pik- |
| --- | --- | --- | --- | --- | ------- | ----- | ------------ | ------ | ---------- | ---- |
AlbertQ.Jiang,AlexandreSablayrolles,ArthurMen- tus, Fabio Petroni, Vladimir Karpukhin, Naman
Goyal,HeinrichKüttler,MikeLewis,Wen-tauYih,
sch,ChrisBamford,DevendraSinghChaplot,Diego
|           |                |           |           |           | Tim    | Rocktäschel, | Sebastian           |     | Riedel, and | Douwe |
| --------- | -------------- | --------- | --------- | --------- | ------ | ------------ | ------------------- | --- | ----------- | ----- |
| de Las    | Casas, Florian | Bressand, | Gianna    | Lengyel,  |        |              |                     |     |             |       |
|           |                |           |           |           | Kiela. | 2020.        | Retrieval-augmented |     | generation  | for   |
| Guillaume | Lample,        | Lucile    | Saulnier, | Lélio Re- |        |              |                     |     |             |       |
nard Lavaud, Marie-Anne Lachaux, Pierre Stock, knowledge-intensiveNLPtasks. InAdvancesinNeu-
TevenLeScao,ThibautLavril,ThomasWang,Timo- ralInformationProcessingSystems33: AnnualCon-
ferenceonNeuralInformationProcessingSystems
| théeLacroix,andWilliamElSayed.2023. |     |     |     | Mistral |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
2020,NeurIPS2020,December6-12,2020,virtual.
7b. CoRR,abs/2310.06825.
|           |                  |     |               |         | Daliang | Li, Ankit | Singh | Rawat, | Manzil Zaheer, | Xin |
| --------- | ---------------- | --- | ------------- | ------- | ------- | --------- | ----- | ------ | -------------- | --- |
| Albert Q. | Jiang, Alexandre |     | Sablayrolles, | Antoine |         |           |       |        |                |     |
Roux,ArthurMensch,BlancheSavary,ChrisBam- Wang, Michal Lukasik, Andreas Veit, Felix X. Yu,
ford,DevendraSinghChaplot,DiegodeLasCasas, and Sanjiv Kumar. 2023. Large language models
Emma Bou Hanna, Florian Bressand, Gianna withcontrollableworkingmemory. InFindingsof
Lengyel, Guillaume Bour, Guillaume Lample, theAssociationforComputationalLinguistics: ACL
2023,Toronto,Canada,July9-14,2023,pages1774–
| Lélio Renard | Lavaud, | Lucile | Saulnier, | Marie- |     |     |     |     |     |     |
| ------------ | ------- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- |
AnneLachaux,PierreStock,SandeepSubramanian, 1793.AssociationforComputationalLinguistics.
| Sophia | Yang, Szymon | Antoniak, | Teven | Le Scao, |     |     |     |     |     |     |
| ------ | ------------ | --------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
Théophile Gervet, Thibaut Lavril, Thomas Wang, JunyiLi,TianyiTang,WayneXinZhao,Jian-YunNie,
TimothéeLacroix,andWilliamElSayed.2024. Mix- andJi-RongWen.2024. Pre-trainedlanguagemodels
|                |                      |     |     |     | fortextgeneration: |     | Asurvey. |     | ACMComput.Surv., |     |
| -------------- | -------------------- | --- | --- | --- | ------------------ | --- | -------- | --- | ---------------- | --- |
| tralofexperts. | CoRR,abs/2401.04088. |     |     |     |                    |     |          |     |                  |     |
56(9).
VladimirKarpukhin,BarlasOguz,SewonMin,Patrick
NelsonF.Liu,KevinLin,JohnHewitt,AshwinParan-
S.H.Lewis,LedellWu,SergeyEdunov,DanqiChen,
andWen-tauYih.2020. Densepassageretrievalfor jape,MicheleBevilacqua,FabioPetroni,andPercy
open-domainquestionanswering. InProceedingsof Liang. 2024. Lost in the middle: How language
the2020ConferenceonEmpiricalMethodsinNat- models use long contexts. Trans. Assoc. Comput.
ural Language Processing, EMNLP 2020, Online, Linguistics,12:157–173.
November16-20,2020,pages6769–6781.Associa-
|     |     |     |     |     | Joshua Maynez, |     | Shashi Narayan, |     | Bernd Bohnet, | and |
| --- | --- | --- | --- | --- | -------------- | --- | --------------- | --- | ------------- | --- |
tionforComputationalLinguistics.
|     |     |     |     |     | RyanT.McDonald.2020. |     |     | Onfaithfulnessandfac- |     |     |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | --------------------- | --- | --- |
Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, tualityinabstractivesummarization. InProceedings
Zhiyuan Zhang, Keshav Santhanam, Sri Vard- of the 58th Annual Meeting of the Association for
hamanan,SaifulHaq,AshutoshSharma,ThomasT. ComputationalLinguistics,ACL2020,Online,July

5-10,2020,pages1906–1919.AssociationforCom- KurtShuster,SpencerPoff,MoyaChen,DouweKiela,
putationalLinguistics. and Jason Weston. 2021. Retrieval augmentation
|     |     |     |     |     |     | reduces | hallucination | in  | conversation. |     | In Findings |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ------------- | --- | ----------- | --- |
KanishkaMisra,JuliaRayz,andAllysonEttinger.2023. of the Association for Computational Linguistics:
COMPS:Conceptualminimalpairsentencesfortest- EMNLP2021,VirtualEvent/PuntaCana,Domini-
ingrobustpropertyknowledgeanditsinheritancein canRepublic,16-20November,2021,pages3784–
pre-trainedlanguagemodels. InProceedingsofthe 3803.AssociationforComputationalLinguistics.
17thConferenceoftheEuropeanChapteroftheAs-
sociationforComputationalLinguistics,pages2928– Nandan Thakur, Nils Reimers, Andreas Rücklé, Ab-
|     |     |     |     |     |     | hishekSrivastava,andIrynaGurevych.2021. |     |     |     |     |     | BEIR: |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ----- |
2949,Dubrovnik,Croatia.AssociationforComputa-
Aheterogeneousbenchmarkforzero-shotevaluation
tionalLinguistics.
|     |     |     |     |     |     | ofinformationretrievalmodels. |     |     |     | InProceedingsof |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --------------- | --- | --- |
ArindamMitra, LucianoDelCorro, ShwetiMahajan, theNeuralInformationProcessingSystemsTrackon
AndrésCodas,ClarisseSimões,SahajAgrawal,Xuxi DatasetsandBenchmarks1,NeurIPSDatasetsand
Benchmarks2021,December2021,virtual.
Chen,AnastasiaRazdaibiedina,ErikJones,KritiAg-
garwal,HamidPalangi,GuoqingZheng,CorbyRos-
|     |     |     |     |     |     | Paul Thomas, | Seth | Spielman, |     | Nick Craswell, |     | and |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | --------- | --- | -------------- | --- | --- |
set,HamedKhanpour,andAhmedAwadallah.2023.
|        |                                      |     |     |     |     | BhaskarMitra.2024.                  |     | Largelanguagemodelscanac- |     |               |     |     |
| ------ | ------------------------------------ | --- | --- | --- | --- | ----------------------------------- | --- | ------------------------- | --- | ------------- | --- | --- |
| Orca2: | Teachingsmalllanguagemodelshowtorea- |     |     |     |     |                                     |     |                           |     |               |     |     |
|        |                                      |     |     |     |     | curatelypredictsearcherpreferences. |     |                           |     | InProceedings |     |     |
son. CoRR,abs/2311.11045.
ofthe47thInternationalACMSIGIRConferenceon
ResearchandDevelopmentinInformationRetrieval,
| OpenAI. 2023. |     | GPT-4 | technical | report. | CoRR, |     |     |     |     |     |     |     |
| ------------- | --- | ----- | --------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
SIGIR2024,WashingtonDC,USA,July14-18,2024,
abs/2303.08774.
pages1930–1940.ACM.
FabioPetroni,PatrickS.H.Lewis,AleksandraPiktus,
|     |     |     |     |     |     | Hugo Touvron, | Louis | Martin, | Kevin | Stone, | Peter | Al- |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | ----- | ------ | ----- | --- |
TimRocktäschel,YuxiangWu,AlexanderH.Miller,
|               |         |     |       |             |         | bert, Amjad | Almahairi, |     | Yasmine | Babaei, | Nikolay |     |
| ------------- | ------- | --- | ----- | ----------- | ------- | ----------- | ---------- | --- | ------- | ------- | ------- | --- |
| and Sebastian | Riedel. |     | 2020. | How context | affects |             |            |     |         |         |         |     |
Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti
| languagemodels’factualpredictions. |     |     |     | InConference |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Bhosale,DanBikel,LukasBlecher,CristianCanton-
onAutomatedKnowledgeBaseConstruction,AKBC
Ferrer,MoyaChen,GuillemCucurull,DavidEsiobu,
2020,Virtual,June22-24,2020.
JudeFernandes,JeremyFu,WenyinFu,BrianFuller,
CynthiaGao,VedanujGoswami,NamanGoyal,An-
| Pranav Rajpurkar, |     | Robin | Jia, and | Percy | Liang. 2018. |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
thonyHartshorn,SagharHosseini,RuiHou,Hakan
| Know what | you | don’t | know: | Unanswerable | ques- |     |     |     |     |     |     |     |
| --------- | --- | ----- | ----- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Inan,MarcinKardas,ViktorKerkez,MadianKhabsa,
| tionsforSQuAD. |     | InProceedingsofthe56thAnnual |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IsabelKloumann,ArtemKorenev,PunitSinghKoura,
| Meeting | of the Association |     | for | Computational | Lin- |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Marie-AnneLachaux,ThibautLavril,JenyaLee,Di-
| guistics(Volume2: |     | ShortPapers), |     | pages784–789, |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
anaLiskovich,YinghaiLu,YuningMao,XavierMar-
Melbourne,Australia.AssociationforComputational tinet,TodorMihaylov,PushkarMishra,IgorMoly-
Linguistics.
|     |     |     |     |     |     | bog, Yixin | Nie, | Andrew | Poulton, | Jeremy | Reizen- |     |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | -------- | ------ | ------- | --- |
stein,RashiRungta,KalyanSaladi,AlanSchelten,
| Vikas Raunak, | Arul | Menezes,                       | and | Marcin | Junczys- |                |      |         |           |        |          |      |
| ------------- | ---- | ------------------------------ | --- | ------ | -------- | -------------- | ---- | ------- | --------- | ------ | -------- | ---- |
|               |      |                                |     |        |          | Ruan Silva,    | Eric | Michael | Smith,    | Ranjan | Subrama- |      |
| Dowmunt.2021. |      | Thecuriouscaseofhallucinations |     |        |          |                |      |         |           |        |          |      |
|               |      |                                |     |        |          | nian, Xiaoqing |      | Ellen   | Tan, Binh | Tang,  | Ross     | Tay- |
inneuralmachinetranslation. InProceedingsofthe lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,
2021ConferenceoftheNorthAmericanChapterof
ZhengYan,IliyanZarov,YuchenZhang,AngelaFan,
| theAssociationforComputationalLinguistics: |     |     |     |     | Hu- |         |           |        |         |     |          |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------- | --------- | ------ | ------- | --- | -------- | --- |
|                                            |     |     |     |     |     | Melanie | Kambadur, | Sharan | Narang, |     | Aurélien | Ro- |
manLanguageTechnologies,NAACL-HLT2021,On-
driguez,RobertStojnic,SergeyEdunov,andThomas
line,June6-11,2021,pages1172–1183.Association
|     |     |     |     |     |     | Scialom.2023. | Llama2: |     | Openfoundationandfine- |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | ---------------------- | --- | --- | --- |
forComputationalLinguistics. tunedchatmodels. CoRR,abs/2307.09288.
SivaReddy,DanqiChen,andChristopherD.Manning. HarshTrivedi,NiranjanBalasubramanian,TusharKhot,
2019. CoQA:AConversationalQuestionAnswer-
|               |     |                                 |     |     |     | andAshishSabharwal.2023. |     |     |           | Interleavingretrieval |            |     |
| ------------- | --- | ------------------------------- | --- | --- | --- | ------------------------ | --- | --- | --------- | --------------------- | ---------- | --- |
| ingChallenge. |     | TransactionsoftheAssociationfor |     |     |     |                          |     |     |           |                       |            |     |
|               |     |                                 |     |     |     | with chain-of-thought    |     |     | reasoning | for                   | knowledge- |     |
ComputationalLinguistics,7:249–266.
|     |     |     |     |     |     | intensive | multi-step | questions. |     | In Proceedings |     | of  |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ---------- | --- | -------------- | --- | --- |
the61stAnnualMeetingoftheAssociationforCom-
StephenE.RobertsonandHugoZaragoza.2009. The putational Linguistics (Volume 1: Long Papers),
probabilistic relevance framework: BM25 and be- ACL2023,Toronto,Canada,July9-14,2023,pages
yond. Found.TrendsInf.Retr.,3(4):333–389.
|     |     |     |     |     |     | 10014–10037. | Association |     | for | Computational |     | Lin- |
| --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --- | ------------- | --- | ---- |
guistics.
| Freda Shi, | Xinyun | Chen, | Kanishka | Misra, | Nathan |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Scales,DavidDohan,EdH.Chi,NathanaelSchärli, AhmetÜstün,ViraatAryabumi,ZhengXinYong,Wei-
andDennyZhou.2023. Largelanguagemodelscan YinKo,DanielD’souza,GbemilekeOnilude,Neel
beeasilydistractedbyirrelevantcontext. InInterna- Bhandari,ShivalikaSingh,Hui-LeeOoi,AmrKayid,
tionalConferenceonMachineLearning,ICML2023, Freddie Vargus, Phil Blunsom, Shayne Longpre,
23-29 July 2023, Honolulu, Hawaii, USA, volume NiklasMuennighoff,MarziehFadaee,JuliaKreutzer,
202ofProceedingsofMachineLearningResearch, andSaraHooker.2024. Ayamodel: Aninstruction
pages31210–31227.PMLR. finetunedopen-accessmultilinguallanguagemodel.

In Proceedings of the 62nd Annual Meeting of the
AssociationforComputationalLinguistics(Volume1:
LongPapers),ACL2024,Bangkok,Thailand,August
11-16, 2024, pages 15894–15939. Association for
ComputationalLinguistics.
EllenM.Voorhees.1998. Variationsinrelevancejudg-
mentsandthemeasurementofretrievaleffectiveness.
InSIGIR’98: Proceedingsofthe21stAnnualInter-
nationalACMSIGIRConferenceonResearchand
DevelopmentinInformationRetrieval,August24-28
1998,Melbourne,Australia,pages315–323.ACM.
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Bosma,BrianIchter,FeiXia,EdH.Chi,QuocV.Le,
andDennyZhou. 2022. Chain-of-thoughtprompt-
ing elicits reasoning in large language models. In
NeurIPS.
PeilinYang,HuiFang,andJimmyLin.2018. Anserini:
ReproduciblerankingbaselinesusingLucene. ACM
J.DataInf.Qual.,10(4):16:1–16:20.
OriYoran,TomerWolfson,OriRam,andJonathanBe-
rant. 2024. Making retrieval-augmented language
modelsrobusttoirrelevantcontext. InTheTwelfth
International Conference on Learning Representa-
tions,ICLR2024,Vienna,Austria,May7-11,2024.
OpenReview.net.
WenhaoYu,HongmingZhang,XiaomanPan,Kaixin
Ma,HongweiWang,andDongYu.2023. Chain-of-
note: Enhancingrobustnessinretrieval-augmented
languagemodels. CoRR,abs/2311.09210.
Xinyu Zhang, Kelechi Ogueji, Xueguang Ma, and
JimmyLin.2022. Towardsbestpracticesfortrain-
ing multilingual dense retrieval models. CoRR,
abs/2204.02363.
Xinyu Zhang, Nandan Thakur, Odunayo Ogundepo,
Ehsan Kamalloo, David Alfonso-Hermelo, Xi-
aoguang Li, Qun Liu, Mehdi Rezagholizadeh, and
Jimmy Lin. 2023. MIRACL: A Multilingual Re-
trieval Dataset Covering 18 Diverse Languages.
TransactionsoftheAssociationforComputational
Linguistics,11:1114–1131.
ShuyanZhou,UriAlon,FrankF.Xu,ZhengbaoJiang,
andGrahamNeubig.2023. DocPrompting: Gener-
atingcodebyretrievingthedocs. InTheEleventh
International Conference on Learning Representa-
tions, ICLR2023, Kigali, Rwanda, May1-5, 2023.
OpenReview.net.

A Appendix
|     |     |     |     |     | onboardingandtrainingprocess. |     |     | Overallourhir- |     |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- | --- | -------------- | --- | --- |
ingprocessandNoMIRACLdataconstructionin
| The following | supplementary |     | sections | in  | the ap-                 |     |     |                     |     |     |
| ------------- | ------------- | --- | -------- | --- | ----------------------- | --- | --- | ------------------- | --- | --- |
|               |               |     |          |     | totaltookaround6months. |     |     | Weofferedannotators |     |     |
pendixarearrangedasfollows:
thehourlyrateof$18.50perhour(convertedinto
| • Appendix | B   | provides | information |     | on the             |     |                       |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ------------------ | --- | --------------------- | --- | --- | --- |
|            |     |          |             |     | USD).Forreference, |     | thelocalminimumwageis |     |     |     |
NoMIRACLdatasetrelease.
$11.50USD/hr.
| • Appendix | C   | provides | additional | construc- |     |     |     |     |     |     |
| ---------- | --- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
tiondetailsinNoMIRACL,includingcorpora
|     |     |     |     |     | D QualityControl |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
preparationandannotatorhiringdetails.
Toensurehighdataquality,weconductamanual
• AppendixDdescribesstepswetookforqual-
|     |     |     |     |     | assessment | executed | by  | human reviewers |     | (hired |
| --- | --- | --- | --- | --- | ---------- | -------- | --- | --------------- | --- | ------ |
itycontrolduringthedatasetconstruction.
• AppendixEprovidesmodelcheckpointsand part-time)onarandomsubsetofNoMIRACLan-
notations,followingMIRACL(Zhangetal.,2023).
additionalexperimentalresults.
Weconductedourqualitycontrolintwophases.
B DetailsonNoMIRACLDatasetRelease PhaseI.Inthisphase,reviewersweregivenboth
|            |     |          |         |          | the prompts | and | the generated | queries | and | filled |
| ---------- | --- | -------- | ------- | -------- | ----------- | --- | ------------- | ------- | --- | ------ |
| Licensing. | The | NoMIRACL | dataset | is based | on          |     |               |         |     |        |
upachecklisttodeterminewhetherthequalityof
| language-specificWikipedia. |              |     | Wefollowthesame |          |                               |     |     |                 |     |     |
| --------------------------- | ------------ | --- | --------------- | -------- | ----------------------------- | --- | --- | --------------- | --- | --- |
|                             |              |     |                 |          | thequeriesmetourrequirements. |     |     | Criteriainclude |     |     |
| license                     | as Wikipedia | for | NoMIRACL:       | Creative |                               |     |     |                 |     |     |
theexaminationofthequeryitself(e.g.,spelling,
CommonsAttribution-ShareAlike4.0UnportedLi-
|                     |     |                          |     |     | syntax, | and fluency, | etc.) | and whether | the | query |
| ------------------- | --- | ------------------------ | --- | --- | ------- | ------------ | ----- | ----------- | --- | ----- |
| cense(CCBY-SA4.0).6 |     | Overall,thelicenseallows |     |     |         |              |       |             |     |       |
couldbeanswereddirectlybytheprompt,which
| both researchers |     | and industry | alike | to access | the |     |     |     |     |     |
| ---------------- | --- | ------------ | ----- | --------- | --- | --- | --- | --- | --- | --- |
wewantedtoavoidtogeneratemoreinformative
dataset,andallowthemtocopyandredistributethe
queries,following(Clarketal.,2020;Zhangetal.,
datasetforfuturework.
|     |     |     |     |     | 2023). | To evaluate | this, | we measured | the | lexical |
| --- | --- | --- | --- | --- | ------ | ----------- | ----- | ----------- | --- | ------- |
Examples. Arandomlysampledexampleforeach overlapbetweenthequeriesandtheircorrespond-
| of the | non-relevant | and | relevant subsets |     | of the      |                                  |     |     |     |     |
| ------ | ------------ | --- | ---------------- | --- | ----------- | -------------------------------- | --- | --- | --- | --- |
|        |              |     |                  |     | ingprompts. | Wefoundtheoverlapsprimarilyoccur |     |     |     |     |
NoMIRACLdatasetforEnglish(en)hasbeenpro-
inentitiesorstopwordsandthusconcludedthatthe
videdinTable8andTable9respectively. generatedqueriesarereasonablydifferentfromthe
givenprompts.
C AdditionalDataConstructionDetails
|     |     |     |     |     | Phase II. | In this | phase, | reviewers | were provided |     |
| --- | --- | --- | --- | --- | --------- | ------- | ------ | --------- | ------------- | --- |
CorporaPreparation. ForeachNoMIRACLlan- thesameguidanceasannotatorsperformingtherel-
guage, we follow the same passage corpora pro- evanceassessment. Theywereaskedtolabelaran-
| videdinMIRACL(Zhangetal.,2023). |     |     |     | Outofthe |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
domlysampledsubsetofthequery–passagepairs
18 languages, 11 of the existing languages com- fromourannotatedbatch. Thedegreeofagreement
moninMr. TYDI (Zhangetal.,2022)usetheraw ontheoverlappingpairsisusedtoquantifythequal-
| Wikipedia | dump | from early | 2019 and | the | rest of                  |     |     |                     |     |     |
| --------- | ---- | ---------- | -------- | --- | ------------------------ | --- | --- | ------------------- | --- | --- |
|           |      |            |          |     | ityoftherelevancelabels. |     |     | Overall,weobserveon |     |     |
thelanguagesusedinMIRACLuseareleasefrom averageagreementsofover80%onquery–passage
March 2022. In MIRACL, all Wikipedia articles relevance,whichisconsistentwiththeIRliterature
| are parsed | using | WikiExtractor7 | and | segmented |     |     |     |     |     |     |
| ---------- | ----- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
datingbackmanydecades(Voorhees,1998).
intopassagesbasedonnaturaldiscourseunitsus-
|     |     |     |     |     | E CheckpointsandAdditionalResults |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- |
ingtwoconsecutivenewlinesinthewikimarkup
asthedelimiter.
Allmultilingual-focusedLLMcheckpointsusedin
AnnotatorHiringDetails. Animportantfeature ourexperimentsforbothclosedandopen-sourced
of NoMIRACL is that our dataset was not con- canbefoundinTable5. Hyperparameterchoices
structedviacrowd-sourcedworkerssimilartoMIR-
duringNoMIRACLsupervisedfine-tuningLLMs
| ACL(Zhangetal.,2023). |     |     | Weoverallhired31an- |     |            |          |       |              |         |     |
| --------------------- | --- | --- | ------------------- | --- | ---------- | -------- | ----- | ------------ | ------- | --- |
|                       |     |     |                     |     | are listed | in Table | 6 and | experimental | results | in  |
notators (both part-time and full-time) across all Table7. LLMevaluationresultsforboththenon-
languagesinNoMIRACL.Eachannotatorwasin-
|     |     |     |     |     | relevant | and relevant |     | subsets for all | models | can |
| --- | --- | --- | --- | --- | -------- | ------------ | --- | --------------- | ------ | --- |
terviewedandevaluatedtobeanativespeakerof
|     |     |     |     |     | be found | in Figure | 8   | and Figure | 9 respectively. |     |
| --- | --- | --- | --- | --- | -------- | --------- | --- | ---------- | --------------- | --- |
their language, based on a carefully constructed Figure10showstemplatechangesforpromptop-
timizationablationexperiments,including(i)role,
6https://creativecommons.org/licenses/by-sa/4.0/
7https://github.com/attardi/wikiextractor (ii)repeat,and(iii)explanationprompts.

GPT-4o GPT-3.5 Mistral-7B Orca-2-7B Aya-101 LLAMA-2-13B LLAMA-3-70B
GPT-4 Mixtral-7x8B Orca-2-13B Aya-23-35B LLAMA-2-70B LLAMA-2-7B LLAMA-3-8B
)% ni( etar noitanicullaH 100%
80%
60%
40%
20%
0%
|     | ar bn de | en es fa | fr fi | hi id ja ko | ru sw | te th yo zh |
| --- | -------- | -------- | ----- | ----------- | ----- | ----------- |
Figure8: Hallucinationrate(in%)=FP/(FP+TN)onthenon-relevantsubsetinNoMIRACLtestsplit. The
non-relevantsubsetcontainsquerieswithno-knownanswers,i.e.,alltop-k(wherek =10)passagesarejudgedby
ahumanannotatorasnon-relevant. Onaverage,mostLLMs(exceptMistral)hallucinateonthenon-relevantsubset.
Lowerthehallucinationrateisbetter.
GPT-4o GPT-3.5 Mistral-7B Orca-2-7B Aya-101 LLAMA-2-13B LLAMA-3-70B
100% GPT-4 Mixtral-7x8B Orca-2-13B Aya-23-35B LLAMA-2-70B LLAMA-2-7B LLAMA-3-8B
)% ni( etar rorrE 80%
60%
40%
20%
0%
|     | ar bn de | en es fa | fr fi | hi id ja ko | ru sw | te th yo zh |
| --- | -------- | -------- | ----- | ----------- | ----- | ----------- |
Errorrate(in%)=FN/(FN+TP)ontherelevantsubsetinNoMIRACLtestsplit.
| Figure9: |     |     |     |     |     | Therelevantsubset |
| -------- | --- | --- | --- | --- | --- | ----------------- |
containsquerieswithknownanswers,i.e.,atleastoneofthetop-k(wherek =10)passagesjudgedbyahuman
annotator is relevant. On average, most LLMs (except Mistral and Aya-101) have a lower error rate, i.e., can
| accuratelyidentifytherelevantanswer. |     |                        | Lowertheerrorrateisbetter. |     |     |     |
| ------------------------------------ | --- | ---------------------- | -------------------------- | --- | --- | --- |
| Model                                |     | ModelCheckpoints(Link) |                            |     |     |     |
OpenAIbaselinemodels
| GPT-4o  | learn.microsoft.com/en-us/azure/ai-services/openai/ |     |     |                |     |       |
| ------- | --------------------------------------------------- | --- | --- | -------------- | --- | ----- |
| GPT-4   | learn.microsoft.com/en-us/azure/ai-services/openai/ |     |     |                |     |       |
| GPT-3.5 | learn.microsoft.com/en-us/azure/ai-services/openai/ |     |     |                |     |       |
|         |                                                     |     |     | Hyperparameter |     | Value |
Mistralbaselinemodels
|              |                                                     |     |     | use_peft    |     | true     |
| ------------ | --------------------------------------------------- | --- | --- | ----------- | --- | -------- |
| Mixtral-8x7B | huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1 |     |     |             |     |          |
|              |                                                     |     |     | torch_dtype |     | bfloat16 |
Mistral-7B(v0.3) huggingface.co/mistralai/Mistral-7B-Instruct-v0.3 lora_r 64
|     | Orca-2baselinemodels |     |     | lora_alpha |     | 16  |
| --- | -------------------- | --- | --- | ---------- | --- | --- |
Orca-2-13B huggingface.co/microsoft/Orca-2-13b lora_dropout 0.05
|           |                                    |     |     | lora_target_modules | {q_proj, k_proj, | v_proj, o_proj,     |
| --------- | ---------------------------------- | --- | --- | ------------------- | ---------------- | ------------------- |
| Orca-2-7B | huggingface.co/microsoft/Orca-2-7b |     |     |                     |                  |                     |
|           |                                    |     |     |                     | gate_proj,       | up_proj, down_proj} |
Ayabaselinemodels
|     |     |     |     | learning_rate |     | 3.0e-06 |
| --- | --- | --- | --- | ------------- | --- | ------- |
Aya-101 huggingface.co/CohereForAI/aya-101 lr_scheduler_type cosine
Aya-23-35B huggingface.co/CohereForAI/aya-23-35B max_seq_length 4096
LLAMA-2baselinemodels
LLAMA-2-70B huggingface.co/meta-llama/Llama-2-70b-chat-hf Table6: HyperparametersettingschosenduringLoRA
LLAMA-2-13B huggingface.co/meta-llama/Llama-2-13b-chat-hf supervised fine-tuning (SFT) Mistral-7B (v0.3) and
| LLAMA-2-7B | huggingface.co/meta-llama/Llama-2-7b-chat-hf |     |     |     |     |     |
| ---------- | -------------------------------------------- | --- | --- | --- | --- | --- |
LLAMA-3baselinemodels LLAMA-3 (8B) instruct models on the NoMIRACL
developmentsplit.
| LLAMA-3(70B) | huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct |                |                |     |     |     |
| ------------ | --------------------------------------------------- | -------------- | -------------- | --- | --- | --- |
| LLAMA-3(8B)  | huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct  |                |                |     |     |     |
| Table 5:     | All models                                          | and checkpoint | links used for |     |     |     |
NoMIRACLevaluation.

You are an evaluator checking whether the question contains the answer within the provided
contexts or not. I will give you a question and several contexts containing information about the
question. Read the contexts carefully. If any of the contexts answers the question, respond as
| either “Yes, | answer is present” | or “I don’t | know”: |     |     |     |     |
| ------------ | ------------------ | ----------- | ------ | --- | --- | --- | --- |
| QUESTION:    | {query}            |             |        |     |     |     |     |
CONTEXTS:
| [1] {Passage | title}: {Passage | text} |     |     |     |     |     |
| ------------ | ---------------- | ----- | --- | --- | --- | --- | --- |
| [2] {Passage | title}: {Passage | text} |     |     |     |     |     |
...
| [10] {Passage | title}: {Passage | text} |     |     |     |     |     |
| ------------- | ---------------- | ----- | --- | --- | --- | --- | --- |
Please remember to read all the contexts carefully. If any of the contexts answers the
question: {query}, respond as either “Yes, answer is present” or “I don’t know”.
OUTPUT:
Read the query and the contexts carefully and provide a step-by-step explanation for your answer.
If any of the contexts answers the question, respond as either “Yes, answer is present” or “I
don’t know”. You must strictly follow the output format with ## Reasoning: ... ## Answer: “Yes,
| answer is | present” OR “I don’t | know”. |     |     |     |     |     |
| --------- | -------------------- | ------ | --- | --- | --- | --- | --- |
| QUESTION: | {query}              |        |     |     |     |     |     |
CONTEXTS:
| [1] {Passage | title}: {Passage | text} |     |     |     |     |     |
| ------------ | ---------------- | ----- | --- | --- | --- | --- | --- |
| [2] {Passage | title}: {Passage | text} |     |     |     |     |     |
...
| [10] {Passage | title}: {Passage | text} |     |     |     |     |     |
| ------------- | ---------------- | ----- | --- | --- | --- | --- | --- |
OUTPUT:
Figure10: AllpromptablationsusedinourexperimentsforLLMhallucinationevaluationforall18languages
inNoMIRACLonboththerelevantandnon-relevantsubsets. RolepromptappendstheroleoftheLLMatthe
beginningoftheprompt(highlightedinblue). Repeatprompthighlightsthetaskbyrepeatinginstructionsatthe
endoftheprompt(highlightedinred). Explanationpromptasksthemodeltoprovideareasoningpathandfinally
answerthequestion(highlightedinviolet).
|     | ar bn | de en es | fa fr fi | hi id ja | ko ru sw | te th yo | zh Avg. |
| --- | ----- | -------- | -------- | -------- | -------- | -------- | ------- |
HallucinationRates(in%)onNoMIRACLtestsplit(non-relevantsubset)
Llama-3(8B) 19.6 20.0 29.5 19.2 30.0 44.8 35.2 10.5 14.4 23.2 52.0 31.6 26.8 4.0 13.2 41.6 1.6 64.4 26.8
Llama-3(8B)(w/SFT) 83.0 12.5 36.9 44.0 46.8 65.6 36.9 70.0 61.5 53.1 41.7 9.7 85.4 42.2 0.0 82.7 12.0 20.0 44.7
Mistral-7B(v0.3) 40.4 63.2 38.2 42.8 17.2 52.4 47.6 16.1 39.6 30.8 44.4 28.8 41.6 14.8 74.0 58.8 23.6 45.2 40.0
Mistral-7B(v0.3)(w/SFT) 46.8 33.2 34.1 73.6 33.6 52.4 48.0 42.7 26.0 59.2 52.0 47.6 62.8 35.6 31.2 40.0 45.2 33.2 44.3
ErrorRates(in%)onNoMIRACLtestsplit(relevantsubset)
Llama-3(8B) 53.6 56.0 36.8 41.6 26.8 26.8 34.4 61.2 56.8 48.4 17.6 35.6 46.4 80.8 65.6 29.2 91.7 6.0 45.3
Llama-3(8B)(w/SFT) 6.0 70.8 32.4 31.2 24.0 14.6 21.2 8.8 14.9 40.6 24.0 77.2 8.3 32.5 87.5 4.2 75.5 50.4 34.7
Mistral-7B(v0.3) 14.4 20.4 21.6 8.0 28.0 22.4 15.6 38.0 30.8 43.6 16.0 30.0 18.0 57.6 17.6 13.6 50.0 13.2 25.5
Mistral-7B(v0.3)(w/SFT) 46.4 60.8 46.0 12.4 46.8 36.4 35.6 42.0 69.6 37.2 37.6 42.0 25.2 69.6 66.4 56.8 52.0 46.8 46.1
Table7: CompleteSFTresultsusingtheNoMIRACLdevelopmentdatasetforLLAMA-3(8B)andMistral-7B
(v0.3)LLMsacrossalllanguagesinNoMIRACL.Lowerthehallucinationanderrorrates(%)isbetter.

Query JudgedPassages Relevance
What is the name [1]AbelPrize:TheAbelPrize()isaNorwegianprizeawardedannuallybytheKingofNorwaytooneormoreoutstanding 0
ofthewinnerofthe mathematicians.ItisnamedafterNorwegianmathematicianNielsHenrikAbel(1802–1829)anddirectlymodeledafterthe
AbelPrizeof2022? NobelPrizes.Itcomeswithamonetaryawardof6millionNorwegiankroner(NOK)(C635,000or$740,000).
[2]MITDepartmentofMathematics:Thecurrentfacultyofaround50membersincludesWolfPrizewinnerMichaelArtin, 0
AbelPrizewinnerIsadoreSinger,andnumericalanalystGilbertStrang.
[3]AbelPrize:Afterinterestintheconceptoftheprizehadrisenin2001,aworkinggroupwasformedtodevelopaproposal, 0
whichwaspresentedtothePrimeMinisterofNorwayinMay.InAugust2001,theNorwegiangovernmentannouncedthat
theprizewouldbeawardedbeginningin2002,thetwo-hundredthanniversaryofAbel’sbirth. AtleSelbergreceivedan
honoraryAbelPrizein2002,butthefirstactualAbelPrizewasawardedin2003.
[4]AbelPrize:Theprizewasfirstproposedin1899,tobepartofthecelebrationofthe100thanniversaryofNielsHenrik 0
Abel’sbirthin1902.Shortlybeforehisdeathin1899,theNorwegianmathematicianSophusLieproposedestablishingan
AbelPrizewhenhelearnedthatAlfredNobel’splansforannualprizeswouldnotincludeaprizeinmathematics.KingOscar
IIwaswillingtofinanceamathematicsprizein1902,andthemathematiciansLudwigSylowandCarlStørmerdrewup
statutesandrulesfortheproposedprize.However,Lie’sinfluencewanedafterhisdeath,andthedissolutionoftheunion
betweenSwedenandNorwayin1905endedthefirstattempttocreateanAbelPrize.
[5]EötvösLorándUniversity: EötvösLorándUniversity(,ELTE)isaHungarianpublicresearchuniversitybasedin 0
Budapest.Foundedin1635,ELTEisoneofthelargestandmostprestigiouspublichighereducationinstitutionsinHungary.
The28,000studentsatELTEareorganizedintoeightfaculties,andintoresearchinstituteslocatedthroughoutBudapestand
onthescenicbanksoftheDanube.ELTEisaffiliatedwith5Nobellaureates,aswellaswinnersoftheWolfPrize,Fulkerson
PrizeandAbelPrize,thelatestofwhichwasAbelPrizewinnerEndreSzemerédiin2012.
[6]AbelPrize:AnyonemaysubmitanominationfortheAbelPrize,however,self-nominationsarenotpermitted.The 0
nomineemustbealive;however,iftheawardeediesafterbeingdeclaredasthewinner,theprizewillbeawardedposthumously.
[7]AbelPrize:TheNorwegianAcademyofScienceandLettersdeclaresthewinneroftheAbelPrizeeachMarchafter 0
recommendationbytheAbelCommittee,whichconsistsoffiveleadingmathematicians. BothNorwegiansandnon-
NorwegiansmayserveontheCommittee.TheyareelectedbytheNorwegianAcademyofScienceandLettersandnominated
bytheInternationalMathematicalUnionandtheEuropeanMathematicalSociety. Thecommitteeisof2018chairedby
NorwegianmathematicianHansMunthe-Kaas(UniversityofBergen),andwasbeforethat,headedbyProfessorJohnRognes.
[8]HansMunthe-Kaas:Munthe-KaasreceivedExxonMobilAwardforbestPhDatNTNU,1989,andtheCarl-ErikFro¯berg 0
PrizeinNumericalMathematics1996forthepaperL¨ie–ButchertheoryforRunge–KuttaMethods¨.Munthe-Kaasiselected
memberoftheNorwegianAcademyofScienceandLetters,theRoyalNorwegianSocietyofSciencesandLettersand
theNorwegianAcademyofTechnologicalSciences.Munthe-KaasisthechairoftheinternationalAbelprizecommittee
(2018-2022),heisPresidentoftheScientificCouncilofCentreInternationaldeMathématiquesPuresetAppliquées(CIMPA)
(2017–present)andheisEditor-in-ChiefofJournalFoundationsofComputationalMathematics(2017–present).Munthe-Kaas
wassecretaryofFoundationsofComputationalMathematics(2005–2011)andmemberoftheBoardoftheAbelPrizein
Mathematics(2010–2018).
[9]ScienceandtechnologyinHungary:AmongHungary’snumerousresearchuniversities,theEötvösLorándUniversity, 0
foundedin1635,isoneofthelargestandthemostprestigiouspublichighereducationinstitutionsinHungary.The28,000
studentsatELTEareorganizedintoeightfaculties,andintoresearchinstituteslocatedthroughoutBudapest.ELTEisaffiliated
with5Nobellaureates,aswellaswinnersoftheWolfPrize,FulkersonPrizeandAbelPrize,thelatestofwhichwasAbel
PrizewinnerEndreSzemerédiin2012.
[10]AbelPrize: TheAbelPrize’shistorydatesbackto1899,whenitsestablishmentwasproposedbytheNorwegian 0
mathematicianSophusLiewhenhelearnedthatAlfredNobel’splansforannualprizeswouldnotincludeaprizein
mathematics. In1902KingOscarIIofSwedenandNorwayindicatedhiswillingnesstofinanceamathematicsprizeto
complementtheNobelPrizes,buttheestablishmentoftheprizewaspreventedbythedissolutionoftheunionbetween
NorwayandSwedenin1905.IttookalmostacenturybeforetheprizewasfinallyestablishedbytheGovernmentofNorway
in2001,anditwasspecificallyintended¨togivethemathematicianstheirownequivalentofaNobelPrize.T¨helaureatesare
selectedbytheAbelCommittee,themembersofwhichareappointedbytheNorwegianAcademyofScienceandLetters.
Table8: Randomlysampledexampleofaqueryon“WhatisthenameofthewinneroftheAbelPrizeof2022?”
andtop-10judgedpassagesinEnglish(en)fromthenon-relevantsubset(testsplit)inNoMIRACL.Titlesofeach
passagearemarkedinbold. Therelevancejudgmenthasbeenannotatedmanuallybyanativespeaker.

Query JudgedPassages Relevance
In which coun- [1]PraiadosPescadores(Albufeira):PraiadosPescadoresorthe“FishermansBeach”isablueflagbeachontheAtlantic 1
try Praia dos southcoastoftheAlgarve,inthedistrictofBairrodosPescadores(NeighborhoodoftheFisherman),Albufeirawhichis
Pescadoresis? withintheMunicipalityofAlbufeira,Portugal.Thebeachisoneofthetwobeacheswhichfrontthetownof“Albufeira”with
“PraiadoTúnel”atthewesternendand“PraiadosPescadores""lyingtotheeasternendofthetownsseafront.Thetownand
itsbeachesarelocatedwestbyroadoftheregionscapitalofFaro.InthedaysbeforeAlbufeirahadaharbourandmarinerthe
“PraiadosPescadores”waswhereallthelocalfishermenoperatedfromandthebeachscenewouldhavebeenverydifferentto
thesiteyouseetoday.Thenthebeachwouldhavebeenfullofbrightlypaintedfishingboatspulleduponthisbeachwhennot
atseaandmuchofthetouristactivitiestookplaceonthe“PraiadoTúnel”.Todaythe“PraiadosPescadores”isnowusedfor
tourismandisaverybusybeachespeciallyinthesummerseason.
[2]PraiadoTúnel(Peneco):PraiadoTúnelisabeachontheAtlanticsouthcoastoftheAlgarve,inthetownofAlbufeira 0
whichiswithintheMunicipalityofAlbufeira,Portugal.Thebeachisalsoknownas“PraiadoPeneco”andisoneofthetwo
beacheswhichfrontthetownof“Albufeira”with“PraiadoTúnel”atthewesternendand“PraiadosPescadores”lyingtothe
easternendofthetownsseafront.ThetownanditsbeachesarelocatedwestbyroadoftheregionscapitalofFaro.Thebeach
getsitsnamefroma20meterlongtunnelnexttothetouristofficeinthemiddleofAlbufeirawhichcutsthroughthecliffs
linkingthetownssquaretothebeach.Atthewesternendofthebeachthereisapromenadewhichendsatthecaveknownas
theXorinoGrotto.Accordingto13th-centurylegend,thecavewasusedasshelterbytheMoorsaftertheChristianconquest
ofAlbufeira.Aswellasthetunnelthereareseveralotherpointsofaccesstothebeachincludingalift,rampsandsteps[...]
[3]PraiadosPescadores(Albufeira):Thebeachisinlengthandiswideatlowtide.Thebeachisdividedbyaprotruding 0
clifffromPraiadoTúnelatthewesternendoftheseafront.TothebeacheseasternboundaryisthePraiadoInatelanditis
dividedfromthatbeachbyaconcretepierwhichcoverstheoutflowoftheRibeiradeAlbufeira(AlbufeiraRiver).Thereare
alsocliffsattheeasternendandtothebackofthebeachthereisanamphitheatreofwhitehousesofthedistrictofBairrodos
Pescadores.ThebeachcanalsobeaccessedbyanoutdoorfootescalatorfromthePaudaBandeirablufflocatedsouthof
BairrodosPescadoresdowntothebeachandAlbufeiraoldtown.
[4]PraiadosPescadores(Albufeira):PraiadosPescadoresisaneasilyaccessedbeachwithitslargehardsurfacesquareat 0
beachlevel.Therearetwocarpark’snear-by,oneofwhich,isatbeachlevel,ashortdistancealongtheAvenida25deAbril
withintheoldtown.ThesecondcarparkisatthetopofthecliffsatBairrodosPescadoresandisaccessedviatheoutdoor
escalator.Tothebackofthewesternendofthebeachthereavarietyofrestaurantsmanyofwhichspecialiseinthelocalfish
andseafood.Thebeachhasseverallicensedconcessionswithopportunitiestohireparasolsandsunloungers.Thereare
alsomanyorganisedbeachandwatersportconcessionsfromvolleyballtoboattripsandParasailing.Thebeachalsohas
toiletandshowerfacilities.Duringthesummermonthsthebeachispatrolledbylifeguards.Inrecentyearsthebeachhas
beenthefocalpointforthenewyearcelebrationsinthetown.AtemporaryconcertstageiserectedontheLargo25deAbril
andconcertsareheldtocelebratethenewyear.Inthepastthecelebrationhasseeninternationalbandsappearingsuchas
Britishreggae/popbandUB40in2009.Thecelebrationscumulatewithafireworkdisplayheldjustofthebeachonboatsand
pontoonsjustoftheshoreline.
[5]PraiadoPenedo:PraiadoPenedoisabeachwithintheMunicipalityofAljezur,intheAlgarve,Portugal.Thebeachis 0
onthewesternSeaboardinthenorthwestoftheAlgarve.ThebeachissouthwestofthevillageofAljezur,andisnorthwest,
byroad,fromtheregionscapitalofFaro.ThebeachofPraiadoPenedoisinsidetheVicentineCoastNaturalPark,anareaof
outstandingnaturalbeauty.
[6]PraiadoNorte:PraiadoNorteisacivilparishofthemunicipalityofHorta,locatedalongthenortherncoastbetween 0
CedrosandCapelo,onthePortugueseislandofFaial,inthearchipelagooftheAzores.Thepopulationin2011was250,inan
areaof.Itistheleastpopulousparishontheisland,reachedalongtheËstradaRegionalË.R.1-1ªregionalroadwayfromthe
urbancentreofHorta.
[7]PraiadasConchas,SãoToméandPríncipe:PraiadasConchasisasettlementinthewesternpartoftheLobataDistrict 0
onSãoToméIslandinSãoToméandPríncipe.Itspopulationis174(2012census).Establishedasaplantation(¨roça¨),Praia
dasConchaslies2kmfromthecoast,3kmwestofGuadalupe.ThereisasmallerseasidesettlementalsocalledP¨raiadas
Conchas¨,3.5kmtothenorth.
[8]PraiadasGatas:PraiadasGatas(Portuguesemeaningb¨eachofthecats¨)isasandybeachinthenortheasternpartof 0
theislandofBoaVistainCapeVerde.ThenearestvillageisFundodasFigueiras,5kmtothesouthwest.Itformsapartof
NorthernNaturePark(P¨arqueNaturaldoNorte¨).ThesmallislandIlhéudosPássarosliesoffthecoastatthePraiadasGatas.
[9]Praia(SantaCruzdaGraciosa):Praia(officiallySãoMateusdaPraia)isaPortuguesecivilparishinthemunicipalityof 0
SantaCruzdaGraciosa,ontheislandofGraciosa,intheAzores.Itstillretainsitsformernamelocally,owingtotheparish
havingoncebeenthehistoricalmunicipalityofPraia.Thepopulationin2011was836,inanareaof12.82km².
[10]PraiaHarbor:PraiaHarbor()istheportofthecityofPraiainthesouthernpartoftheislandofSantiago,CapeVerde. 0
ItissituatedinanaturalbayoftheAtlanticOcean.Sincethelatestmodernizationin2014,ithas2longquays,3shorter
quays,aquayforfishingboatswithfishprocessinginstallations,2containerparks,2roll-on/roll-offramps,andapassenger
terminal.Thetotallengthofthequaysis863m,andthemaximumdepthis13.5m.TheportofPraiaplayedanimportant
roleinthecolonizationofAfricaandSouthAmericabythePortuguese.With817,845metrictonnesofcargoand85,518
passengershandled(2017),itisthesecondbusiestportofCapeVerde,afterPortoGrande(Mindelo).
Table9: Randomlysampledexampleofaqueryon“InwhichcountryPraiadosPescadoresis?” andtop-10judged
passagesinEnglish(en)fromtherelevantsubset(testsplit)inNoMIRACL.Titlesofeachpassagearemarkedin
bold. Therelevancejudgmenthasbeenannotatedmanuallybyanativespeaker.