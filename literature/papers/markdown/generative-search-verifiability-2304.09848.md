|     |     | Evaluating |              | Verifiability |     | in          | Generative |            | Search | Engines |     |     |
| --- | --- | ---------- | ------------ | ------------- | --- | ----------- | ---------- | ---------- | ------ | ------- | --- | --- |
|     |     |            | NelsonF.Liu∗ |               |     | TianyiZhang |            | PercyLiang |        |         |     |     |
ComputerScienceDepartment
StanfordUniversity
nfliu@cs.stanford.edu
Abstract
What are the latest discoveries from the James Webb
Space Telescope?
Generativesearchenginesdirectlygeneratere-
The James Webb Space Telescope is designed to peer
sponsestouserqueries,alongwithin-lineci- into the dusty clouds of gas where stars and planetary
systems are born. Webb has captured the first direct
| 3202 tcO 32  ]LC.sc[  2v84890.4032:viXra | tations. | A prerequisite |     | trait of | a trustworthy |     |     |     |     |     |     |     |
| ---------------------------------------- | -------- | -------------- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
image of an exoplanet, and the Pillars of Creation in the
generative search engine is verifiability, i.e., Eagle Nebula[1][2]. Additionally, the telescope will be
systemsshouldcitecomprehensively(highci- used to study the next interstellar interloper[3].
(*Some generated statements may not be fully supported by
tationrecall;allstatementsarefullysupported citations, while others are fully supported.)
bycitations)andaccurately(highcitationpre-
Cited Webpages
cision;everycitesupportsitsassociatedstate-
[1]:     nasa.gov (     citation does not support its associated statement)
|     | ment). | Weconducthumanevaluationtoaudit |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
NASA's Webb Confirms Its First Exoplanet
fourpopulargenerativesearchengines—Bing ... Researchers confirmed an exoplanet, a planet that orbits another
star, using NASA’s James Webb Space Telescope for the first time. ...
|     | Chat, NeevaAI, | perplexity.ai, |     | and | YouChat— |     |     |     |     |     |     |     |
| --- | -------------- | -------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
[2]:     cnn.com (     citation partially supports its associated statement)
acrossadiversesetofqueriesfromavarietyof
Pillars of Creation: James Webb Space Telescope ...
sources (e.g., historical Google user queries, ... The Pillars of Creation, in the Eagle Nebula, is a star-forming region
captured in a new image (right) by the James Webb Space Telescope
|     | dynamically-collected |     | open-ended |     | questions |     |     |     |     |     |     |     |
| --- | --------------------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
that reveals more detail than a 2014 image (left) by Hubble ...
|     | onReddit,etc.). | Wefindthatresponsesfrom |     |     |     |     |     |     |     |     |     |     |
| --- | --------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[3]:     nasa.gov (     citation fully supports its associated statement)
existing generative search engines are fluent Studying the Next Interstellar Interloper with Webb
and appear informative, but frequently con- ...Scientists have had only limited ability to study these objects once
discovered, but all of that is about to change with NASA's James
Webb Space Telescope...The team will use Webb's spectroscopic
tainunsupportedstatementsandinaccurateci-
capabilities in both the near-infrared and mid-infrared bands to study
tations: onaverage,amere51.5%ofgenerated two different aspects of the interstellar object.
sentencesarefullysupportedbycitationsand
only74.5%ofcitationssupporttheirassociated Figure1:Generativesearchenginesansweruserqueries
sentence. Webelievethattheseresultsarecon- by generating a tailored response, along with in-line
|     |           |         |         |      |           |     | citations. | However, | not all | generated | statements | are |
| --- | --------- | ------- | ------- | ---- | --------- | --- | ---------- | -------- | ------- | --------- | ---------- | --- |
|     | cerningly | low for | systems | that | may serve | as  |            |          |         |           |            |     |
a primary tool for information-seeking users, fully supported by citations (citation recall), and not
especiallygiventheirfacadeoftrustworthiness. everycitationsupportsitsassociatedstatement(citation
precision).
|     | We hope | that our | results | further | motivate | the |     |     |     |     |     |     |
| --- | ------- | -------- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
developmentoftrustworthygenerativesearch
enginesandhelpresearchersandusersbetter
understandtheshortcomingsofexistingcom- [Bing]Chatdaily”,andthatBingChatserved45
mercialsystems. millionchatsinthefirstmonthofitspublicpreview
|     |     |     |     |     |     |     | (Mehdi,2023). |     | Generativesearchengineshavethe |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------------------------ | --- | --- | --- |
1 Introduction
|     |     |     |     |     |     |     | potential | to transform | how | people | find informa- |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ------ | ------------- | --- |
tiononline,butgeneratedresponsesfromexisting
Generativesearchenginesfulfilluserinformation
largelanguagemodel-backedgenerativesearchen-
|     | needs by | directly generating |     | responses |     | to input |     |     |     |     |     |     |
| --- | -------- | ------------------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
ginesmaynotalwaysbeaccurate(Maynezetal.,
|     | queries, along | with | in-line | citations | (Figure | 1).1 |     |     |     |     |     |     |
| --- | -------------- | ---- | ------- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- |
2020). Giventheirpotentialandrapidmainstream
Existinggenerativesearchenginesarerapidlygain-
adoption,itiscriticaltoevaluatethesesystemsto
ingusers—inMarch2023,Microsoftreportedthat
betterunderstandtheirpotentiallimitations(akin
“roughlyonethirdofdailypreviewusersareusing
|     |     |     |     |     |     |     | to prior | work | in algorithmic | auditing; | Metaxas |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------------- | --------- | ------- | --- |
*Thisworkwouldnotbepossiblewithoutthe34annotators andPruksachatkun,2017;BuolamwiniandGebru,
whoperformedhumanevaluation; wethankthemfortheir 2018;KiritchenkoandMohammad,2018;Robert-
contributions.
|     |              |                                       |     |     |     |     | son et al., | 2018; | Metaxa | et al., | 2019; Green | and |
| --- | ------------ | ------------------------------------- | --- | --- | --- | --- | ----------- | ----- | ------ | ------- | ----------- | --- |
|     | 1Incontrast, | conventionalsearchenginesarelimitedto |     |     |     |     |             |       |        |         |             |     |
Chen,2019;Birhaneetal.,2022,interalia).
retrievingpre-existingwebpages.

Aprerequisitetraitofatrustworthygenerative knowledgeabouttheJamesWebbSpaceTelescope
search engine is verifiability,2 that is, each gen- (motivating a query about its recent discoveries)
erated statement about the external world should will likely struggle to identify unsupported state-
befullysupportedbyasetofin-linecitations,and mentsinthegeneratedresponse. Wehypothesize
eachprovidedcitationshouldsupportitsassociated thatcitationprecisionisinverselycorrelatedwith
statement. Verifiability enables readers to easily perceivedutilitybecausegenerativesearchengines
checkthatanygeneratedstatementissupportedby often copy or closely paraphrase from their cited
itscitedsource. webpages (§4.4). This improves citation preci-
We conduct a human evaluation to audit four sionbecausecopiedtextisoftensupportedbythe
popular commercial generative search engines citedwebpage,butdecreasesperceivedutilitywhen
(BingChat,NeevaAI,perplexity.ai,andYouChat) copiedstatementsareirrelevanttothequeryorthe
acrossadiversesetofinformation-seekingqueries restofthegeneratedresponse.
(e.g., various types of historical Google user Wemakethefollowingcontributions: first,we
queriesfromNaturalQuestions(Kwiatkowskietal., definethecitationrecallandcitationprecisioneval-
2019), dynamically-collected open-ended ques- uationmetrics,whichaimtoencouragethedevel-
tionsfromReddit;seeAppendixAforexamples). opmentofsystemsthatcitecomprehensivelyand
For each query-response pair, we use human correctly. Second,weconductahumanevaluation
evaluationtomeasureavarietyofdimensions: offourpopulargenerativesearchengines,finding
1. fluency (whether the generated text is fluent thatresponsesarebroadlyfluentandappearuseful,
andcohesive;§2.2); butfrequentlycontainunsupportedstatementsand
2. perceived utility (whether the generated an- inaccurate citations, increasing their potential to
swerishelpfulandinformative;§2.2); mislead users. Third, we observe that perceived
3. citation recall (the proportion of generated utilityisinverselycorrelatedwithcitationprecision
statements about the external world that are inexistinggenerativesearchengines,andhypothe-
fullysupportedbytheircitations;§2.3);and sizethatthisinversecorrelationoccurswhensome
4. citationprecision(theproportionofgenerated systemscopyorcloselyparaphrasefromcitedweb-
citations that support their associated state- pages. To facilitate further work on developing
ments;§2.4). trustworthygenerativesearchengines,wehavere-
Atrustworthygenerativesearchengineshould leasedourhumanevaluationannotations.3
achievehighcitationrecallandprecision,indicat-
ingthatitsgeneratedcitationsarecomprehensive 2 HumanEvaluationofFluency,
(every generated statement is fully supported by PerceivedUtility,andVerifiability
citation) and correct (every citation supports its
Inthissection,weformalizetheinputsandoutputs
associatedstatement).
ofthegenerativesearchengineswestudy,describe
Wefindthatexistinggenerativesearchenginere-
theevaluationoffluencyandperceivedutility,and
sponsesoftenhavehighfluencyandperceivedutil-
defineanddescribetheevaluationofcitationrecall
ity(§4.1),butfrequentlycontainunsupportedstate-
andprecision. Citationrecallandprecisionarede-
ments or inaccurate citations (low citation recall
signedtorewardsystemsthatcitecomprehensively
andprecision;§4.2). Onaverage,merely51.5%of
(i.e.,highrecall;allstatementsarefullysupported
generatedsentencesarefullysupportedwithcita-
bycitations)andaccurately(i.e.,highprecision;ev-
tions(citationrecall),andonly74.5%ofcitations
erycitesupportsitsassociatedstatement). Wealso
support their associated sentence (citation preci-
definecitationF ,ametricthatcombinescitation
sion). Furthermore,citationprecisionisinversely 1
precisionandcitationrecall.
correlated withperceivedutility(r = −0.96);the
responses that seem more helpful are often those
2.1 TaskFormulation
with inaccurate citations (§4.3). This facade of
Givenauserqueryq asinput,agenerativesearch
trustworthinessincreasesthepotentialforexisting
engineproducesatextresponser,whichisastring
generative search engines to mislead users. For
withembeddedin-linecitations. Fortheexamplein
example,inFigure1,auserwithlittlebackground
Figure1,thequeryq is“Whatarethelatestdiscov-
2WeadoptthetermverifiabilityfromtheWikipediacom-
munity. VerifiabilityisacorecontentpolicyofWikipedia: 3github.com/nelson-liu/evaluating-verifiability-in-
statementsmustbefullysupportedbyprovidedsources. generative-search-engines

eriesfromtheJamesWebbSpaceTelescope?” and First generated statement [1✅][2❌][3⚠].
theresponser isthestringparagraph“TheJames Second generated statement [1✅][2❌][4❌].
Third generated statement [4✅][5⚠].
WebbSpaceTelescope... usedtostudythenextin-
Citation Recall: 3/3 = 100%
terstellarinterloper[3].”,withembeddedcitations Citation Precision: 3/8 = 37.5%
“[1]”,“[2]”,and“[3]”.
First generated statement [1⚠][2⚠].
To evaluate citation precision and recall, we Second generated statement [2❌].
Third generated statement.
first segment the r into a set of n statements
Citation Recall: 1/3 = 33%
S = {s 1 ,...,s n }. In this work, the segmenta- Citation Precision: 2/3 = 66%
tion S is set of sentences in the response r. For
First generated statement [1✅][2✅][3❌].
each statement s ∈ S, we construct a (possibly Second generated statement.
i
Third generated statement.
empty) set C = {c ,...,c } of k citations as-
i i,1 i,k
Citation Recall: 1/3 = 33%
sociated with the statement s i , where c i,j is the Citation Precision: 2/3 = 66%
jthcitationassociatedwiththeithresponsestate-
: highlighted statement is fully supported by citations
ment. For each citation c , we have a URL u : highlighted statement is not fully supported by citations.
i,j i,j
anditscontentsp i,j . Inthiswork,C i issetofcita- ✅: citation fully supports its associated statement.
tionsthatoccurins (e.g.,fors =“Blueberries[1], ⚠: citation partially supports its associated statement.
i i ❌: citation does not support its associated statement.
cherries[2],andgrapes[3]growontrees.[4]”,C =
i
{[1],[2],[3],[4]}). Figure 2: Examples of calculating citation recall and
In practice, a sentence may contain multiple precision. Citation recall measures the proportion of
generatedstatementsthataresupportedbycitations. Ci-
independently-verifiable claims (e.g., conjuncts
tationprecisionmeasurestheproportionofcitationsthat
such as “Cups can be made of glass[1] or plas-
supporttheirassociatedstatements.Partially-supporting
tic[2].”), and a single in-line citation’s scope is
citationsonlyimprovecitationprecisionwhentheiras-
oftenambiguous(e.g.,acitemarkeraftertwostate-
sociatedstatementissupportedbytheunionofitscita-
ments could be interpreted as either supporting tionsandnootherassociatedcitationfullysupportsthe
bothstatements,ormerelythefinalone);weleave statementbyitself(middleexample).
finer-grainedevaluationtofuturework.
that are not verification-worthy. We take the
2.2 MeasuringFluencyandPerceivedUtility
position that every generated statement about
To measure response fluency, annotators were
the external world is verification-worthy, even
showntheuserquery,thegeneratedresponse,and
those that might seem obvious, trivially true, or
the claim “The response is fluent and cohesive”.
“common sense”. Generated statements may be
Weaskannotatorstoratetheirlevelofagreement
incorrect, and statements that seem obvious to
with the claim on a five-point Likert scale from
some readers may be less than obvious to others
Strongly Disagree to Strongly Agree. We use a
(e.g., “The Pope is Catholic”). We believe that
similarprocesstomeasureperceivedutility,asking
systems should aim to provide a source for all
annotatorstoratetheirlevelofagreementwiththe
generated statements about the external world,
claim“Theresponseisahelpfulandinformative
enablingreaderstoeasilyverifyanystatementina
answertothequery”.
generatedresponse.
In practice, almost all system-generated state-
2.3 MeasuringCitationRecall
mentsareverification-worthy—notableexceptions
Citation recall is the proportion of verification- includestatementsaboutthespeaker(thesystem)
worthystatementsthatarefullysupportedbytheir itself (e.g., “As a language model, I do not have
associated citations (see Figure 2 for several ex- the ability to ban books.”) and questions posed
amples). Thus,computingcitationrecallrequires totheuser(e.g.,“Wouldyouliketolearnmore?”,
(i) identifying the verification-worthy statements generatedbysystemslikeBingChatandYouChat
in a response and (ii) evaluating whether each thataredeployedinconversationalsettings).
verification-worthystatementisfullysupportedby
Evaluatingwhetheraverification-worthystate-
itsassociatedcitations.
ment is fully supported by its associated cita-
Identifying verification-worthy statements. tions. Giventheverification-worthystatements
GiventhestatementsS inaresponser,wefirstask inaresponser,annotatorsevaluatewhethereach
annotators to remove statements in the response statementisfullysupportedbyitsassociatedcita-

tions (see the sentences of generated response in in the response. Then, the citation precision is
| Figure | 1 for | examples). | To  | collect | these | binary | (T +T | )/N. |     |     |     |     |
| ------ | ----- | ---------- | --- | ------- | ----- | ------ | ----- | ---- | --- | --- | --- | --- |
fs ps
| judgments, | we  | use | the attributable |     | to  | identified |     |     |     |     |     |     |
| ---------- | --- | --- | ---------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
2.5 CitationF
| sources        | (AIS) | evaluation     | framework |             | of  | Rashkin    |           | 1                                   |     |     |     |     |
| -------------- | ----- | -------------- | --------- | ----------- | --- | ---------- | --------- | ----------------------------------- | --- | --- | --- | --- |
| et al. (2022). |       | In particular, |           | a statement |     | s is fully | CitationF |                                     |     |     |     |     |
|                |       |                |           |             |     | i          |           | 1 isametricthatcombinescitationpre- |     |     |     |     |
supportedbyitsassociatedcitationsC ifageneric cisionandcitationrecallbytakingtheirharmonic
i
| hearer         | would | affirm | the statement |     | “According | to     | mean: |     |     |     |     |     |
| -------------- | ----- | ------ | ------------- | --- | ---------- | ------ | ----- | --- | --- | --- | --- | --- |
| cited webpages |       | C i ,  | s i ”, within | the | context    | of the |       |     |     |     |     |     |
citationprecision·citationrecall
| queryqandresponser,andunsupportedotherwise. |     |     |     |     |     |     | F = | 2·  |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
citationprecision+citationrecall
2.4 MeasuringCitationPrecision
|     |     |     |     |     |     |     | ToachieveahighcitationF |     |     | ,systemsmusthave |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---------------- | --- | --- |
1
Citation precision is the proportion of generated highcitationprecisionand highcitationrecall.
| citations | that | support | their | associated |     | statements |     |     |     |     |     |     |
| --------- | ---- | ------- | ----- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(Figure 2). In contrast to citation recall, citation 3 EvaluationSetup
precisionrewardssystemsforcitingaccurately—a
Inthissection,wedescribetheevaluatedgenerative
responsethatciteseverywebpageontheInternet
|     |     |     |     |     |     |     | search engines | (§3.1), | the | diverse | query | distribu- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --- | ------- | ----- | --------- |
foreachgeneratedstatementwouldhavehighcita-
tionsweuseforevaluation(§3.2),andthedetails
tionrecall,butlowcitationprecision(sincemany
ofourhumanevaluationprotocol(§3.3).
| articles | are irrelevant |     | and do | not | support | their as- |     |     |     |     |     |     |
| -------- | -------------- | --- | ------ | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
sociatedstatement). Tomeasurecitationprecision 3.1 EvaluatedGenerativeSearchEngines
| for a response       |     | r, we   | first ask                | annotators |     | to judge |                |                                 |     |            |     |            |
| -------------------- | --- | ------- | ------------------------ | ---------- | --- | -------- | -------------- | ------------------------------- | --- | ---------- | --- | ---------- |
|                      |     |         |                          |            |     |          | We evaluate    | four existing                   |     | commercial |     | generative |
| whethereachcitationc |     |         | contributesfull,partial, |            |     |          |                |                                 |     |            |     |            |
|                      |     |         | i,k                      |            |     |          | searchengines: | BingChat,NeevaAI,perplexity.ai, |     |            |     |            |
| or no support        |     | for its | associated               | statement  |     | s i (see |                |                                 |     |            |     |            |
|                      |     |         |                          |            |     |          | andYouChat.    | 5 Thesesystemspatternafterprior |     |            |     |            |
citedwebpagesinFigure1forexamples):
work(e.g.,Nakanoetal.,2021;Menicketal.,2022;
| • Full | support: |     | all of the | information |     | in the |        |               |           |     |         |             |
| ------ | -------- | --- | ---------- | ----------- | --- | ------ | ------ | ------------- | --------- | --- | ------- | ----------- |
|        |          |     |            |             |     |        | Glaese | et al., 2022; | Thoppilan |     | et al., | 2022, inter |
statementissupportedbythecitation.
alia)andgenerateresponsesbyconditioninglarge
| • Partial | support: |     | some | of the | information | in  |     |     |     |     |     |     |
| --------- | -------- | --- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
languagemodelsontheinputqueryandretrieved
thestatementissupportedbythecitation,but
|     |     |     |     |     |     |     | content | (e.g., search | results | from | a conventional |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ------- | ---- | -------------- | --- |
otherpartsarenotsupported(e.g.,missingor
|     |     |     |     |     |     |     | search engine). | For | each | input, | we save | the sys- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---- | ------ | ------- | -------- |
contradictory).
|              |     |                              |     |     |     |     | tem’sfirstcompleteresponse(i.e.,single-turn). |              |         |     |               | Re- |
| ------------ | --- | ---------------------------- | --- | --- | --- | --- | --------------------------------------------- | ------------ | ------- | --- | ------------- | --- |
| • Nosupport: |     | thecitationdoesnotsupportany |     |     |     |     |                                               |              |         |     |               |     |
|              |     |                              |     |     |     |     | sponses                                       | were scraped | between |     | late February | and |
partofthestatement(e.g.,thecitedwebpage
lateMarch2023.
iscompletelyirrelevantorcontradictory).
|     |     |     |     |     |     |     | Note | that evaluated | generative |     | search | engines |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ---------- | --- | ------ | ------- |
Forstatementsthathavemultipleassociatedci-
havedifferingabstentionrates(Table1),whichcan
tations,weadditionallyaskannotatorswhetherthe
|     |     |     |     |     |     |     | make direct | comparison |     | difficult—one |     | might ex- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------------- | --- | --------- |
unionofitsassociatedcitedwebpagescollectively
pectthatsystemswithhigherabstentionratesmight
| provides | full | support | for the | statement |     | (a binary |     |     |     |     |     |     |
| -------- | ---- | ------- | ------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
alsohavehigherevaluationperformance,sincethey
| judgment). | Similar |     | to citation | recall, | we  | use the |            |         |      |            |           |     |
| ---------- | ------- | --- | ----------- | ------- | --- | ------- | ---------- | ------- | ---- | ---------- | --------- | --- |
|            |         |     |             |         |     |         | can simply | abstain | from | generating | responses | to  |
AISevaluationframeworkofRashkinetal.(2022)
difficultqueries(wedonotfindthistobethecase
tocollectthesebinaryjudgments.
|              |              |          |            |         |     |             | inpractice).                                 | NeevaAIabstainsfromrespondingon |     |     |     |     |
| ------------ | ------------ | -------- | ---------- | ------- | --- | ----------- | -------------------------------------------- | ------------------------------- | --- | --- | --- | --- |
| To calculate |              | citation | precision, |         | let | T be the    |                                              |                                 |     |     |     |     |
|              |              |          |            |         |     | fs          | nearly23%ofevaluatedqueries,sinceitsresponse |                                 |     |     |     |     |
| number       | of citations |          | that fully | support |     | its associ- |                                              |                                 |     |     |     |     |
atedstatement, andletT bethenumberofcita- itsassociatedcitations[1]and[2].Supposethatthesecitations
ps
eachcontributepartialsupportfortheentirestatement—the
tionsthatpartiallysupportsitsassociatedstatement,
firstcitation[1]onlystatesthat“Healthbenefitsofcycling
wheretheassociatedstatementisfullysupported includeimprovedcardiovascularhealth”,andsecondcitation
bytheunionofitsassociatedcitationsandnoas- [2]onlystatesthat“Healthbenefitsofcyclingincludelowered
cholesterollevels”.Takentogether,thecitationsofferfullsup-
| sociated | citation | fully | supports | the | statement | by  |                      |     |                                  |     |     |     |
| -------- | -------- | ----- | -------- | --- | --------- | --- | -------------------- | --- | -------------------------------- | --- | --- | --- |
|          |          |       |          |     |           |     | portforthestatement. |     | Althoughthesecitationsdonotfully |     |     |     |
itself.4
Let N be the total number of citations supportthestatementontheirown, theystillmeaningfully
contributetoitsverifiability—systemsshouldnotbepenalized
4For an intuitive example of when partially-supporting foraggregatinginformationfrommultiplecitations.
citescounttowardimprovingprecision(greaterT ps ),consider 5WedonotevaluateOpenAI’sChatGPTorGoogle’sBard
thestatement“Healthbenefitsofcyclingincludeimprovedcar- becausetheydonotprovidein-linecitationsfortheirresponses
diovascularhealth[1]andloweredcholesterollevels[2].”with (asofMarch2023),andthustriviallyhavelowverifiability.

|     |               |     | AbstentionRate(↓) |       |     |     | (KILT)useshistoricalqueriesfromtheKILTELI5 |                    |         |                |             |        |
| --- | ------------- | --- | ----------------- | ----- | --- | --- | ------------------------------------------ | ------------------ | ------- | -------------- | ----------- | ------ |
|     |               |     |                   |       |     |     | dataset                                    | (Fan et al., 2019; | Petroni |                | et al.,     | 2021), |
|     | BingChat      |     |                   | <0.5% |     |     |                                            |                    |         |                |             |        |
|     | NeevaAI       |     |                   | 22.7% |     |     | drawn from                                 | posts created      | before  | July           | 2018.       | A      |
|     | perplexity.ai |     |                   | <0.5% |     |     |                                            |                    |         |                |             |        |
|     |               |     |                   |       |     |     | retrieval-based                            | system             | could   | hypothetically |             | per-   |
|     | YouChat       |     |                   | <0.5% |     |     |                                            |                    |         |                |             |        |
|     |               |     |                   |       |     |     | form well                                  | on ELI5 (KILT)     | by      | simply         | identifying |        |
thequery’ssourceRedditELI5postandcopying
| Table 1: | Generative | search | engines | may | be designed |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
fordeploymentindifferentcontexts. NeevaAIabstains itscontent. Asaresult,wealsoevaluategenerative
fromrespondingto22.7%ofour1450queries,sinceits searchenginesontheELI5(Live)subdistribution,
responseisdesignedfordisplaywithinaconventional whichincreasesecologicalvaliditybyevaluating
| searchresultspage. |     | Incontrast,theconversationalin- |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
systemsonrealuserqueriesattheirtimeofcreation
terfaceofBingChat,andYouChatmeansthatsystems
andreducingtheincidenceofsearchresultswith
| must generate |     | a response | for | nearly every | input | user |             |                 |     |      |              |     |
| ------------- | --- | ---------- | --- | ------------ | ----- | ---- | ----------- | --------------- | --- | ---- | ------------ | --- |
|               |     |            |     |              |       |      | the query’s | exact keywords. |     | 6 We | continuously |     |
query(excepting,e.g.,querycharacterlengthlimits).
listentothestreamofnewRedditELI5postsand
|              |     |          |              |        |        |     | immediately                         | query generative |     | search | engines | for     |
| ------------ | --- | -------- | ------------ | ------ | ------ | --- | ----------------------------------- | ---------------- | --- | ------ | ------- | ------- |
| is displayed |     | within a | conventional | search | engine |     |                                     |                  |     |        |         |         |
|              |     |          |              |        |        |     | responseswheneveranewpostiscreated. |                  |     |        |         | Thisen- |
resultspage. Incontrast,BingChat,perplexity.ai, suresthatthesourceELI5postwillnothavebeen
andYouChatrespondtoalmosteveryuserquery. indexed(andthus,cannotberetrieved)byconven-
|     |     |     |     |     |     |     | tional search | engines. | minimizing | the | possibility |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ---------- | --- | ----------- | --- |
3.2 EvaluatedQueryDistributions thatthegenerativesearchenginehasaccesstothe
| To gain | a broader | understanding |     | of  | the strengths |     | sourceELI5post. |     |     |     |     |     |
| ------- | --------- | ------------- | --- | --- | ------------- | --- | --------------- | --- | --- | --- | --- | --- |
andweaknessesofexistingcommercialgenerative WikiHowKeywords. We evaluate systems on
search engines, we evaluate on a diverse set of queriesderivedfromWikiHowarticles. Wefound
| queries | from | a variety | of  | sources | (e.g., Google |     |               |          |            |        |     |         |
| ------- | ---- | --------- | --- | ------- | ------------- | --- | ------------- | -------- | ---------- | ------ | --- | ------- |
|         |      |           |     |         |               |     | that directly | querying | generative | search |     | engines |
userqueries,open-endedRedditquestions,how-to with WikiHow article titles yields responses that
queries)requiringknowledgefromseveraldifferent largelyparaphraseorcopytextdirectlyfromWik-
answertypes(e.g.,shorttextualspans,long-form
|     |     |     |     |     |     |     | iHow. As | a result, we | use text-davinci-003 |     |     | to  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | -------------------- | --- | --- | --- |
paragraph, lists, or tables). See Appendix A for paraphrasearticletitles(e.g.,“HowtoCutAnAvo-
examplequeriesfromeachdistribution. Eachsys- cado”)intokeywordqueries(e.g.,“cutavocado”).
temisevaluatedon1450queries—150randomly- NaturalQuestions. We evaluate generative
| sampled | queries | from | each | of AllSouls, | davinci- |     |     |     |     |     |     |     |
| ------- | ------- | ---- | ---- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- |
searchenginesonNaturalQuestions(Kwiatkowski
| debate, | ELI5 | (KILT | / Live), | and WikiHowKey- |     |     |               |          |            |     |       |        |
| ------- | ---- | ----- | -------- | --------------- | --- | --- | ------------- | -------- | ---------- | --- | ----- | ------ |
|         |      |       |          |                 |     |     | et al., 2019) | queries, | stratified | by  | their | answer |
words,and100randomly-sampledqueriesforeach type. NaturalQuestionscontainshistoricalqueries
ofthesevenNaturalQuestionssubdistributions.
|     |     |     |     |     |     |     | issued to | the Google | search | engine | coupled | with |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------ | ------ | ------- | ---- |
AllSouls. We evaluate systems on open-ended longandshortanswersextractedfromWikipedia.
essayquestionstakenfromtheentranceexam(gen- We evaluate on queries from 7 NaturalQuestions
eralpapercomponent)forAllSoulsCollege,Ox- subdistributions: querieswithparagraph-typelong
ford University. These questions cover topics in- answers (i) with and (ii) without short answers,
cludingthearts,science,politics,literature,current queries with list-type long answers (iii) with and
events,andissuesineducationandsport. (iv)withoutshortanswer,querieswithtable-type
|                 |     |                           |     |     |     |     | long answers | (v) with | and | (vi) without |     | short |
| --------------- | --- | ------------------------- | --- | --- | --- | --- | ------------ | -------- | --- | ------------ | --- | ----- |
| davinci-debate. |     | Weevaluatesystemsondebate |     |     |     |     |              |          |     |              |     |       |
topicsgeneratedfromtext-davinci-003. answers, and finally (vii) queries with no long
Togen-
answer(andthusnoshortanswereither).
| erate debate |     | queries, | we follow | the | procedure | of  |     |     |     |     |     |     |
| ------------ | --- | -------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Bakkeretal.(2022);seeAppendixB.1fordetails. Summary. In total, we evaluate existing gener-
|           |         |            |      |              |               |      | ative search                                    | engines | on 12   | total query |              | distribu- |
| --------- | ------- | ---------- | ---- | ------------ | ------------- | ---- | ----------------------------------------------- | ------- | ------- | ----------- | ------------ | --------- |
| ELI5.     | We take | queries    | from | the “Explain |               | Like |                                                 |         |         |             |              |           |
|           |         |            |      |              |               |      | tions. Eightquerydistributionsaretakenfromprior |         |         |             |              |           |
| I’m Five” | (ELI5)  | subreddit, |      | where        | users provide |      |                                                 |         |         |             |              |           |
|           |         |            |      |              |               |      | work (ELI5                                      | (KILT)  | and the | seven       | NaturalQues- |           |
long-formlayperson-accessibleanswerstosubmit-
tionsquerydistributions),whilefourquerydistri-
| tedquestions. |     | Submittedquestionsarerequiredto |     |     |     |     |                                    |     |     |     |           |     |
| ------------- | --- | ------------------------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --------- | --- |
|               |     |                                 |     |     |     |     | butionswereconstructedforthiswork: |     |     |     | AllSouls, |     |
admitobjectiveexplanations,andansweringthem
oftenrequireslong-formtextualresponses. 6ThegoaloftheELI5(Live)subdistributionisnottoiden-
|     |          |     |                  |     |     |      | tifyquerieswithnorelevantwebpagesontheInternet. |     |     |     |     | We  |
| --- | -------- | --- | ---------------- | --- | --- | ---- | ----------------------------------------------- | --- | --- | --- | --- | --- |
| We  | consider | two | subdistributions |     | of  | ELI5 |                                                 |     |     |     |     |     |
recognizethatmanyuserqueriesexpresspreviously-seenin-
| queries: | ELI5 | (KILT) | and | ELI5 (Live). |     | ELI5 |     |     |     |     |     |     |
| -------- | ---- | ------ | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |
formationneeds,eveniftheprecisewordingdiffers.

4 ResultsandAnalysis
| davinci-debate, |     | ELI5 | (Live), | and WikiHowKey- |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
words. Thesediversesettingsprovidebroadcover-
Thissectionpresentstheresultsofourhumaneval-
ageofseveralpotentialusecasesandinformation
uationstudyanddiscussesourmainobservations
needs,helpingusgainacomprehensiveunderstand-
ingofsystems’strengthsandweaknesses. and analyses. We see that fluency and perceived
utilityaregenerallyhighacrossdifferentgenerative
searchengines(§4.1),whilecitationrecallandpre-
3.3 HumanEvaluationProtocol
cisionarequitelow(§4.2),thoughperformancecer-
Annotationprocess. Evaluatingasinglequery- tainlyvariesbysystemandquerydistribution—the
| response | pair | requires | human | annotators | to com- |     |     |     |     |     |     |
| -------- | ---- | -------- | ----- | ---------- | ------- | --- | --- | --- | --- | --- | --- |
lowcitationrecallandprecision,whencombined
| plete a | three-step | The | first step | measures | the re- |     |     |     |     |     |     |
| ------- | ---------- | --- | ---------- | -------- | ------- | --- | --- | --- | --- | --- | --- |
withthefacadeoftrustworthinessfromfluencyand
sponse’sfluencyandperceivedutility(§2.2),and
highperceivedutility,increasethepotentialforex-
the second and third step provide the judgments isting generative search engines to mislead users.
necessarytomeasurecitationrecall(§2.3)andpre-
Ourresultsalsoshowthatcitationprecisionisin-
| cision(§2.4). |     | SeeAppendixCforscreenshotsof |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
verselycorrelatedwithperceivedutilityinexisting
the annotation interface and Appendix D for the generativesearchengines(§4.3). Wehypothesize
annotationguidelines.
|     |     |     |     |     |     | that this | is a byproduct |     | of systems’ | propensity | to  |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ----------- | ---------- | --- |
Annotatorrecruitmentandtraining. Annota- copy or closely paraphrase text from cited web-
tionwasperformedonAmazonMechanicalTurk. pages,whichmayincreasecitationprecisionand
decreaseperceivedutility(§4.4).
Annotatorswerepre-screenedwithaqualification
| study, which |     | required | them | to read | an annota- |     |     |     |     |     |     |
| ------------ | --- | -------- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- |
4.1 FluencyandPerceivedUtility
tionguidelinesdocumentandevaluatefiverepre-
sentative query-response pairs. We individually SeeAppendixFforfullfluencyandperceivedutil-
reviewed submitted annotations for qualification ity results for every generative search engine on
study and provided annotators with personalized eachofourquerydistributions.
feedbacktohelpcorrectanymisconceptionsorcon-
Generatedresponsesarefluentandappearhelp-
| fusionaboutthetask. |     |     | Annotatorswhoperformed |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ful. Averagingacrossallsystemsandresponses
well on the qualification study and demonstrated yields an average rating of 4.48 for fluency and
thoroughunderstandingofthetaskandannotation
|     |     |     |     |     |     | 4.50 for | perceived | utility, | indicating | that | annota- |
| --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | ---------- | ---- | ------- |
guidelineswerepermittedtoparticipateinthemain
torsgenerallyfoundgeneratedresponsesfluentand
roundofhumanevaluation. Weremainedincon- helpfulforansweringtheuser’sinputquery.
| stant contact | with | annotators |     | throughout | the hu- |           |         |     |               |         |     |
| ------------- | ---- | ---------- | --- | ---------- | ------- | --------- | ------- | --- | ------------- | ------- | --- |
|               |      |            |     |            |         | Comparing | fluency |     | and perceived | utility | be- |
manevaluationprocesstoanswerquestionsabout
|                                         |     |     |     |     |          | tween generative |               | search | engines.        | Comparing |     |
| --------------------------------------- | --- | --- | --- | --- | -------- | ---------------- | ------------- | ------ | --------------- | --------- | --- |
| corner-casesandclarifyintendedbehavior. |     |     |     |     | Intotal, |                  |               |        |                 |           |     |
|                                         |     |     |     |     |          | fluency          | and perceived |        | utility ratings | between   | the |
34annotatorsparticipatedinhumanevaluation.
generativesearchengines(aggregatedoverallre-
Annotator compensation. Annotators were sponses),weseethatBingChatreceivesthelowest
| compensated |     | $1.00 per | query-response |     | pair for |     |     |     |     |     |     |
| ----------- | --- | --------- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
fluency/perceivedutilityratings(4.40/4.34),fol-
responses with citations, and $0.38 per query- lowedbyNeevaAI(4.43/4.48),perplexity.ai(4.51
response pair for responses without citations /4.56),andYouChat(4.59/4.62).
($15.00perhour,byconservativetimeestimates).
Comparingfluencyacrossquerydistributions.
| On average, | annotators |     | took | approximately | four |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
Comparingaveragefluencyratingsacrossdifferent
| minutes | to complete |     | all three | steps | for a single |     |     |     |     |     |     |
| ------- | ----------- | --- | --------- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
querydistributions,weseesimilarratingsbetween
query-responsepairforresponsesthatcontainedat
NaturalQuestionsqueriesthathavealonganswer
leastonecitation.
(i.e.,anextractiveanswerofsomelengthexistson
Annotation agreement. Each query-response Wikipedia)andnon-NaturalQuestionsdistributions
pair is annotated once in the human evaluation (4.50vs. 4.47,respectively). Comparingaverage
process. To measure inter-annotator agreement, fluencyratingsbetweenNaturalQuestionssubdistri-
wecollectedthreeannotationsfor250randomly- butions,weseethatgeneratedresponsestoqueries
sampledquery-responsepairs,findinghighagree- that have a short extractive answer are generally
mentrates(greaterthan82.0%pairwiseagreement morefluent(4.55)thanresponsestoquerieswith
and91.0F1foralljudgments;seeAppendixE). onlyalonganswer(4.46)orthosewithoutalong

answer(4.46),perhapsbecauseresponsestoques- pearinformativeanduseful.
tionswithshortanswersaregenerallyshorterand
|     |     |     |     |     |     |     | Comparing | citation | recall |     | and precision | be- |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | --- | ------------- | --- |
oftenonlyrequirefactoidknowledge.
|           |         |              |     |     |              |     | tweengenerativesearchengines. |     |     |     | Citationrecall |     |
| --------- | ------- | ------------ | --- | --- | ------------ | --- | ----------------------------- | --- | --- | --- | -------------- | --- |
| A notable | outlier | distribution |     | is  | NaturalQues- |     |                               |     |     |     |                |     |
andprecisionvariesdramaticallybetweendifferent
tionsquerieswithtable-typelonganswersandno generative search engines. perplexity.ai achieves
| short answers, | where |     | system | responses |     | are dra- |     |     |     |     |     |     |
| -------------- | ----- | --- | ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- |
thehighestaveragerecall(68.7),comparedtoNee-
| matically | less fluent | (average |     | of 4.36 | across | sys- |     |     |     |     |     |     |
| --------- | ----------- | -------- | --- | ------- | ------ | ---- | --- | --- | --- | --- | --- | --- |
vaAI(67.6),BingChat(58.7),andYouChat(11.1).
temsvs. averageof4.48acrossallquerydistribu- Ontheotherhand,BingChatachievesthehighest
tions). Thesechallengingqueriesoftenrequireag-
averageprecision(89.5),followedbyperplexity.ai
gregatinginformationacrosstablecellsorretrieved
|          |           |      |            |        |     |         | (72.7),NeevaAI(72.0),andYouChat(63.6). |     |     |     |     | Agap |
| -------- | --------- | ---- | ---------- | ------ | --- | ------- | -------------------------------------- | --- | --- | --- | --- | ---- |
| sources, | since the | lack | of a short | answer |     | implies |                                        |     |     |     |     |      |
ofnearly58%separatesthesystemwiththehigh-
thatnosingleWikipediatablecelldirectlyanswers est and lowest recall (perplexity.ai vs. YouChat),
thequestion(e.g.,thequery“howmanygrammys
andthegapbetweenthesystemswiththehighest
| doesbeyoncehavewithoutdestiny’schild”). |     |     |     |     |     | When |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
andlowestprecisionisalmost25%(BingChatvs.
| the retrieved | webpages |     | do not | contain | a clear | ex- | YouChat). |     |     |     |     |     |
| ------------- | -------- | --- | ------ | ------- | ------- | --- | --------- | --- | --- | --- | --- | --- |
tractiveanswertothequery,butcontainfactsthat
|               |         |             |              |       |           |        | Comparing      | citation  | recall    | across     | query  | distri-   |
| ------------- | ------- | ----------- | ------------ | ----- | --------- | ------ | -------------- | --------- | --------- | ---------- | ------ | --------- |
| seem relevant | (e.g.,  | information |              | about | Destiny’s |        |                |           |           |            |        |           |
|               |         |             |              |       |           |        | butions.       | Modifying | the       | evaluation | query  | distri-   |
| Child’s first | Grammy, |             | or Beyonce’s |       | total     | number |                |           |           |            |        |           |
|               |         |             |              |       |           |        | bution appears |           | to affect | citation   | recall | more than |
ofcareerGrammyawards),thegeneratedresponse
|     |     |     |     |     |     |     | citation precision. |     | For | example, | the | gap in cita- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | -------- | --- | ------------ |
isoftenastiltedagglomerationofstatementsfrom
tionrecallbetweenNaturalQuestionsquerieswith
varioussources,reducingoverallfluency.
|     |     |     |     |     |     |     | a long answer | and | non-NaturalQuestions |     |     | queries |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------------- | --- | --- | ------- |
Comparingperceivedutilityacrossquerydistri- isnearly11%(58.5vs. 47.8,respectively). Simi-
| butions. | Incontrasttofluency,perceivedutility |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
larly,thedifferenceincitationrecallbetweenNat-
candiffersubstantiallybetweendifferentquerydis- uralQuestions queries with and without short an-
tributions. Perceived utility is much higher for swersisnearly10%(63.4forquerieswithashort
NaturalQuestionsqueriescontainingalonganswer
answer,53.6forquerieswithonlyalonganswer,
(4.59),asopposedtonon-NaturalQuestionsqueries
and53.4forquerieswithnolongorshortanswer).
(4.43). ComparingbetweendifferentNaturalQues- Wehypothesizethatcitationrecallisdrivenby
tions subdistributions, we see that perceived util- the relevance of retrieved webpages. In the ab-
ityishighestforqueriesthathaveashortanswer
|     |     |     |     |     |     |     | sence of | retrieved | evidence | that | directly | answers |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | ---- | -------- | ------- |
(4.62),followedbyqueriesthathaveonlyalongan-
theinputuserquery,systemsgeneratestatements
swer(4.55),andfinallybyqueriesthathavenolong that are unsubstantiated by citations, resulting in
| (orshort)answer(4.52). |     |     | Overall,perceivedutility |     |     |     |               |     |          |            |     |            |
| ---------------------- | --- | --- | ------------------------ | --- | --- | --- | ------------- | --- | -------- | ---------- | --- | ---------- |
|                        |     |     |                          |     |     |     | lower recall. | For | example, | generative |     | search en- |
decreasesasqueriesrequirelonger-formandless-
ginesstrugglewithcitationrecallwhenevaluated
extractiveanswers(e.g.,factoidNaturalQuestions ontheopen-endedAllSoulsessayquestions(aver-
querieswithshortanswersversusELI5queries).
agerecallof44.3),becausethesequeriesgenerally
havenoextractiveanswerontheInternet.
4.2 CitationRecallandPrecision
|     |     |     |     |     |     |     | Comparing | citation | precision |     | across | query |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | --- | ------ | ----- |
SeeAppendixGforfullcitationrecallandpreci-
|     |     |     |     |     |     |     | distributions. |     | Precision | on  | NaturalQuestions |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ---------------- | --- |
sionresultsforeverygenerativesearchengineon
|     |     |     |     |     |     |     | queries with | long | answers | is  | higher | than non- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------- | --- | ------ | --------- |
eachofourquerydistributions. NaturalQuestions distributions (76.1 vs. 72.3, re-
Existinggenerativesearchenginesoftendonot spectively). Precision is highest on NaturalQues-
citecomprehensivelyorcorrectly. Whenaver- tionsquerieswithparagraphanswertypes(preci-
aging across all systems, a mere 51.5% of gener- sion of 81.5 when a short answer exists and 78.7
atedstatementsarefullysupportedwithcitations whenonlyalonganswerexists). Ontheotherhand,
(recall),andonly74.5%ofcitationsfullysupport citationprecisionislowestwhensystemsareevalu-
theirassociatedstatements(precision). Webelieve atedonAllSoulsopen-endedessayquestions(67.8)
theseresultsareunacceptablylowforsystemsthat anddavinci-debatequeries(70.3). Comparingbe-
are quickly becoming a popular tool for answer- tweenNaturalQuestionssubdistributions,average
inguserqueriesandalreadyhavemillionsofusers, system precision is higher on queries with short
especiallygiventhatgeneratedresponsesoftenap- answers(77.4)thanthosewithonlylonganswers

YouChat Is cooperation or competition the driving force guiding
|     | ytilitU deviecreP 4.6 |     |     |     |     |     | the evolution of society? |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
perplexity.ai
Bing Chat
(higher citation precision, lower perceived utility)
4.5 NeevaAI There are different opinions on this topic. Some researchers
believe that cooperation, not struggle for survival, drives
evolution [1]. Others think that there are two driving forces
of evolution: mutation (change) and competition [2]. What
4.4
do you think?
|     |     |     |     | Bing Chat |     | (*Some generated statements may not be fully supported by  |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
citations, while others are fully supported.)
|     | 20  |     | 40  | 60  |     | Cited Webpages |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
Citation F
1
[1]:     phys.org
(     citation fully supports its associated statement)
Figure3: Averagedperceivedutilityplottedagainstav- Cooperation, not struggle for survival, drives evolution
Researchers believe that competition tends to differentiate
eragedcitationF foreachevaluatedgenerativesearch ecological requirements ... A new conceptual evolutionary
1
engine. Differentsystemsmakedifferenttrade-offsbe- model ... reviewed the debated mechanism of speciation,
suggesting that competition and a struggle for existence are not
tweenperceivedutilityandcitationF 1 . Notethatthese the main drivers of evolution.
| systemsaredifficulttodirectlycomparesincetheymay |     |     |     |     |     | [2]:     cooperation.cool |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- |
havedifferentabstentionrates(Table1). (     citation fully supports its associated statement)
Game Theory - Cooperation is cool
Lots of biologists consider evolution as a continuous struggle
for survival. They think that there are two driving forces of the
evolution: mutation (change), and competition.
(74.8)ornolonganswer(73.5).
| Summary. |     |     |     |     |     | Figure4: | Citationprecisionisinverselycorrelatedwith |     |     |     |
| -------- | --- | --- | --- | --- | --- | -------- | ------------------------------------------ | --- | --- | --- |
Tosummarizeourhumanevaluation
perceivedutilityinexistinggenerativesearchengines.
| results, | Figure | 3 plots | average | perceived | utility |     |     |     |     |     |
| -------- | ------ | ------- | ------- | --------- | ------- | --- | --- | --- | --- | --- |
BingChatoftenachieveshighcitationprecisionbecause
| againstaveragecitationF |     |     | . Existingsystemsmake |     |     |            |             |      |                |           |
| ----------------------- | --- | --- | --------------------- | --- | --- | ---------- | ----------- | ---- | -------------- | --------- |
|                         |     |     | 1                     |     |     | it closely | paraphrases | from | cited webpages | (bolded). |
differenttrade-offsbetweencitationrecall,citation However,sincethesecitationsarelargelyirrelevantto
| precision, | andperceivedutility. |     |     | SeeAppendixH |     |                                            |     |     |     |          |
| ---------- | -------------------- | --- | --- | ------------ | --- | ------------------------------------------ | --- | --- | --- | -------- |
|            |                      |     |     |              |     | theuser’sinputquery(biologicalevolutionvs. |     |     |     | societal |
for full citation F results for every generative evolution), copying this contents results in lower per-
1
| searchengineoneachofourquerydistributions. |     |     |     |     |     | ceivedutility. |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
4.3 CitationPrecisionisInverselyRelatedto
|     |     |     |     |     |     | This tradeoff | is  | especially | apparent | on the All- |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | -------- | ----------- |
PerceivedUtility
|     |     |     |     |     |     | Souls query | distribution, |     | which contains | open- |
| --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | -------------- | ----- |
We find that citation precision is inversely corre- endedessayquestions. AllSoulsqueriesoftencan-
latedwithperceivedutilityinexistinggenerative
notbeansweredviaextractionfromasingleweb-
search engines (r = −0.96). For example, Bing pageontheInternet. Forexample,giventhequery
Chatachievesthehighestprecision,buthasthelow- “Is cooperation or competition the driving force
| estperceivedutility. |     |     | Incontrast,YouChathasthe |     |     |         |               |     |                            |     |
| -------------------- | --- | --- | ------------------------ | --- | --- | ------- | ------------- | --- | -------------------------- | --- |
|                      |     |     |                          |     |     | guiding | the evolution |     | of society?”, conventional |     |
lowest citation precision, but its responses attain searchengineresultsfocusonbiologicalevolution,
thehighestperceivedutilityratings. rather than societal evolution. Bing Chat simply
This inverse relationship between citation pre- copiesirrelevantstatementsdirectlyfromthecited
sources,resultinginhighcitationprecisionbutlow
| cision | and perceived |     | utility | is symptomatic | of a |     |     |     |     |     |
| ------ | ------------- | --- | ------- | -------------- | ---- | --- | --- | --- | --- | --- |
trade-offbetweenfaithfulnessandabstractiveness perceivedutility(Figure4).
| (Ladhak          | et al., | 2022).     | In particular, | we            | find that |                                    |     |     |     |     |
| ---------------- | ------- | ---------- | -------------- | ------------- | --------- | ---------------------------------- | --- | --- | --- | --- |
|                  |         |            |                |               |           | 4.4 GenerativeSearchEnginesClosely |     |     |     |     |
| system-generated |         | statements |                | often closely | para-     |                                    |     |     |     |     |
phrase or directly copy from their associated ci- ParaphraseFromCitedWebpages
tations(see§4.4forfurtheranalysis). Thisresults Tobetterunderstandhowgenerativesearchengines
inhighcitationprecision(sinceextractivelycopied usecitationstosupporttheirresponses,weanalyze
textisalmostalwaysfullysupportedbythesource the similarity between generated statements and
citation),butlowerperceivedutility(sincetheex- theirsupportingcitedwebpages. Forcitationsthat
tractivesnippetsmaynotactuallyanswertheuser’s providefullorpartialsupportfortheirassociated
inputquery). Incontrast, systemsthatfrequently statement, annotators were asked to provide evi-
deviatefromcitedcontent(resultinginlowcitation dencebycopy-pastingtheminimalsetofsentences
precision) may have greater freedom to generate from the cited webpage that support their judg-
fluent responses that appear relevant and helpful ment (if any such sentences exist). We compute
totheuser’sinputquery. theBLEU(Papinenietal.,2002)andBERTScore

BLEU BERTScore(F1) (2022)proposetheattributedtoidentifiedsources
(AIS)evaluationframeworktoassesswhetherapar-
|     | BingChat |     | 44.1 |     | 78.8 |     |     |     |     |     |     |     |
| --- | -------- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
NeevaAI 30.0 72.9 ticularstatementissupportedbyprovidedevidence
|     | perplexity.ai |     | 22.3 |     | 69.2 |     |              |                  |     |     |                |     |
| --- | ------------- | --- | ---- | --- | ---- | --- | ------------ | ---------------- | --- | --- | -------------- | --- |
|     |               |     |      |     |      |     | and validate | their guidelines |     | on  | conversational |     |
|     | YouChat       |     | 28.6 |     | 72.0 |     |              |                  |     |     |                |     |
questionanswering,summarization,andtable-to-
|     | Average |     | 31.3 |     | 73.2 |     |                    |          |        |            |           |      |
| --- | ------- | --- | ---- | --- | ---- | --- | ------------------ | -------- | ------ | ---------- | --------- | ---- |
|     |         |     |      |     |      |     | text systems.      | Bohnet   | et al. | (2023)     | introduce | the  |
|     |         |     |      |     |      |     | task of attributed | question |        | answering, | where     | sys- |
Table2:Existinggenerativesearchenginescloselypara-
phrase from cited articles; generated statements have temsaregivenaninputquestionandmustoutput
ananswerstringwithapointertoevidencetextsup-
highsimilaritywiththeircitedwebpages.
portingtheanswer,andproposeareproducibleeval-
uationsetupwithNaturalQuestionsqueries(only
(Zhangetal.,2020)betweeneachgeneratedstate-
|     |     |     |     |     |     |     | paragraph | answer type | containing |     | long and | short |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---------- | --- | -------- | ----- |
mentandtheannotator-providedevidencefromthe
answers)withWikipediaastheevidencecorpus.
| associatedcitation. |     |     | Forstatementswithmultipleas- |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Incontemporaneouswork,PeskoffandStewart
sociatedcitations,wetakethemaximumsimilarity
(2023)havedomainexpertsevaluateChatGPTand
withanyassociatedcitation’sevidence.
YouChatresponsesto100expert-writtenquestions.
Table2presentssimilaritymetricsbetweengen-
Theyfindthatgeneratedresponsesarecoherentand
eratedstatementsandextractedevidencefromsup-
|         |               |     |     |            |     |          | concise, | but frequently | undersourced |     | and | inaccu- |
| ------- | ------------- | --- | --- | ---------- | --- | -------- | -------- | -------------- | ------------ | --- | --- | ------- |
| porting | webpages—when |     |     | statements | are | fully or |          |                |              |     |     |         |
rate;ourresultsalsoshowthatYouChatresponses
| partially | supported |     | by their | citations, | they | often |     |     |     |     |     |     |
| --------- | --------- | --- | -------- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
frequentlylackcitationsforgeneratedstatements
| copy | or closely | paraphrase |     | from | their cited | arti- |     |     |     |     |     |     |
| ---- | ---------- | ---------- | --- | ---- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
(i.e.,lowcitationrecall).
cles. Furthermore,systemswithhighersimilarity
betweentheirgeneratedstatementsandcitedweb-
|     |     |     |     |     |     |     | 6 Conclusion |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
pagesalsohavehigheraveragecitationprecision
(r =0.80betweeneachofBLEUandBERTScore Inthiswork,weusedhumanevaluationtoauditthe
| with | average | citation | precision), |     | indicating | that |     |     |     |     |     |     |
| ---- | ------- | -------- | ----------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
verifiabilityoffourpopularcommercialgenerative
theirimprovedprecisionmaylargelybeabyprod-
searchengines—BingChat,NeevaAI,perplexity.ai,
uct of their increased tendency to copy or para- andYouChat. Wefindthatresponsesfromexisting
phrasefromcitedwebpages.
generativesearchenginesaregenerallyfluentand
|     |     |     |     |     |     |     | often appear | informative, |     | but frequently |     | contain |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | -------------- | --- | ------- |
5 RelatedWork
|     |     |     |     |     |     |     | unsupported | statements | and | inaccurate | citations |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ---------- | --------- | --- |
Existingworkhasproposedavarietyoftechniques (lowcitationrecallandprecision)—amere51.5%
for building language models that provide refer- ofgeneratedstatementsarefullysupportedbycita-
ences to support generated text. Nakano et al. tions(recall),andonly74.5%ofcitationssupport
(2021) use reinforcement learning from human theirassociatedstatements(precision). Webelieve
preferences to train language models to answer thatexistingsystems’citationrecallandprecision
questionsandprovidesupportingevidence. Simi- areunacceptablylow, giventhattheyarequickly
larly,Menicketal.(2022)alsousereinforcement becomingapopulartoolforansweringuserqueries
learningfromhumanpreferencestotrainlanguage andalreadyhavemillionsofusers. Moreover,we
modelstoansweruserquestions,buttheirsystem findthat citationprecision isinversely correlated
generates responses by conditioning on evidence withperceivedutilityinexistinggenerativesearch
retrievedfromaGooglesearchforthegivenuser engines—theresponsesthatseemmorehelpfulare
query. Finally, the LaMDA system of Thoppilan often those with more unsupported statements or
et al. (2022) is trained to provide URLs that sup- inaccurate citations. Analysis suggests that this
port its generated statements. In contrast to the inverse correlation occurs in existing systems be-
aforementioned line of work on training systems cause of their propensity to copy or closely para-
to generate citations, Gao et al. (2022) propose a phrasefromcitedwebpages,whichinflatescitation
methodforpost-editinggeneratedoutputtoreflect precisionatthecostoflowerperceivedutility. We
andciteretrievedevidence. hopeourresultsandinsightsfurthermotivatethe
Existingworkhasalsoproposedevaluationpro- developmentoftrustworthygenerativesearchen-
tocols and benchmarks for improving verifiabil- ginesandhelpresearchersandusersbetterunder-
ityinlanguagegenerationsystems. Rashkinetal. standtheircurrentshortcomings.

Acknowledgements
|     |     |     |     |     |     | Bernd Bohnet, |     | Vinh | Q. Tran, | Pat | Verga, | Roee Aha- |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | -------- | --- | ------ | --------- |
roni,DanielAndor,LivioBaldiniSoares,Massimil-
We are grateful to the 34 annotators who partici- ianoCiaramita,JacobEisenstein,KuzmanGanchev,
JonathanHerzig,KaiHui,TomKwiatkowski,JiMa,
| pated in | our human | evaluation | study—this |     | work |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
would not have been possible without them. We Jianmo Ni, Lierni Sestorain Saralegui, Tal Schus-
|            |       |            |     |      |         | ter, William |     | W. Cohen, | Michael |     | Collins, | Dipanjan |
| ---------- | ----- | ---------- | --- | ---- | ------- | ------------ | --- | --------- | ------- | --- | -------- | -------- |
| also thank | Rishi | Bommasani, | Ge  | Gao, | Natasha |              |     |           |         |     |          |          |
Das,DonaldMetzler,SlavPetrov,andKellieWebster.
Klein-Atlas,VivianLai,KevinLin,JohnThickstun, 2023. Attributed question answering: Evaluation
EricWallace,andGerbenWierdaforfeedbackand andmodelingforattributedlargelanguagemodels.
| discussions  | that | helped   | improve | this work. | We   | ArXiv:2212.08037. |     |     |        |        |       |        |
| ------------ | ---- | -------- | ------- | ---------- | ---- | ----------------- | --- | --- | ------ | ------ | ----- | ------ |
| thank Amazon | Web  | Services | for     | providing  | Ama- |                   |     |     |        |        |       |        |
|              |      |          |         |            |      | Joy Buolamwini    |     | and | Timnit | Gebru. | 2018. | Gender |
zon Mechanical Turk credits that helped support shades: Intersectional accuracy disparities in com-
thiswork. Thisworkwassupportedinpartbythe mercialgenderclassification. InProc.ofFAccT.
AI2050programatSchmidtFutures(GrantG-22-
|         |     |     |     |     |     | Sihao Chen,                     | Daniel | Khashabi, |                            | Wenpeng |              | Yin, Chris |
| ------- | --- | --- | --- | --- | --- | ------------------------------- | ------ | --------- | -------------------------- | ------- | ------------ | ---------- |
| 63429). |     |     |     |     |     | Callison-Burch,andDanRoth.2019. |        |           |                            |         | Seeingthings |            |
|         |     |     |     |     |     | fromadifferentangle:            |        |           | Discoveringdiverseperspec- |         |              |            |
Limitations
|     |     |     |     |     |     | tivesaboutclaims. |     |     | InProc.ofNAACL. |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --------------- | --- | --- | --- |
Theprimarygoalofthisworkwastoassessverifia- AngelaFan,YacineJernite,EthanPerez,DavidGrang-
bilityingenerativesearchengineresponses. How- ier, Jason Weston, and Michael Auli. 2019. ELI5:
|     |     |     |     |     |     | Longformquestionanswering. |     |     |     | InProc.ofACL. |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ------------- | --- | --- |
ever,notethatverifiabilityisnotfactuality—rather
thanarbitratingifageneratedstatementistrue(dif- Luyu Gao, Zhuyun Dai, Panupong Pasupat, Anthony
ficultforallbutthesimplestclaims;Rashkinetal., Chen, Arun Tejasvi Chaganty, Yicheng Fan, Vin-
2022), verifiability enables users to easily check centY.Zhao,NiLao,HongraeLee,Da-ChengJuan,
|     |     |     |     |     |     | and Kelvin | Guu. | 2022. |     | RARR: | Researching | and |
| --- | --- | --- | --- | --- | --- | ---------- | ---- | ----- | --- | ----- | ----------- | --- |
anygeneratedstatement’ssource,allowingthemto
revisingwhatlanguagemodelssay,usinglanguage
drawtheirownconclusionsaboutwhethertotrust models. ArXiv:2210.08726.
| thegeneratedstatement. |     |     | Studyingthefactualityof |     |     |                |     |     |           |      |           |      |
| ---------------------- | --- | --- | ----------------------- | --- | --- | -------------- | --- | --- | --------- | ---- | --------- | ---- |
|                        |     |     |                         |     |     | Amelia Glaese, |     | Nat | McAleese, | Maja | Tre˛bacz, | John |
generativesearchengines(thatmayormaynotpro-
Aslanides,VladFiroiu,TimoEwalds,MaribethRauh,
videcitations)isanimportantdirectionforfuture
LauraWeidinger,MartinChadwick,PhoebeThacker,
work—usersmaynotnecessarilybothertocheck
|     |     |     |     |     |     | Lucy Campbell-Gillingham, |     |     |     | Jonathan | Uesato, | Po- |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | -------- | ------- | --- |
thesources,especiallygiventhatresponsesoften SenHuang,RamonaComanescu,FanYang,Abigail
See,SumanthDathathri,RoryGreig,CharlieChen,
| seemhelpfulandsoundconfident, |     |     |     | andwe’dthus |     |      |        |       |         |        |         |        |
| ----------------------------- | --- | --- | --- | ----------- | --- | ---- | ------ | ----- | ------- | ------ | ------- | ------ |
|                               |     |     |     |             |     | Doug | Fritz, | Jaume | Sanchez | Elias, | Richard | Green, |
likeresponsestobeasfactualaspossible.
SonˇaMokrá,NicholasFernando,BoxiWu,Rachel
| In our | evaluation | of  | verifiability, | we  | consider |     |     |     |     |     |     |     |
| ------ | ---------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Foley,SusannahYoung,IasonGabriel,WilliamIsaac,
sentence-level claims. However, sentences often JohnMellor,DemisHassabis,KorayKavukcuoglu,
|               |        |        |          |     |         | Lisa Anne | Hendricks, |     | and | Geoffrey | Irving. | 2022. |
| ------------- | ------ | ------ | -------- | --- | ------- | --------- | ---------- | --- | --- | -------- | ------- | ----- |
| have multiple | claims | (e.g., | “Cats[1] | and | dogs[2] |           |            |     |     |          |         |       |
are common pets.”). However, there is currently Improvingalignmentofdialogueagentsviatargeted
|     |     |     |     |     |     | humanjudgements. |     |     | ArXiv:2209.14375. |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ----------------- | --- | --- | --- |
noclearlinguisticdefinitiononwhatconstitutesa
claim. Asaresult,weusesentencesforsimplicity BenGreenandYilingChen.2019. Disparateinterac-
tions: Analgorithm-in-the-loopanalysisoffairness
| andreproducibility. |     | Proposingaconcretedefinition |     |     |     |                    |     |     |                 |     |     |     |
| ------------------- | --- | ---------------------------- | --- | --- | --- | ------------------ | --- | --- | --------------- | --- | --- | --- |
|                     |     |                              |     |     |     | inriskassessments. |     |     | InProc.ofFAccT. |     |     |     |
ofa“claim”andperformingafiner-grainedevalua-
tionisaninterestingdirectionforfuturework. SvetlanaKiritchenkoandSaifMohammad.2018. Ex-
amininggenderandracebiasintwohundredsenti-
|     |     |     |     |     |     | mentanalysissystems. |     |     | InProc.of*SEM. |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------------- | --- | --- | --- |
References
|     |     |     |     |     |     | TomKwiatkowski, |     | JennimariaPalomaki, |     |     | OliviaRed- |     |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------------------- | --- | --- | ---------- | --- |
Michiel Bakker, Martin Chadwick, Hannah Sheahan, field,MichaelCollins,AnkurParikh,ChrisAlberti,
Michael Tessler, Lucy Campbell-Gillingham, Jan DanielleEpstein,IlliaPolosukhin,JacobDevlin,Ken-
Balaguer, Nat McAleese, Amelia Glaese, John tonLee,KristinaToutanova,LlionJones,Matthew
Aslanides, Matt Botvinick, and Christopher Sum- Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob
merfield.2022. Fine-tuninglanguagemodelstofind Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natu-
agreementamonghumanswithdiversepreferences. ralquestions: Abenchmarkforquestionanswering
InProc.ofNeurIPS. research. TransactionsoftheAssociationforCompu-
tationalLinguistics,7:452–466.
AbebaBirhane,VinayUdayPrabhu,andJohnWhaley.
2022. Auditing saliency cropping algorithms. In FaisalLadhak,EsinDurmus,HeHe,ClaireCardie,and
| Proc.ofWACV. |     |     |     |     |     | KathleenMcKeown.2022. |     |     |     | Faithfulorextractive? |     | on  |
| ------------ | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --------------------- | --- | --- |

mitigatingthefaithfulness-abstractivenesstrade-off AminGhafouri,MarceloMenegali,YanpingHuang,
inabstractivesummarization. InProc.ofACL. MaximKrikun,DmitryLepikhin,JamesQin,Dehao
Chen,YuanzhongXu,ZhifengChen,AdamRoberts,
Joshua Maynez, Shashi Narayan, Bernd Bohnet, and MaartenBosma,VincentZhao,YanqiZhou,Chung-
| RyanMcDonald.2020.             |     |     | Onfaithfulnessandfactual- |               |     |     |              |                |     |      |        |      |
| ------------------------------ | --- | --- | ------------------------- | ------------- | --- | --- | ------------ | -------------- | --- | ---- | ------ | ---- |
|                                |     |     |                           |               |     |     | Ching Chang, | Igor Krivokon, |     | Will | Rusch, | Marc |
| ityinabstractivesummarization. |     |     |                           | InProc.ofACL. |     |     |              |                |     |      |        |      |
Pickett,PraneshSrinivasan,LaicheeMan,Kathleen
|                  |     |                            |     |     |     |     | Meier-Hellstern, | Meredith |     | Ringel Morris, |     | Tulsee |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- | ---------------- | -------- | --- | -------------- | --- | ------ |
| YusufMehdi.2023. |     | ThenewBingandEdge–progress |     |     |     |     |                  |          |     |                |     |        |
Doshi,RenelitoDelosSantos,TojuDuke,JohnnySo-
fromourfirstmonth|Bingsearchblog. Accessedon raker,BenZevenbergen,VinodkumarPrabhakaran,
March28,2023.
|     |     |     |     |     |     |     | Mark Diaz, | Ben Hutchinson, |     | Kristen | Olson, | Ale- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------- | ------ | ---- |
jandraMolina,ErinHoffman-John,JoshLee,Lora
| Jacob Menick,   |     | Maja    | Trebacz, | Vladimir |           | Mikulik, |             |            |       |          |         |     |
| --------------- | --- | ------- | -------- | -------- | --------- | -------- | ----------- | ---------- | ----- | -------- | ------- | --- |
|                 |     |         |          |          |           |          | Aroyo, Ravi | Rajakumar, | Alena | Butryna, | Matthew |     |
| John Aslanides, |     | Francis | Song,    | Martin   | Chadwick, |          |             |            |       |          |         |     |
Lamm,ViktoriyaKuzmina,JoeFenton,AaronCo-
| Mia Glaese, |     | Susannah | Young, |     | Lucy Campbell- |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
hen,RachelBernstein,RayKurzweil,BlaiseAguera-
| Gillingham, | Geoffrey |     | Irving, | and | Nat McAleese. |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Arcas,ClaireCui,MarianCroak,EdChi,andQuoc
2022. Teachinglanguagemodelstosupportanswers
|                     |     |                   |     |     |     |     | Le.2022.    | LaMDA:Languagemodelsfordialogap- |     |     |     |     |
| ------------------- | --- | ----------------- | --- | --- | --- | --- | ----------- | -------------------------------- | --- | --- | --- | --- |
| withverifiedquotes. |     | ArXiv:2203.11147. |     |     |     |     |             |                                  |     |     |     |     |
|                     |     |                   |     |     |     |     | plications. | ArXiv:2201.08239.                |     |     |     |     |
DanaëMetaxa,JoonSungPark,JamesA.Landay,and
|                   |     |                          |     |     |     |     | Tianyi Zhang, | Varsha Kishore, |        | Felix Wu, | Kilian     | Q.  |
| ----------------- | --- | ------------------------ | --- | --- | --- | --- | ------------- | --------------- | ------ | --------- | ---------- | --- |
| JeffHancock.2019. |     | Searchmediaandelections: |     |     |     | A   |               |                 |        |           |            |     |
|                   |     |                          |     |     |     |     | Weinberger,   | and Yoav        | Artzi. | 2020.     | BERTScore: |     |
longitudinalinvestigationofpoliticalsearchresults.
|     |     |     |     |     |     |     | EvaluatingtextgenerationwithBERT. |     |     |     | InProc.of |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --------- | --- |
InProc.ofCSCW.
ICLR.
| Panagiotis | Takis | Metaxas | and | Yada | Pruksachatkun. |     |     |     |     |     |     |     |
| ---------- | ----- | ------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
2017. Manipulationofsearchengineresultsduring
the2016uscongressionalelections.
| Reiichiro        | Nakano,  | Jacob        | Hilton,     | Suchir         | Balaji,        | Jeff    |     |     |     |     |     |     |
| ---------------- | -------- | ------------ | ----------- | -------------- | -------------- | ------- | --- | --- | --- | --- | --- | --- |
| Wu, Long         | Ouyang,  |              | Christina   | Kim,           | Christopher    |         |     |     |     |     |     |     |
| Hesse,           | Shantanu | Jain,        | Vineet      | Kosaraju,      |                | William |     |     |     |     |     |     |
| Saunders,        | Xu       | Jiang,       | Karl Cobbe, |                | Tyna Eloundou, |         |     |     |     |     |     |     |
| GretchenKrueger, |          | KevinButton, |             | MatthewKnight, |                |         |     |     |     |     |     |     |
| Benjamin         | Chess,   | and          | John        | Schulman.      | 2021.          | We-     |     |     |     |     |     |     |
bGPT:Browser-assistedquestion-answeringwithhu-
| manfeedback. |     | ArXiv:2112.09332. |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
KishorePapineni,SalimRoukos,ToddWard,andWei-
| JingZhu.2002.               |         | BLEU:amethodforautomaticeval- |          |               |            |          |     |     |     |     |     |     |
| --------------------------- | ------- | ----------------------------- | -------- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
| uationofmachinetranslation. |         |                               |          | InProc.ofACL. |            |          |     |     |     |     |     |     |
| Denis Peskoff               | and     | Brandon                       | Stewart. |               | 2023.      | Credible |     |     |     |     |     |     |
| without                     | credit: | Domain                        | experts  | assess        | generative |          |     |     |     |     |     |     |
| languagemodels.             |         | InProc.ofACL.                 |          |               |            |          |     |     |     |     |     |     |
FabioPetroni,AleksandraPiktus,AngelaFan,Patrick
Lewis,MajidYazdani,NicolaDeCao,JamesThorne,
YacineJernite,VladimirKarpukhin,JeanMaillard,
VassilisPlachouras,TimRocktäschel,andSebastian
| Riedel.                 | 2021.   | KILT:  | a benchmark     |          | for knowledge |       |     |     |     |     |     |     |
| ----------------------- | ------- | ------ | --------------- | -------- | ------------- | ----- | --- | --- | --- | --- | --- | --- |
| intensivelanguagetasks. |         |        | InProc.ofNAACL. |          |               |       |     |     |     |     |     |     |
| Hannah Rashkin,         |         | Vitaly | Nikolaev,       | Matthew  |               | Lamm, |     |     |     |     |     |     |
| Lora Aroyo,             | Michael |        | Collins,        | Dipanjan | Das,          | Slav  |     |     |     |     |     |     |
Petrov,GauravSinghTomar,IuliaTurc,andDavid
| Reitter.2022.          |     | Measuringattributioninnaturallan- |                   |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --------------------------------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| guagegenerationmodels. |     |                                   | ArXiv:2112.12870. |     |     |     |     |     |     |     |     |     |
RonaldE.Robertson,DavidLazer,andChristoWilson.
2018. Auditingthepersonalizationandcomposition
| ofpolitically-relatedsearchengineresultspages. |     |     |     |     |     | In  |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proc.ofWWW.
| Romal Thoppilan, |     | Daniel | De            | Freitas, | Jamie    | Hall, |     |     |     |     |     |     |
| ---------------- | --- | ------ | ------------- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| Noam Shazeer,    |     | Apoorv | Kulshreshtha, |          | Heng-Tze |       |     |     |     |     |     |     |
Cheng,AliciaJin,TaylorBos,LeslieBaker,YuDu,
| YaGuang | Li, Hongrae |     | Lee, | Huaixiu | Steven | Zheng, |     |     |     |     |     |     |
| ------- | ----------- | --- | ---- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- |

A Examplequeriesfromeachevaluatedquerydistribution
Source ExampleQueries
Whatarethefunctionsoffashion?
AllSouls
Shouldwealthbeinheritable?
Shouldprivatecompaniesbeallowedtomanagepublicutilities?
davinci-debate
Shouldcontroversialopinionsbecensoredonsocialmedia?
Whyisacircle360degreesandnot100degrees?
ELI5(KILT)
Whycananimalsdrinkdirtywatersafelybuthumanscan’t?
Whyjumpingintowaterfromgreatheightfeelslikelandinginconcrete?
ELI5(Live)
wheredoesthedeleteddatago
agepaperusingtea
WikiHowKeywords
waystostopstressingoverexamresults
NaturalQuestions whowrotethesonggodyourmamaandme
(paragraphlonganswer,hasshortanswer) whatisthequeenofspain’sname
NaturalQuestions wheredidknockonwoodsuperstitioncomefrom
(paragraphlonganswer,noshortanswer) whatistheuseoftapanddie
NaturalQuestions whatisthemostnominatedfilmfortheoscars
(listlonganswer,hasshortanswer) whoplayedguitaroniwantyoushe’ssoheavy
NaturalQuestions aliciakeysifiain’tgotyouawards
(listlonganswer,noshortanswer) isalloffloridainthesametimezone
NaturalQuestions howmanyepisodesarethereinquantumleap
(tablelonganswer,hasshortanswer) whatkindofmusicisredhotchilipeppers
NaturalQuestions wheredoescopaairlinesflyintheunitedstates
(tablelonganswer,noshortanswer) michaeljordancareerhighagainsteverynbateam
NaturalQuestions whatdoesthexcardmeaninuno
(nolongorshortanswer) whatchangesweremadewhentrinidadandtobagogainedindependence
Table 3: Example queries from each of the evaluated query distributions. Queries come from diverse sources
andrequireknowledgefromavarietyofanswertypes(e.g.,shorttextspan,long-formparagraph,list,ortable).
Eachsystemisevaluatedon1450queries—150randomly-sampledqueriesfromeachofAllSouls,davinci-debate,
ELI5 (KILT), ELI5 (Live), and WikiHowKeywords, and 100 randomly-sampled queries for each of the seven
NaturalQuestionssubdistributions.
B QueryDistributionDetails
B.1 davinci-debate
Weseedthedatagenerationprocesswith100debatequestions,whicharemanuallytransformedpropo-
sitions propositions taken from the Perspectrum dataset of Chen et al. (2019) (e.g., the proposition
“Vaccinationmustbemadecompulsory.” couldberewrittenasthequestion“Shouldvaccinesbemanda-
tory?”).
Togenerateadebatequestion,weprompttext-davinci-003with10randomly-sampledseedques-
tions. We repeat this procedure until we have generated 150 unique debate questions that also do not
appearinourseedset. Finally,generatedquestionsweremanuallyfilteredforinappropriatecontent.
B.2 ELI5
TotransformELI5posttitlesintoqueries,weremoveELI5-specificprefixes(e.g.,theposttitle“ELI5:
why can’t our brains recall every memory?” becomes the query “Why can’t our brains recall every
memory?”).
B.3 WikiHowKeywords
Toparaphrasearticletitlesintokeywordqueries,weprompttext-davinci-003with“Givenaquestion,
writeaconciseGooglesearchquerythatwouldanswerthequestion”andtwoin-contextexamples.

C AnnotationInterface
Figures5-7showtheannotationinterfaceusedforhumanevaluation.
Inthefirststep,annotatorswereshownthequeryandthegeneratedresponse(withoutcitations)and
askedtorateresponsefluencyandperceivedutilityonafive-pointLikertscale.
In the second step, annotators were shown the statements in the generated response (including any
generatedcitations)andaskedtofilteroutstatementsarenotverification-worthy.
Finally,inthethirdstep,annotatorswereshownthestatementsthatwerepreviouslyjudgedtorequire
verification (in the prior step), as well as each statement’s associated system-generated citations. For
eachstatementandassociatedcitation,annotatorsjudgedwhetherthecitationfullysupports,partially
supports,ordoesnotsupportthestatement,asinterpretedwithinthebroadercontextofthequeryand
systemresponse. Forstatementswithmultipleassociatedcitations,annotatorsareaskedtojudgewhether
thecitations,whentakentogether,fullysupportthestatement;thiscapturescaseswheremultiplecitations
supportdisjointpartsofastatement(e.g.,“Healthbenefitsofcyclingincludeimprovedcardiovascular
health[1]andloweredcholesterollevels[2].”).
Figure5: Firststepoftheannotationinterface,whereannotatorsjudgeresponsefluencyandperceivedutility.

Figure6: Secondstepoftheannotationinterface,whereannotatorsuncheckstatementsthatarenotverification-
worthy. Statementsthatcontaingeneratedcitationsmustbeverification-worthy,soweautomaticallymarkthemas
suchintheinterface(greyed-outcheckboxesnexttothe2ndand4thsentencesabove).
Figure7: Thirdstepoftheannotationinterface, whereannotatorsprovidejudgmentsonwhethereachcitation
supports its associated statement, and whether each statement is supported by the union of its citations (only
applicablewhenastatementhasmultipleassociatedcitations).

D AnnotationGuidelines
Figures8-12showtheannotationguidelinesweusedforthetask. Weaskcrowdannotatorstoreadthese
Overview
guidelinesaspartofthequalificationstudy. Onlyannotatorsthatdemonstratedathoroughunderstanding
oftheguidelHini!eWseaanrdetaatsekamwoefrSetapnefromrdirtetesdeatrochpearsrtinicteirpeastteedinintehvealmuaatiningrthoeutnrudstowforhthuimneasnsoefvAaIluation.
systems.
Inthistask,youwillevaluateanAIsystem'sresponsetoauserquery.TheAIsystemoutputsa
paragraphthatcontainsinformationrelevanttotheuser'squery,andwewouldliketoevaluate
whethertheAIsystemcanaccuratelycitesourcesforstatementsitmakesabouttheexternal
world.
Atahighlevel,thistaskbreaksdownintothreesteps:
1.Evaluatingresponsequality
2.Filteringsentencesthatdonotrequirecitation.
3.Judgingwhethereachstatementisfullysupportedbyitscitation(s).
Pleasecarefullyreadtheguidelinesbelowbeforestartingonthetask.Thetask
compensationaccountsforthetimeneededtoreadtheguidelines.
Preliminaries: Logging In
Whenfirstenteringthesite,youwillbepromptedtoselectausername.Pleaseuseyour
workerIDastheusername,sowecankeeptrackoftheexamplesyou'veannotated.The
topoftheinterfacedisplaysyourworkerID,thetotalnumberofexamplessubmittedfromthis
username,andwillshowacompletioncodewhenyouhavefinishedthetask.
Ifsomethingiswrongwiththeexample,youmaypressthe"FlagExample"buttoninthe
top-rightcornertoreporttheerror.Pleasedonotsubmitannotationsforsuchexamples.
Yourtaskendsafteryou'vecompleted5responses.Acompletioncodewillappearatthe
topoftheinterface---thereisnoneedtocompletemorethan5responsestoreceive
creditforthestudy.
Step 1: Evaluating response quality
Youwillbeshowntheuser'soriginalquery,andthesystem'sresponsetothequery---please
carefullyreadbothofthem.Then,youwillbeaskedtorateyourlevelofagreementwithtwo
questions:
1.Theresponseisfluentandcohesive.
2.Theresponseisahelpfulandinformativeanswertothequery.
Figure8: Firstpageoftheannotationguidelines.

Onceyouhavefinishedselectingaresponseforeachofthetwoquestions,pressthe"Next
Step"buttoninthetop-rightcornertocontinue.
Step 2: Filtering sentences that do not require
citation.
Thegoalofthisstepistofilterthesentencesinthesystemresponsebyremovingsentences
thatdonotrequirecitation(uncheckingthemintheinterface).Weexpectthemajorityof
sentencesproducedbythesystemtorequirecitation,sodon'tworryifyoufindyourself
rarelyuncheckingsentences.
Ingeneral,wetakethepositionthatallstatementsabouttheexternalworldrequirecitation,
eveniftheyaretriviallytrueor"commonsense"(sinceusersmaydifferintheirbackground,
whichaffectstheirbasicbeliefs).Forexample,thefollowingsentencesrequirecitation:
- (1a):TheHouseofLordsisatopicofongoingdebateintheUK.
- (1b):However,thereisstillnoconsensusonwhatshouldreplacetheElectoralCollege.
- (1c):Theskyisblue.
- (1d):Themoonlandingwasstaged.
- (1e):InFebruary2023,LeBronJamestook261,960totalbreaths.
- (1f):PatrickHenryoncesaid"Givemeliberty,orgivemedeath".
- (1g):Thanksgivingdinnersusuallytastebad.
- (1h):Votingrightsarecontroversial
Inparticular,notethatsentencescanrequirecitationdespitebeingnearlyimpossibletoverify.
Considerexample(e)above.It'shighlyunlikelythatanyoneknowsexactlyhowmanybreaths
LeBronJamestookinFebruary2023,letalonethatsuchinformationcouldbelinkedtoina
citation.However,it'sstillastatementabouttheexternalworld,andit'sstillpossibletofindout
forcertainwhetherthestatementistrueorfalse.Thus,thestatementrequirescitation.
Incontrast,considerthefollowingexamplesofsentencesthatdonotrequirecitation:
- (2a):Ibelievethatthemoonlandingwasstaged.
- Explanation:Ingeneral,allsentencespertainingto"I"donotrequirecitation.
Thisstatementexpressesabeliefheldbythespeaker.Thespeakerisunknown,
sothisstatementdoesnotrequirecitation.Notethatthesimilar-looking
statement"Themoonlandingwasstaged"(example1d)requirecitationandis
verifiable.
- (2b):Haveyoulistenedtothatsong?
- Explanation:Questionsdonothaveinformationtoverify.
- (2c):Pickuptheballonthefloor.
- Explanation:Commandsdonothaveinformationtoverify.
- (2d):Itistheyear2300.Robotsruletheearth.
Figure9: Secondpageoftheannotationguidelines.

- Explanation:thesentence"Robotsruletheearth."doesnotrequirecitation,
sincethecontext("Itistheyear2300")specifiesthatthisisahypothetical
situationandnotastatementabouttheexternalworld.
Carefullyreadeachsentenceagainanddecidewhetheritrequirescitation.Ifitdoesnotrequire
citation,uncheckitscorrespondingcheckbox.Whenyouhavefinished,pressthe"NextStep"
buttoninthetop-rightcornertoproceed.
Step 3: Judging whether each statement is fully
supported by its citation(s).
Inthisstep,youwillevaluatewhethereachstatementissupportedbyitscorresponding
citations.Notethatthesystemresponsesmayappearveryfluentandwell-formed,butcontain
slightinaccuraciesthatarenoteasytodiscernatfirstglance.Paycloseattentiontothetext.
Readitcarefullyasyouwouldwhenproofreading.
Carefullyreadtheuserqueryandthestatement.Youmayalsohavetore-readthefullsystem
responsetounderstandthestatementinitsfullcontext.Giventhestatement'sassociated
citations,yourtaskistojudgewhetheralloftheinformationprovidedbythesystemresponseis
fullysupportedbythesourcedocument.
Inparticular,thisquestioncanbeansweredbyconsidering:
- (A):Whatistheinformationprovidedbythestatement?
- (B):Accordingtothecitation(s),isthisstatementtrue?
(A):Whatistheinformationprovidedbythestatement?
Todeterminetheinformationprovidedbythestatement,youmustconsiderthequery,the
statement,andthecontextofthestatementwithinthefullresponse.Thecitationsshouldbe
completelyignoredwhendetermining"theinformationprovidedbythestatement."
Considerthefollowingexample:
Query:Whydosomanypeoplewanttogetmarried?
Response(statementhighlighted):Peoplegetmarriedformanyreasons,includinglove,
companionship,financialsecurity,andtosharetheirliveswithapartner.Marriagecanalsobe
seenasawaytoaffirmmutualloveorstartafamily.
Inthiscase,thestatementisstand-alone,andcanbeinterpretedwithoutlookingatthequeryor
therestoftheresponse.However,thisisnotalwaysthecase.Considertheexamplebelow:
Query:Isitwrongtoexaggerateinaletterofrecommendation?
Figure10: Thirdpageoftheannotationguidelines.

Response(statementhighlighted):Yes,itiswrong.Lettersofrecommendationshouldreflect
theauthor'shonestperspectiveonthecandidate.
Theresponse"Yes,itiswrong"isuninterpretableonitsown,becauseitisnotclearwhat"it"
refersto.However,byusingthecontextofthequery,itbecomesclearthatthestatementis
equivalentto"Yes,[exaggeratinginaletterofrecommendation]iswrong".
Foranotherexample,consider:
Query:howmanycharactersareintheprologueofcanterburytales
Response(statementhighlighted):InGeoffreyChaucer'sTheCanterburyTales,32
charactersmakethejourneytoCanterbury.Thisincludesthenarrator,thehost,andthe
Canon'syeoman,whojointhegrouplater.
Thestatement"Thisincludesthenarrator,thehost,andtheCanon'syeoman,whojointhe
grouplater."isuninterpretableonitsown,becauseitisnotclearwhat"This"refersto,orwhat
"group"theyjoin.Theprecedingsentenceoftheresponseisessentialforrealizingthatthis
sentenceisequivalentto"[The32charactersthatmakethejourneytoCanterbury]includethe
narrator,thehost,andtheCanon'syeoman,whojointhe[32characters]later".
Ingeneral,useyourbestjudgmenttodeterminetheinformationprovidedbythesystem
response.
(B):Accordingtothecitation(s),isthisstatementtrue?
Again,youshoulduseyourbestjudgmentindeterminingwhetheralloftheinformationprovided
bythestatementissupportedbytheassociatedcitation(s).
Itmaybehelpfultoaskyourselfwhetheritisaccuratetosay"accordingtothecitation"witha
statementfollowingthisphrase.Forexample,isitaccuratetosay“accordingtothecitation,in
GeoffreyChaucer'sTheCanterburyTales,32charactersmakethejourneytoCanterbury"?
Besuretocheckalloftheinformationinthestatement.Youwillbegivensixoptions:
- "FullSupport":Alloftheinformationinthestatementissupportedinthedocument.
- "PartialSupport":Onlysomeoftheinformationissupportedinthedocument,butother
partsoftheinformationaremissingfromthedocument.
- "NoSupport":Thisdocumentdoesnotsupportanypartofthestatement.
- "ArticleNotAccessible":Notabletoaccessthedocument(e.g.,paywallorthelinkis
dead)
- "CitationHasSupportbutalsoRefutesStatement":Thecitationhasinformationthat
supportsthestatement,butalsohasinformationthatrefutesthestatement.
- "StatementisUnclear,Can'tMakeJudgment":Thestatementissoincomprehensible
thatitcannotbedeterminedifthecitationsupportsthestatement.
Figure11: Fourthpageoftheannotationguidelines.

Ifthecitationoffers"fullsupport"or"partialsupport"ofadocument,youwillalsobeasked
tocopyandpastetheminimalsetofsentencesfromthearticlethatsupportyourjudgment.In
caseswhereyoucan'tlocalizethejudgmenttoparticularsentence(s)(e.g.,theentirearticle
supportsthestatement,orthesupportcomesfromanimageorgraphic),feelfreetoleavethis
inputblank.
Whenastatementhasmorethanoneassociatedcitation,youwillalsojudgewhetherthe
citations,whentakentogether,fullysupportthestatement(Yes/No).Inotherwords,ifyou
mergedallofthesecitationsintoonebigwebpage(anditbecameasinglecitation),wouldthis
citationfullysupportthestatement?Ifthecitationscontradicteachother(e.g.,onefullysupports
thestatement,whereasanotherrefutesthestatement),thenselect"CitationsContradictEach
Other".
Questions oFirgufreee12d:bFiafthcpka?geoftheannotationguidelines.
Ifyouhavequestionsaboutthetask,oranyfeedbackabouthowwecouldmakeitbetteror
whatyourexperiencewaslikewithit,pleaseemailnfliu@cs.stanford.edu,andwe'llgetbackto
youpromptly.Thanks!

