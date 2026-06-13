# RAG Evaluation Paper Library

This directory stores the RAG evaluation literature used by this repository.

- `papers/pdf/`: downloaded PDFs.
- `papers/markdown/`: Markdown converted from the PDFs with `markitdown`.

The Markdown files are useful for search, note taking, and LLM-assisted reading.
They are not publication-quality transcriptions; PDF layout, tables, math, and
author metadata may contain conversion artifacts.

## Core Evaluation Frameworks

| Paper | Source | PDF | Markdown | Why it matters |
| --- | --- | --- | --- | --- |
| RAGAS: Automated Evaluation of Retrieval Augmented Generation | [arXiv:2309.15217](https://arxiv.org/abs/2309.15217) | [PDF](papers/pdf/ragas-2309.15217.pdf) | [MD](papers/markdown/ragas-2309.15217.md) | Reference-free RAG metrics: faithfulness, answer relevancy, context precision, context recall. |
| ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | [arXiv:2311.09476](https://arxiv.org/abs/2311.09476) | [PDF](papers/pdf/ares-2311.09476.pdf) | [MD](papers/markdown/ares-2311.09476.md) | Trains lightweight judges for context relevance, answer faithfulness, and answer relevance. |

## RAG Benchmarks and Stress Tests

| Paper | Source | PDF | Markdown | Why it matters |
| --- | --- | --- | --- | --- |
| CRAG: Comprehensive RAG Benchmark | [arXiv:2406.04744](https://arxiv.org/abs/2406.04744) | [PDF](papers/pdf/crag-2406.04744.pdf) | [MD](papers/markdown/crag-2406.04744.md) | Tests realistic RAG behavior across dynamic facts, entity popularity, and multiple domains. |
| RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems | [arXiv:2407.11005](https://arxiv.org/abs/2407.11005) | [PDF](papers/pdf/ragbench-2407.11005.pdf) | [MD](papers/markdown/ragbench-2407.11005.md) | Large explainable RAG benchmark and TRACe-style evaluation data. |
| RGB: Benchmarking Large Language Models in Retrieval-Augmented Generation | [arXiv:2309.01431](https://arxiv.org/abs/2309.01431) | [PDF](papers/pdf/rgb-2309.01431.pdf) | [MD](papers/markdown/rgb-2309.01431.md) | Tests noise robustness, negative rejection, information integration, and counterfactual robustness. |
| MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries | [arXiv:2401.15391](https://arxiv.org/abs/2401.15391) | [PDF](papers/pdf/multihop-rag-2401.15391.pdf) | [MD](papers/markdown/multihop-rag-2401.15391.md) | Focuses on multi-hop evidence retrieval and reasoning. |
| NoMIRACL: Knowing When You Don't Know | [arXiv:2312.11361](https://arxiv.org/abs/2312.11361) | [PDF](papers/pdf/nomiracl-2312.11361.pdf) | [MD](papers/markdown/nomiracl-2312.11361.md) | Tests refusal and abstention when retrieval evidence is insufficient. |

## Citation, Attribution, and Verifiability

| Paper | Source | PDF | Markdown | Why it matters |
| --- | --- | --- | --- | --- |
| ALCE: Enabling Large Language Models to Generate Text with Citations | [arXiv:2305.14627](https://arxiv.org/abs/2305.14627) | [PDF](papers/pdf/alce-2305.14627.pdf) | [MD](papers/markdown/alce-2305.14627.md) | Evaluates whether generated claims are properly supported by citations. |
| Evaluating Verifiability in Generative Search Engines | [arXiv:2304.09848](https://arxiv.org/abs/2304.09848) | [PDF](papers/pdf/generative-search-verifiability-2304.09848.pdf) | [MD](papers/markdown/generative-search-verifiability-2304.09848.md) | Audits citation precision and recall in generative search. |

## Factuality and Grounding

| Paper | Source | PDF | Markdown | Why it matters |
| --- | --- | --- | --- | --- |
| FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | [arXiv:2305.14251](https://arxiv.org/abs/2305.14251) | [PDF](papers/pdf/factscore-2305.14251.pdf) | [MD](papers/markdown/factscore-2305.14251.md) | Splits generations into atomic facts and checks support, useful for wiki consistency tests. |
| Long-form Factuality in Large Language Models / SAFE | [arXiv:2403.18802](https://arxiv.org/abs/2403.18802) | [PDF](papers/pdf/safe-long-form-factuality-2403.18802.pdf) | [MD](papers/markdown/safe-long-form-factuality-2403.18802.md) | Search-augmented factuality evaluation for long-form answers. |
| The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality | [arXiv:2512.10791](https://arxiv.org/abs/2512.10791) | [PDF](papers/pdf/facts-grounding-2512.10791.pdf) | [MD](papers/markdown/facts-grounding-2512.10791.md) | Broad factuality leaderboard with grounding-oriented evaluation tracks. |

## Retriever and Knowledge-Intensive Task Benchmarks

| Paper | Source | PDF | Markdown | Why it matters |
| --- | --- | --- | --- | --- |
| BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models | [arXiv:2104.08663](https://arxiv.org/abs/2104.08663) | [PDF](papers/pdf/beir-2104.08663.pdf) | [MD](papers/markdown/beir-2104.08663.md) | Standard retrieval benchmark for Recall@k, nDCG@k, and MRR-style component testing. |
| KILT: a Benchmark for Knowledge Intensive Language Tasks | [arXiv:2009.02252](https://arxiv.org/abs/2009.02252) | [PDF](papers/pdf/kilt-2009.02252.pdf) | [MD](papers/markdown/kilt-2009.02252.md) | Evaluates knowledge-intensive tasks with provenance over a shared Wikipedia snapshot. |

## Surveys

| Paper | Source | PDF | Markdown | Why it matters |
| --- | --- | --- | --- | --- |
| Evaluation of Retrieval-Augmented Generation: A Survey | [arXiv:2405.07437](https://arxiv.org/abs/2405.07437) | [PDF](papers/pdf/rag-evaluation-survey-2405.07437.pdf) | [MD](papers/markdown/rag-evaluation-survey-2405.07437.md) | Compact map of RAG evaluation dimensions and metrics. |
| Retrieval Augmented Generation Evaluation in the Era of Large Language Models: A Comprehensive Survey | [arXiv:2504.14891](https://arxiv.org/abs/2504.14891) | [PDF](papers/pdf/rag-evaluation-comprehensive-survey-2504.14891.pdf) | [MD](papers/markdown/rag-evaluation-comprehensive-survey-2504.14891.md) | Broader survey for related-work framing and metric taxonomy. |

## Suggested Reading Order

1. Read the two surveys to define the taxonomy.
2. Use RAGAS and ARES for the first implementation layer.
3. Use RGB, CRAG, MultiHop-RAG, and NoMIRACL as stress-test families.
4. Use ALCE, FActScore, and SAFE for the LLM wiki stability and grounding layer.
5. Use BEIR and KILT to separate retriever quality from end-to-end RAG behavior.
