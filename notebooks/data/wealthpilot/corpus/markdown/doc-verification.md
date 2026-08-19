# Document Verification and Fraud Screening Procedure

**DOCUMENT CONTROL NUMBER:** MAN-ASH-CRED-2024-V3  
**ISSUING AUTHORITY:** Office of the Chief Credit Officer, Ashva Capital Commercial Lending Limited  
**EFFECTIVE DATE:** November 1, 2024  
**TARGET AUDIENCE:** Commercial Credit Underwriters, Operations Analysts, Risk & Fraud Officers  
**CLASSIFICATION:** Internal Strictly Confidential  

---

### POLICY MANUAL SECTION 7: SME DOCUMENT VERIFICATION & FRAUD RISK CONTROL PROCEDURES

#### 7.1 MANDATORY DOCUMENTATION MATRIX
Every Small and Medium Enterprise (SME) credit application submitted to Ashva Capital for facilities exceeding INR 2,500,000 (or equivalent foreign currency) must contain the complete mandatory document set set forth in Table 7.1 prior to underwriting initiation. Incomplete submissions shall be auto-rejected by the Credit Decision Engine (CDE) after 72 hours of initial portal upload.

##### Table 7.1: Mandatory Document Requirements
| Ref Code | Document Description | Minimum Period / Qualification | Source Format Required |
| :--- | :--- | :--- | :--- |
| **DOC-01** | Primary Operational Bank Statements | 12 consecutive months ending no earlier than 15 days prior to application date | Direct API Feed / Original digital PDF (unprotected) |
| **DOC-02** | Goods and Services Tax (GST) / Sales Tax Returns | Last 4 consecutive quarters (Form GST-3B and GSTR-1 equivalent) | Downloaded directly from Tax Authority Portal |
| **DOC-03** | Audited Financial Statements | Last 2 completed Financial Years (P&L, Balance Sheet, Notes, Cash Flow) | Signed PDF with valid Unique Document Identification Number (UDIN) |
| **DOC-04** | Entity Proof & Operating License | Valid Registration/Incorporation Certificate, Partnership Deed, or MOA/AOA | Government Portal Verified Copy |
| **DOC-05** | KYC of Key Controlling Persons | Beneficial Owners holding $\ge 15.0\%$ equity interest and all executive directors | Government-issued ID + Video KYC |
| **DOC-06** | Facility Proof of Premises | Utility Bill or Registered Lease Agreement | Dated within 60 days of application |

---

#### 7.2 STEP-BY-STEP VERIFICATION PROTOCOLS

##### 7.2.1 Bank Statement Verification Protocol
1. **Ingestion & Parsing:** Underwriters must process all electronic bank statements through the *AshvaParse Engine v3.2*. Statements rendered as scanned images or flat raster files are non-compliant; they must be re-sourced directly from the applicant’s banking portal via Account Aggregator API or direct digital PDF download.
2. **Opening/Closing Balance Continuity:** The closing balance of Month *N* must match the opening balance of Month *N+1* with zero variance ($INR\ 0.00$). Any discrepancy indicates file tampering and requires an immediate Fraud Hold under Section 7.4.
3. **Transaction Reconciliation:**
   * 100% of single credit/debit entries exceeding INR 500,000 must be auto-categorized by counterparty.
   * Cash deposit volume shall not exceed 10.0% of total monthly credits. Cash credit volumes exceeding 10.0% require a hair-cut to eligible monthly inflows equal to $1.5 \times \text{cash volume in excess of 10.0\%}$.
4. **Metadata Audit:** Underwriters must inspect PDF metadata properties. File creation dates occurring *after* the stated statement period end-date, or metadata indicating editing tools (e.g., *iText*, *Quartz PDFContext*, *PDFedit*, *Adobe Acrobat Pro Edit Suite*), shall trigger an automatic Fraud Hold.

##### 7.2.2 GST / Indirect Tax Return Verification Protocol
1. **API Tax Verification:** Underwriters must pull the taxpayer record directly via the Ashva-GSTN API gateway.
2. **Turnover Cross-Check:** 
   * Aggregate gross turnover declared in GSTR-1 (Outward Supplies) across the 12-month period must be reconciled against the tax paid in Form GSTR-3B.
   * The variance between total turnover reported in GSTR-1 and GSTR-3B must not exceed $2.0\%$.