E AnnotationQuality
Table4presentsinter-annotatoragreementstatistics,computedonarandomsampleof250query-response
pairs that received annotations each. We measure the pairwise agreement between individual pairs of
ratingsandanF1scorecomparingindividualratingstothemajorityconsensus. Wecomputeagreementon
judgmentsof(i)fluencyandperceivedutility,(ii)whetherastatementisverification-worthy,(iii)whether
acitationsupportsitsassociatedstatement,and(iv)whetherastatementisfullysupportedbytheunion
ofitscitations(inthecasewheremultiplewebpagesarecited). Whencalculatingagreementonfluency
andperceivedutilityjudgments,wecoarsenthe5-pointLikertjudgmentsintothreeoptions: “Disagree”,
“Neutral”,and“Agree”. Agreementratesbetweenannotatorsarehigh(pairwiseagreementgreaterthan
82.0%andF1greaterthan91.0foralljudgments).
Inter-AnnotatorAgreement(↑)
PairwiseAgreement% F1
Fluency 88.5 94.1
PerceivedUtility 86.4 93.1
Verifiability 94.6 97.3
CitationSupports 82.0 91.0
StatementSupported 82.2 91.1
Table 4: Inter-annotator agreement statistics. Pairwise Agreement % computes the proportion of individual
judgment pairs that agree, and F1 compares individual judgments to the majority consensus judgment. Inter-
annotatoragreementishigh(greaterthan82.0%pairwiseagreement%and91.0F1foralljudgments).

