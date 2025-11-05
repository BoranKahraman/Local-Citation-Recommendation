# Local-Citation-Recommendation
This project proposes a Local Citation Recommendation (LCR) system for Turkish academic papers, designed to assist researchers by automatically identifying and suggesting relevant citations within a document.
Unlike traditional global citation systems that rely solely on content similarity, this model integrates context awareness—analyzing the local text window around each citation—to deliver more accurate and meaningful references.
<img width="513" height="588" alt="image" src="https://github.com/user-attachments/assets/001ea04f-bfce-4421-bb17-7d7ab0e5e7fe" />


The system uses Natural Language Processing (NLP) techniques and combines BM25 for initial ranking with SciNCL (Scientific Neighborhood Contrastive Learning) for re-ranking, providing both efficiency and contextual depth.
# 🧩 System Architecture

## PDF Parsing (GROBID):
Academic papers in PDF format are parsed into XML using GROBID, extracting metadata, in-text citation markers, and reference lists.

## Citation Context Generation:
Citation markers in the text are detected, and context windows (±50 tokens) are created around each citation for localized understanding.

## Reference Matching:
Citations are matched with their corresponding references using fuzzy string matching (Levenshtein similarity).

## Abstract Retrieval:
Abstracts and metadata are fetched from the DergiPark API and stored in CSV/Pickle databases for model training.

## Ranking and Re-Ranking:
BM25 ranks abstracts based on lexical similarity.
SciNCL, fine-tuned on context–abstract pairs, re-ranks the outputs to capture semantic and contextual relationships.

## Evaluation:
Metrics: Precision@k, MRR (Mean Reciprocal Rank), and NDCG (Normalized Discounted Cumulative Gain).
The model achieves competitive performance, closely approaching BERTurk benchmarks while remaining lightweight and domain-specific.

## ⚙️ Technologies Used
-Python
-GROBID for PDF to XML conversion
-BM25 (Information Retrieval model)
-SciNCL (Neural Re-Ranking model)
-fuzzywuzzy / Levenshtein for text similarity
-DergiPark API for Turkish academic data
-pandas, pickle, scikit-learn, matplotlib for preprocessing and visualization

## 📊 Results
<img width="486" height="121" alt="image" src="https://github.com/user-attachments/assets/c5d6c4c2-4f61-46a7-8430-c680136660f3" />


The system successfully retrieves contextually relevant Turkish academic papers and demonstrates a scalable approach to language-specific citation recommendation.

## 🚀 Future Work
-Development of a user interface for query input and citation visualization.
-Expansion of the Turkish academic dataset for improved generalization.
-Integration of transformer-based models (e.g., BERTurk, GPT-3) for enhanced semantic understanding.
-Performance optimization and model fine-tuning for faster response times.

## 📚 Citation
If you reference this work, please cite:
Akay, S. N., & Kahraman, B. (2024). Local Citation Recommendation for Turkish.
Undergraduate Thesis, Istanbul Technical University, Department of Artificial Intelligence and Data Engineering.

## 🏁 Summary
Our system bridges Turkish academic research with modern NLP by providing accurate, context-aware citation recommendations.
By combining BM25 and SciNCL, it delivers efficiency, relevance, and linguistic adaptability for the Turkish academic ecosystem.