3. **Status Check:** The GSTIN status must be "Active". If the status reflects "Suspended", "Cancelled", or "Pending Cancellation", the application is hard-stopped and rejected immediately.

##### 7.2.3 Audited Financial Statements Verification Protocol
1. **UDIN Portal Validation:** Underwriters must extract the Chartered Accountant’s (CA) Unique Document Identification Number (UDIN) from the audit report and execute a query on the Institute of Chartered Accountants Official Verification Portal within 24 hours of receipt.
2. **Auditor Credential Audit:** The signing auditor or firm must not appear on the Ashva Capital Disqualified Auditor List (Ref: `APP-RISK-BLK-2024-Q3`).
3. **Internal Math Check:** Underwriters must verify that:
   * $\text{Total Assets} - \text{Total Liabilities} = \text{Shareholders' Equity}$ (Max deviation allowed: $INR\ 0.00$).
   * Net Profit after Tax (PAT) matches between the P&L Statement and the Retained Earnings schedule in the Balance Sheet.

---

#### 7.3 REVENUE RECONCILIATION & TOLERANCE THRESHOLDS

Underwriters must compute the **Verified Annual Gross Revenue (VAGR)**, which is defined as the lowest value among:
$$\text{VAGR} = \min\left(\text{Declared App Revenue}, \text{Annualized 12-M Bank Credits}, \text{Annualized 12-M GST Turnover}\right)$$

##### Table 7.2: Revenue Variance Tolerance Thresholds & Action Matrix
| Variance Range | Calculation Formula | Permitted Action | Required Approval Level |
| :--- | :--- | :--- | :--- |
| **Tier 1:** $\le 5.0\%$ | $\frac{|\text{Declared} - \text{Verified}|}{\text{Declared}} \times 100 \le 5.0\%$ | Auto-accept verified figure. Proceed to CDE underwriting. | Level 1: Junior Credit Analyst (Sethi, V.) |
| **Tier 2:** $> 5.0\%$ to $\le 12.0\%$ | $\frac{|\text{Declared} - \text{Verified}|}{\text{Declared}} \times 100 \in (5.0, 12.0]$ | Manual Underwriting required. Credit exposure capped at $80\%$ of baseline model limit. | Level 2: Senior Credit Manager (Deshmukh, A.) |
| **Tier 3:** $> 12.0\%$ to $\le 20.0\%$ | $\frac{|\text{Declared} - \text{Verified}|}{\text{Declared}} \times 100 \in (12.0, 20.0]$ | Mandatory exception review. Requires 2 years of IT Returns to validate non-operating income. | Level 3: Head of Underwriting (Mehta, R.) |
| **Tier 4:** $> 20.0\%$ | $\frac{|\text{Declared} - \text{Verified}|}{\text{Declared}} \times 100 > 20.0\%$ | **Hard Stop.** Automatic rejection. Applicant blocked from re-applying for 180 days. | System Enforced / Chief Credit Officer (Varma, A.) |

##### 7.3.1 Bank vs. GST Turnover Specific Tolerance
* Where **12-Month Total Bank Operational Credits** diverge from **12-Month Gross GST Turnover**:
  * Variance $\le 8.0\%$: Acceptable without escalation.
  * Variance $> 8.0\%$ and $\le 15.0\%$: Underwriter must confirm if non-taxable exports or exempt supplies account for the gap. A detailed reconciliation note must be attached to the credit memorandum.
  * Variance $> 15.0\%$: Mandatory rejection unless written sign-off is granted by Level 3 (Head of Underwriting).

---

#### 7.4 MANDATORY FRAUD HOLD TRIGGERS (RED FLAGS)

The occurrence of any single Red Flag detailed below mandates an immediate, system-enforced **Fraud Hold**. Underwriters are strictly prohibited from overriding a Fraud Hold without written clearance from the Fraud Risk Group (FRG).

##### 7.4.1 Document Integrity & Digital Artifact Red Flags
1. **Font Inconsistency:** Presence of more than two distinct font families within transaction line items of a single bank statement page, or character pitch variations exceeding $0.5\text{ pt}$ on line item figures.
2. **Software Footprint:** Metadata indicating creation by open-source PDF manipulation utilities or graphic editing software (*GIMP*, *Photoshop*, *PDF2Go*, *Canva*, *Sejda*).
3. **Layer Anomalies:** Unflattened vector text overlays detected above rasterized background images during parsing by *AshvaParse Engine*.

##### 7.4.2 Transactional & Operational Red Flags
1. **Circular Flow Patterns:** Any instance where $\ge 80.0\%$ of funds transferred to a third party return to the applicant’s bank accounts within 48 hours, where individual batch values exceed INR 1,000,000.
2. **Sequential Invoicing:** Three or more invoices issued to structurally non-affiliated buyers possessing sequential invoice control numbers, accounting for $> 35.0\%$ of cumulative quarterly revenue.
3. **Tax Stagnation:** GST Returns reflecting reported gross turnover $> \text{INR } 5,000,000$ per quarter, but zero net cash tax liability paid (100% satisfied via Input Tax Credit claims) for 2 consecutive quarters, without physical inventory verification.
4. **UDIN Invalidation:** The UDIN portal returns "Revoked", "Expired", or details an entity name differing from the applicant company name.

---

#### 7.5 ESCALATION PATHWAY & FRAUD CLEARANCE TIMELINES

When a Fraud Hold is triggered or revenue discrepancy tolerances cross Tier 2 boundaries, the file must follow the precise escalation hierarchy defined below.

```
[Underwriter / Credit Analyst] 
              │
              ├── (Fraud Hold Triggered) ──────► [Fraud Risk Group (FRG)]
              │                                      │ (Investigation Max 24 Hrs)
              │                                      ▼
              │                             [FRG Clear / Reject Memo]
              │                                      │
              ├── (Tier 2 Discrepancy: 5.1-12.0%) ───┼─► [Level 2: Senior Manager]
              │                                      │
              ├── (Tier 3 Discrepancy: 12.1-20.0%) ──┼─► [Level 3: Head of Underwriting]
              │                                      │
              └── (Policy Override Request) ─────────┴─► [Level 4: Chief Credit Officer]
```

##### 7.5.1 Escalation Procedures and Timelines
1. **Notification Deadline:** The Underwriter must log the Fraud Hold in the Loan Origination System (LOS) within **2 business hours** of discovery. This automatically locks the file against approval routing.
2. **Fraud Risk Group (FRG) SLA:** The FRG, led by Chief Fraud Officer *Nikhil Roy*, must complete a forensic review within **24 business hours** of ticket creation.
   * **FRG Release:** Requires a formal Fraud Clearance Memo signed by an FRG Manager.
   * **FRG Rejection:** Application is permanently designated as *Declined - Suspected Fraud* and logged in the Industry Fraud Registry within **48 hours**.
3. **Numeric Approval Authority Limits:**

##### Table 7.3: Escalation Authority Matrix
| Level | Officer Name / Title | Maximum Facility Limit | Authorized Override Scope |
| :--- | :--- | :--- | :--- |
| **Level 1** | Vikram Sethi, Junior Credit Analyst | INR 10,000,000 | Tier 1 Variances ($\le 5.0\%$) |
| **Level 2** | Ananya Deshmukh, Senior Credit Manager | INR 30,000,000 | Tier 2 Variances ($5.1\% - 12.0\%$), Bank/GST Variance up to $15.0\%$ |
| **Level 3** | Rohan Mehta, Head of Underwriting | INR 100,000,000 | Tier 3 Variances ($12.1\% - 20.0\%$), Audit exceptions |
| **Level 4** | Arjun Varma, Chief Credit Officer | Unlimited | Policy Mandate Overrides, Final Appeal on Fraud Holds |

4. **Prohibition of Verbal Approvals:** All approvals, sign-offs, and exceptions must be documented in writing within the LOS audit trail. Verbal, messaging app, or unrecorded email approvals are void and constitute a material breach of credit compliance.

---
**APPROVED BY:**  
*Arjun Varma*  
Chief Credit Officer, Ashva Capital Commercial Lending Limited  
*Signature Document Identifier: AV-CCO-8849-ASH*
