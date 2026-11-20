Accounts payable: Document and image review agent
Build a Python service that reconciles invoices, purchase orders (POs), goods receipts, and standalone
images. Return ready_for_approval, needs_review, or reject with cited evidence. Use Azure AI Foundry,
Content Understanding, and Azure AI Search. Simulate payment/posting actions locally.
Required inputs: Documents and standalone images
Use three labeled scenarios: a clean digital invoice, a noisy invoice photo, and an invoice-PO-receipt
mismatch. Include PDFs, standalone JPEG/PNG invoice and delivery/receipt photos, and one mixed
packet. Use synthetic data and label the expected fields and review decisions.
Build the multimodal processing and retrieval workflow
• Content Understanding: use OCR/layout/tables, build fields (extract/classify/generate), and
contextualize with grounding/confidence. Return Markdown and typed invoice JSON (supplier, IDs,
dates, currency, line items, tax, totals), retaining raw/normalized values and source regions.
• Use prebuilt-invoice and appropriate PO/layout/receipt analyzers. Classify/split/route one mixed packet,
sending unknown types to review. Record service/analyzer versions and explain schema choices.
• Image understanding: analyze delivery/receipt photos with a vision-capable model or image analyzer.
Cite image regions, distinguish OCR from visual observations, and flag unreadable or conflicting
evidence.
• Keep OCR word confidence, field confidence, and correctness distinct; report unavailable scores.
Justify review thresholds with labels, reconcile totals deterministically, and annotate uncertain or
mismatched fields for review.
• Build a Blob-to-Search indexer/skillset pipeline for extraction, chunking, embeddings, and parent-child
records. Index image references, OCR text, visual descriptions, source IDs/versions, invoice metadata,
and access filters. Explain where extraction occurs to avoid duplicate OCR.
• Implement hybrid search in Azure AI Search for document text and image OCR/descriptions. Return
relevant source images/regions or page citations, enforce access filters, and demonstrate one source
update without stale evidence.
• Briefly discuss extensions using Azure Language/Translator, Speech/Video Indexer, analyzer
customization, and knowledge-store audit projections.
1
Agentic review, evaluation, and delivery
• Content Understanding agentic mode (preview): reconcile one bundled invoice/PO/receipt and
derive totalsMatch and discrepancyReasons. Explain escalation from standard extraction; respect the
one-file/document-only limits and unsupported extract-method fields. If unavailable, demonstrate a
Foundry tool-based fallback and explain the difference.
• Use Foundry agent/Responses API tools for retrieval, deterministic reconciliation, and local review-case
creation. Cite document/image evidence; enforce access, human confirmation, argument checks,
bounded steps, and audit state. Replay one request to prove duplicate prevention.
Demonstrate and measure
Run eight representative checks: a clear PDF, a noisy invoice image, visual delivery/receipt evidence, an
amount mismatch or insufficient evidence, denied access, a document prompt injection, a repeated tool
request, and a simulated timeout or rate limit.
• Extraction/review: report critical-field accuracy and review decisions against your labels. Show
annotated source regions, OCR/field confidence, deterministic checks, and the reason for each
decision. A model-generated confidence claim cannot authorize approval.
• Quality/RAG: assess correctness, grounding, citation validity, and retrieval relevance. Use suitable
Azure AI Evaluation evaluators for groundedness/relevance where available; state inputs/thresholds
and check results against labeled financial facts.
• Agent: check intent resolution, tool-call accuracy, and task adherence using the recorded run and tool
results. Demonstrate access isolation, human confirmation, and duplicate prevention. Diagnose one
failure, explain the fix, and show the corrected behavior and response latency.
Safety and operational proof
Demonstrate protection against document prompt injection, unauthorized evidence access, and sensitive
information in output/logs. Explain applicable Foundry safety controls, content-filter severity settings,
protected material, PII, grounding/task adherence, blocklists, and preview constraints. Financial validation
and human approval remain application responsibilities.
Implement a request deadline, bounded retries, and request-correlated logs; demonstrate one simulated
dependency failure. Briefly explain managed identity/RBAC, secret handling, monitoring, deployment,
source re-indexing, and rollback choices.
