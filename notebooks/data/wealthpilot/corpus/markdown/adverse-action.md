# Adverse Action and Applicant Communication Standard

# POLICY MANUAL SECTION 8.4: ADVERSE ACTION AND APPLICATION DECLINE STANDARDS

**Document Identifier:** AC-POL-CRD-084-REV3  
**Effective Date:** October 15, 2024  
**Approved By:** Office of the Chief Credit Officer, Ashva Capital Financial Technologies Inc.  
**Scope:** Applicable to all Credit Risk Personnel, Automated Decisioning Engines, and Underwriting Operations.

---

### 8.4.1 Turnaround Time Standards

8.4.1.1 **Automated Decision Engine Declines:** Applications triggered for decline by the Credit Decisioning System (CDS) hard-stop rules must generate and dispatch the automated Adverse Action Notice to the applicant within fifteen (15) minutes of final payload submission.

8.4.1.2 **Manual Underwriting Declines:** Applications evaluated by a Level 1 or Level 2 Underwriter that result in a decline decision must receive final Underwriting Officer approval and dispatch of the Adverse Action Notice within forty-eight (48) hours of dossier completion.

8.4.1.3 **Hard Ceiling Exception:** Under no circumstances shall an un-adjudicated decline exceed seventy-two (72) hours from initial receipt of the complete application file. Any application exceeding this limit requires immediate automated escalation to the Head of Underwriting Operations and must be resolved within four (4) business hours.

---

### 8.4.2 Mandatory Content of Adverse Action Notices

Every Adverse Action Notice issued by Ashva Capital—whether generated electronically or manually—must explicitly contain the following mandatory elements without exception:

1. **Applicant Identification:** Full Legal Business Name, Primary Applicant Name, Ashva Unique Application Tracking ID (UAT-ID), and Date of Adverse Decision.
2. **Action Taken Statement:** A clear, unambiguous statement that the application for credit extension has been declined.
3. **Approved Reason Codes:** Up to, but no more than, four (4) primary reason codes selected strictly from the Authorized Reason Code Directory (Section 8.4.3). Reasons must be listed in descending order of impact on the credit decision.
4. **Credit Bureau Information:** Where credit score or bureau information contributed to the decision:
   - Full legal name of the credit reporting agency utilized (e.g., Apex Credit Assessment Bureau Inc., CrediCheck Data Systems Ltd.).
   - The exact numerical credit score obtained, the score scale/range, the date the score was generated, and the top four (4) key score-impairing factors provided by the bureau.
   - Standard statutory notice stating that the credit bureau did not make the lending decision and cannot provide specific reasons for the decline.
5. **Notice of Right to Appeal:** Instructions detailing the 14-day window and formal submission pathway for an appeal (Section 8.4.5).
6. **Fair Lending & Non-Discrimination Statement:** The mandatory Ashva Capital Non-Discrimination Compliance Statement and contact details for the Regulatory Oversight Ombudsman.

---

### 8.4.3 Authorized Decline Reason Code Directory

Underwriters and automated systems are strictly restricted to selecting decline reasons from the following exhaustive matrix. No other codes or text descriptions are permitted.

| Reason Code | Official Notice Designation | Precise Metric / Policy Trigger Threshold |
| :--- | :--- | :--- |
| **ARC-101** | Insufficient Debt Service Coverage | Debt Service Coverage Ratio (DSCR) calculated at lower than 1.25x across trailing 12 months (TTM). |
| **ARC-102** | Credit Score Below Minimum Threshold | Commercial/Personal Bureau Score below 680 for Tier-1 products or below 640 for Tier-2 products. |
| **ARC-103** | Excessive Debt-to-Income / Leverage | Total Debt-to-Income (DTI) ratio exceeds 45.0%, or Total Funded Debt-to-EBITDA exceeds 3.50x. |
| **ARC-104** | Uncured Delinquency History | Presence of one or more 30+ days past due (DPD) events within the trailing 12 months across existing credit facilities. |
| **ARC-105** | Insufficient Operating History | Business entity operating under active incorporation for less than twenty-four (24) consecutive calendar months. |
| **ARC-106** | Unverifiable Revenue / Tax Discrepancy | Variance greater than 8.0% between self-reported gross revenue and verified bank transaction statements or tax filings. |
| **ARC-107** | Excluded Industry Sector | Primary NAICS code falls within the Prohibited Industry List detailed in Policy Manual Schedule 2.1 (e.g., Adult Entertainment, Unregulated Crypto-Assets, Weapons Manufacturing). |
| **ARC-108** | Outstanding Tax Liens or Legal Judgments | Open tax liens or civil judgments totaling in aggregate greater than $10,000 USD (or local currency equivalent). |
| **ARC-109** | Insolvency / Bankruptcy Record | Active or prior bankruptcy, receivership, or corporate restructuring filings within the preceding seven (7) years. |
| **ARC-110** | Insufficient Tangible Net Worth | Tangible Net Worth (TNW) calculated at less than $250,000 USD for commercial lines exceeding $100,000 USD. |