F FluencyandPerceivedUtility
Table5presentsthefluencyofgenerativesearchengineresponsesoneachofourquerydistributions,and
Table6presentstheperceivedutility.
Fluency(↑)
Fluency(↑)
|               | AverageOver |                    |     |                         |           | ELI5 |                 |      |
| ------------- | ----------- | ------------------ | --- | ----------------------- | --------- | ---- | --------------- | ---- |
|               | AllQueries  |                    |     | AllSouls davinci-debate |           |      | WikiHowKeywords |      |
|               |             |                    |     |                         | KILT      | Live |                 |      |
| BingChat      |             | 4.40 BingChat      |     | 4.31                    | 4.37 4.36 | 4.30 |                 | 4.41 |
| NeevaAI       |             | 4.43 NeevaAI       |     | 4.50                    | 4.53 4.50 | 4.42 |                 | 4.42 |
| perplexity.ai |             | 4.51 perplexity.ai |     | 4.43                    | 4.54 4.55 | 4.47 |                 | 4.45 |
| YouChat       |             | 4.59 YouChat       |     | 4.58                    | 4.65 4.56 | 4.53 |                 | 4.52 |
| Average       |             | 4.48 Average       |     | 4.45                    | 4.52 4.49 | 4.43 |                 | 4.45 |
Fluency(↑)
NaturalQuestions
|     |     | ListLongAnswer | TableLongAnswer |     | ParagraphLongAnswer |     |     |     |
| --- | --- | -------------- | --------------- | --- | ------------------- | --- | --- | --- |
NoAnswer
|               |     | HasShort NoShort | HasShort | NoShort   | HasShort | NoShort |      |      |
| ------------- | --- | ---------------- | -------- | --------- | -------- | ------- | ---- | ---- |
| BingChat      |     | 4.49 4.52        |          | 4.46 4.30 | 4.54     |         | 4.41 | 4.39 |
| NeevaAI       |     | 4.45 4.40        |          | 4.31 4.28 | 4.41     |         | 4.49 | 4.43 |
| perplexity.ai |     | 4.69 4.54        |          | 4.59 4.41 | 4.73     |         | 4.43 | 4.37 |
| YouChat       |     | 4.65 4.56        |          | 4.60 4.45 | 4.66     |         | 4.69 | 4.64 |
| Average       |     | 4.57 4.50        |          | 4.49 4.36 | 4.58     |         | 4.50 | 4.46 |
Table5: Humanevaluationresultsforgeneratedresponsefluency(five-pointLikertratings). Ingeneral,existing
generativesearchenginesproducefluenttext. PerformanceisnotablyloweronNaturalQuestionsquerieswith
table-typelonganswersandnoshortanswers,whichoftenrequireaggregatinginformationwithinoracrosscitations.

| PerceivedUtility(↑) |     | PerceivedUtility(↑) |     |     |     |     |
| ------------------- | --- | ------------------- | --- | --- | --- | --- |
ELI5
AverageOver
|               |            |               | AllSouls davinci-debate |           | WikiHowKeywords |      |
| ------------- | ---------- | ------------- | ----------------------- | --------- | --------------- | ---- |
|               | AllQueries |               |                         | KILT      | Live            |      |
| BingChat      | 4.34       |               |                         |           |                 |      |
|               |            | BingChat      | 4.15                    | 4.19 4.19 | 4.09            | 4.37 |
| NeevaAI       | 4.48       |               |                         |           |                 |      |
|               |            | NeevaAI       | 4.44                    | 4.39 4.54 | 4.46            | 4.42 |
| perplexity.ai | 4.56       |               |                         |           |                 |      |
|               |            | perplexity.ai | 4.39                    | 4.60 4.54 | 4.50            | 4.51 |
| YouChat       | 4.62       |               |                         |           |                 |      |
|               |            | YouChat       | 4.53                    | 4.54 4.53 | 4.50            | 4.63 |
| Average       | 4.50       |               |                         |           |                 |      |
|               |            | Average       | 4.38                    | 4.43 4.45 | 4.39            | 4.48 |
PerceivedUtility(↑)
NaturalQuestions
|     | ListLongAnswer |     | TableLongAnswer | ParagraphLongAnswer |     |     |
| --- | -------------- | --- | --------------- | ------------------- | --- | --- |
NoAnswer
|               | HasShort | NoShort | HasShort NoShort | HasShort | NoShort |      |
| ------------- | -------- | ------- | ---------------- | -------- | ------- | ---- |
| BingChat      | 4.63     | 4.49    | 4.49 4.47        | 4.53     | 4.40    | 4.38 |
| NeevaAI       | 4.65     | 4.57    | 4.43 4.38        | 4.43     | 4.63    | 4.49 |
| perplexity.ai | 4.71     | 4.61    | 4.60 4.55        | 4.77     | 4.58    | 4.50 |
| YouChat       | 4.72     | 4.64    | 4.70 4.54        | 4.77     | 4.77    | 4.70 |
| Average       | 4.68     | 4.58    | 4.55 4.49        | 4.62     | 4.60    | 4.52 |
Table6: Humanevaluationresultsforperceivedutilityofgeneratedresponses(five-pointLikertratings). Ingeneral,
responsesfromexistinggenerativesearchenginesappearinformativeanduseful.