---

### 8.4.4 Prohibition on Non-Approved Reasons and Free-Text Entries

8.4.4.1 **System Lock:** The Credit Decisioning System (CDS) and Underwriter Management Portal (UMP) are programmatically locked to prevent manual entry, free-text typing, or custom modification of decline reasons. 

8.4.4.2 **Strict Ban on Off-List Reasons:** Underwriters are strictly prohibited from issuing external emails, letter correspondence, or verbal statements to applicants or brokers containing reason descriptions, commentary, or justifications not explicitly mapped to codes ARC-101 through ARC-110.

8.4.4.3 **Compliance Violation Penalty:** Direct or indirect violation of this prohibition constitutes a Tier-1 Compliance Breach. Any staff member entering or communicating unauthorized decline grounds will face immediate suspension of underwriting authority, mandatory re-training, and referral to the Principal Credit Risk Officer (PCRO) for disciplinary review.

---

### 8.4.5 Credit Decision Appeal Process and Deadlines

8.4.5.1 **Eligibility for Appeal:** Declined applicants possess the right to appeal a credit decision solely if they can provide verified, previously unsubmitted material financial information (e.g., cleared tax liens, updated audited financial statements, cured credit bureau errors).

8.4.5.2 **Submission Deadline:** The formal Appeal Dossier must be received via the Ashva Capital Applicant Portal within fourteen (14) calendar days from the timestamp shown on the original Adverse Action Notice. Appeals submitted on day 15 or later are system-rejected without review.

8.4.5.3 **Adjudication Body:** All valid appeals are routed directly to the Credit Appeals Committee (CAC), consisting of the Chief Credit Officer, one Senior Risk Officer, and the Head of Compliance. The original deciding underwriter is barred from voting on the appeal.

8.4.5.4 **Appeal Turnaround Deadline:** The CAC must issue a final, unappealable written decision within five (5) business days of receiving the complete Appeal Dossier.

8.4.5.5 **Appeal Limits:** Applicants are permitted exactly one (1) appeal per declined application tracking ID.

---

### 8.4.6 Record Retention Requirements

8.4.6.1 **Mandatory Retention Period:** In accordance with institutional regulatory standards and internal governance, all records pertaining to declined applications must be retained for a mandatory minimum period of seven (7) years (84 calendar months) from the date of Adverse Action Notice issuance.

8.4.6.2 **Required Archival Artifacts:** The archived file must contain:
1. The full application data payload submitted by the user.
2. Raw credit bureau pull outputs and scoring files.
3. Financial spreading analysis sheets and automated engine logs.
4. Underwriter sign-off logs and time-stamped reason code selections.
5. Exact duplicate PDF copy of the dispatched Adverse Action Notice.
6. Complete communications log, including appeal submissions and CAC decision records, if applicable.

8.4.6.3 **Storage Architecture:** Archives must be written to immutable, write-once-read-many (WORM) storage hosted within Ashva Capital’s secured AWS S3 Glacier environment (`ashva-credit-declines-archive-prod`) with encryption at rest utilizing AES-256 standards. Destruction of decline records prior to the expiration of the 84-month period is technically restricted and prohibited.