G CitationRecallandPrecision
Table 7 presents generative search engine citation recall across the evaluated query distributions, and
Table8presentscitationprecision.
CitationRecall(%;↑)
CitationRecall(%;↑)
|               | AverageOver |                    |     |                         |           | ELI5    |                 |      |
| ------------- | ----------- | ------------------ | --- | ----------------------- | --------- | ------- | --------------- | ---- |
|               | AllQueries  |                    |     | AllSouls davinci-debate |           |         | WikiHowKeywords |      |
|               |             |                    |     |                         | KILT      | Live    |                 |      |
| BingChat      |             | 58.7 BingChat      |     | 55.6                    | 57.1 59.8 | 59.9    |                 | 50.7 |
| NeevaAI       |             | 67.6 NeevaAI       |     | 55.3                    | 66.3 66.6 | 61.6    |                 | 72.5 |
| perplexity.ai |             | 68.7 perplexity.ai |     | 63.0                    | 64.2 64.8 | 58.1    |                 | 74.6 |
| YouChat       |             | 11.1 YouChat       |     | 3.2                     | 3.9       | 3.0 4.6 |                 | 12.1 |
| Average       |             | 51.5 Average       |     | 44.3                    | 47.9 48.5 | 46.0    |                 | 52.5 |
CitationRecall(%;↑)
NaturalQuestions
|     |     | ListLongAnswer | TableLongAnswer |     | ParagraphLongAnswer |     |     |     |
| --- | --- | -------------- | --------------- | --- | ------------------- | --- | --- | --- |
NoAnswer
|               |     | HasShort NoShort | HasShort | NoShort   | HasShort | NoShort |      |      |
| ------------- | --- | ---------------- | -------- | --------- | -------- | ------- | ---- | ---- |
| BingChat      |     | 74.1 60.6        |          | 63.5 49.2 | 72.1     |         | 66.3 | 61.9 |
| NeevaAI       |     | 73.0 64.2        |          | 69.5 65.1 | 75.0     |         | 74.8 | 65.6 |
| perplexity.ai |     | 85.3 74.4        |          | 79.6 62.4 | 84.9     |         | 75.9 | 68.4 |
| YouChat       |     | 21.6 16.6        |          | 30.6 11.5 | 31.6     |         | 21.8 | 17.8 |
| Average       |     | 63.5 53.9        |          | 60.8 47.1 | 65.9     |         | 59.7 | 53.4 |
Table 7: Human evaluation results of citation recall in existing generative search engines. Citation recall is
concerningly low (many generated statements are not fully supported by citations), especially given that these
systemsalreadyhavemillionsofusersandmayserveasaprimarytoolforfulfillinguserinformationneeds.

CitationPrecision(%;↑)
CitationPrecision(%;↑)
ELI5
AverageOver
|               |                    | AllSouls davinci-debate |           | WikiHowKeywords |      |
| ------------- | ------------------ | ----------------------- | --------- | --------------- | ---- |
|               | AllQueries         |                         | KILT      | Live            |      |
| BingChat      | 89.5 BingChat      | 88.8                    | 88.8 87.6 | 87.2            | 92.1 |
| NeevaAI       | 72.0 NeevaAI       | 69.8                    | 74.1 75.7 | 73.8            | 74.0 |
| perplexity.ai | 72.7 perplexity.ai | 61.7                    | 68.4 64.9 | 66.3            | 77.4 |
| YouChat       | 63.6 YouChat       | 51.1                    | 50.0 64.7 | 57.9            | 71.1 |
| Average       | 74.5 Average       | 67.8                    | 70.3 73.2 | 71.3            | 78.7 |
CitationPrecision(%;↑)
NaturalQuestions
|     | ListLongAnswer | TableLongAnswer | ParagraphLongAnswer |     |     |
| --- | -------------- | --------------- | ------------------- | --- | --- |
NoAnswer
|               | HasShort NoShort | HasShort NoShort | HasShort | NoShort |      |
| ------------- | ---------------- | ---------------- | -------- | ------- | ---- |
| BingChat      | 86.8 86.8        | 89.0 92.5        | 92.9     | 91.3    | 90.8 |
| NeevaAI       | 73.2 67.6        | 67.1 64.2        | 73.4     | 76.5    | 70.8 |
| perplexity.ai | 82.1 81.0        | 76.0 71.7        | 83.8     | 79.7    | 74.0 |
| YouChat       | 63.3 62.7        | 64.8 56.1        | 75.7     | 67.5    | 58.6 |
| Average       | 76.4 74.5        | 74.2 71.1        | 81.5     | 78.7    | 73.5 |
Table8: Humanevaluationresultsofcitationprecisioninexistinggenerativesearchengines. Citationprecisionis
concerninglylow(manygeneratedcitationsdonotsupporttheirassociatedstatements),especiallygiventhatthese
systemsalreadyhavemillionsofusersandmayserveasaprimarytoolforfulfillinguserinformationneeds.

H CitationF
1
Table9presentsthecitationF foreveryevaluatedgenerativesearchengineoneachquerydistribution.
1
|               |     | CitationF | (↑) |     |     |     |
| ------------- | --- | --------- | --- | --- | --- | --- |
| CitationF (↑) |     |           | 1   |     |     |     |
1
ELI5
AverageOver
|               |            |               | AllSouls davinci-debate |           | WikiHowKeywords |      |
| ------------- | ---------- | ------------- | ----------------------- | --------- | --------------- | ---- |
|               | AllQueries |               |                         | KILT      | Live            |      |
| BingChat      | 70.9       | BingChat      | 68.4                    | 69.5 71.1 | 71.0            | 65.4 |
| NeevaAI       | 69.8       | NeevaAI       | 61.7                    | 70.0 70.8 | 67.1            | 73.2 |
| perplexity.ai | 70.6       | perplexity.ai | 62.3                    | 66.2 64.8 | 62.0            | 76.0 |
| YouChat       | 18.9       | YouChat       | 6.0                     | 7.2       | 5.6 8.5         | 20.7 |
| Average       | 57.6       |               |                         |           |                 |      |
|               |            | Average       | 49.6                    | 53.2 53.1 | 52.2            | 58.8 |
| CitationF     | (↑)        |               |                         |           |                 |      |
1
NaturalQuestions
|     | ListLongAnswer |     | TableLongAnswer | ParagraphLongAnswer |     |     |
| --- | -------------- | --- | --------------- | ------------------- | --- | --- |
NoAnswer
|               | HasShort | NoShort | HasShort NoShort                | HasShort | NoShort |      |
| ------------- | -------- | ------- | ------------------------------- | -------- | ------- | ---- |
| BingChat      | 79.9     | 71.4    | 74.1 64.2                       | 81.2     | 76.8    | 73.6 |
| NeevaAI       | 73.1     | 65.9    | 68.3 64.6                       | 74.2     | 75.7    | 68.1 |
| perplexity.ai | 83.7     | 77.5    | 77.8 66.7                       | 84.3     | 77.7    | 71.1 |
| YouChat       | 32.2     | 26.2    | 41.5 19.2                       | 44.6     | 32.9    | 27.4 |
| Average       | 67.2     | 60.2    | 65.4 53.7                       | 71.1     | 65.8    | 60.0 |
|               |          | Table9: | CitationF ofgeneratedresponses. |          |         |      |
1