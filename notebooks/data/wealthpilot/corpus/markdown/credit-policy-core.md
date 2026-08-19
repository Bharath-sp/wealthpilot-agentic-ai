# Ashva Capital Credit Policy Manual: Core Underwriting Standards

# ASHVA CAPITAL PRIVATE LIMITED
## INTERNAL CREDIT POLICY MANUAL
**DOCUMENT REF:** ACPL-CPM-2024-V3  
**SUBJECT:** SECTION 4 – SME TERM LOAN UNDERWRITING STANDARDS  
**ISSUING AUTHORITY:** OFFICE OF THE CHIEF CREDIT OFFICER  

---

### 4.1 MINIMUM ELIGIBILITY & FINANCIAL RATIO THRESHOLDS

4.1.1 **Operating History:** The borrowing entity must possess a verified uninterrupted operating history of not less than 24 months, measured from the date of official incorporation or GST registration to the date of loan application submission. Applications from entities with less than 24 months of operational continuous trace are automatically rejected at the system intake layer.

4.1.2 **Debt-Service Coverage Ratio (DSCR):** The minimum acceptable Debt-Service Coverage Ratio (DSCR) for any SME Term Loan candidate is 1.25x. 
* 4.1.2.1 DSCR is calculated as:  
  $$\text{DSCR} = \frac{\text{Net Operating Income} + \text{Depreciation} + \text{Amortization}}{\text{Annual Principal Payments} + \text{Annual Interest Expense} + \text{Proposed Ashva Capital Annual Debt Service}}$$
* 4.1.2.2 Calculation shall be based on audited financial statements for the preceding two fiscal years plus trailing twelve-month (TTM) bank account statements. No exceptions or waivers to the 1.25x floor are permitted without prior written approval from the Chief Credit Officer under Exception Clause 4.5.1.

4.1.3 **Current Ratio Floor:** The borrowing entity must maintain a minimum Current Ratio of 1.15x calculated as Current Assets divided by Current Liabilities. 
* 4.1.3.1 For the purposes of this calculation, short-term director loans without a minimum 36-month subordination agreement shall be categorized under Current Liabilities.

4.1.4 **Maximum Leverage:** Total Debt to Tangible Net Worth (TD/TNW) shall not exceed 3.00x post-drawdown.
* 4.1.4.1 Total Debt includes all funded interest-bearing bank borrowings, non-bank financial institution (NBFC) obligations, equipment leases, and the full approved principal amount of the proposed Ashva Capital SME Term Loan.
* 4.1.4.2 Tangible Net Worth is calculated as Paid-Up Share Capital + Free Reserves − Intangible Assets − Deferred Tax Assets − Loans/Advances to Related Parties.

---

### 4.2 BUREAU SCORE BANDS AND OPERATIONAL PERMISSIONS

4.2.1 **Primary Commercial & Consumer Score Standard:** Underwriters must evaluate both the entity commercial bureau score (CIBIL Rank / CMR) and the personal consumer bureau score (CIBIL TransUnion v3) of all primary promoters holding 25% or greater equity in the borrowing business.

4.2.2 **Bureau Score Band Matrix:**

| Band | Commercial Rank (CMR) | Promoter CIBIL Score | Permitted Actions & Product Limits | Risk Premium Adjustments |
| :--- | :--- | :--- | :--- | :--- |
| **Band A** | CMR 1 to CMR 3 | 775 and above | Eligible for maximum allowable loan tenor (60 months) and maximum unsecured exposure. Straight-Through Processing (STP) auto-approval enabled for requests $\le$ ₹5,000,000. | Base Risk Rate (0.00% Spread Addition) |
| **Band B** | CMR 4 to CMR 5 | 725 to 774 | Eligible for loan tenors up to 36 months. Manual underwriting mandatory. Maximum loan cap: ₹15,000,000. | Base Rate + 1.25% per annum |
| **Band C** | CMR 6 | 675 to 724 | Conditional approval only. Tenor capped at 24 months. Maximum loan cap: ₹5,000,000. Mandates a 100% personal guarantee from all promoters and a charge over fixed assets equal to 1.10x loan value. | Base Rate + 2.75% per annum |
| **Band D** | CMR 7 to CMR 10 | Below 675 | **Decline.** Application is hard-locked by the credit decisioning system. | N/A (Ineligible) |

4.2.3 **Bureau Derogatory Overrides:** Regardless of numerical score, any instance of a written-off trade line, suit-filed account, or overdue status greater than 30 days past due (DPD) within the preceding 12 months across any commercial or personal credit facility shall immediately classify the application into Band D (Decline).

---

### 4.3 LOAN-SIZE TIERS AND APPROVAL AUTHORITY MATRIX

4.3.1 **Tier Assignment:** Loan applications are classified into four discrete tiers based on aggregate gross exposure requested (inclusive of existing outstanding obligations with Ashva Capital).

4.3.2 **Approval Matrix Table:**

```
+-----------------------------------------------------------------------------------+
| TIER | AMOUNT RANGE (INR)         | MANDATORY APPROVAL AUTHORITY                  |
+------+----------------------------+-----------------------------------------------+
| I    | Up to ₹1,500,000           | Junior Underwriting Officer (JUO)             |
| II   | ₹1,500,001 to ₹5,000,000   | Senior Underwriting Officer (SUO)             |
| III  | ₹5,000,001 to ₹25,000,000  | Credit Committee (Minimum 2 Standing Members) |
| IV   | ₹25,000,001 to ₹50,000,000 | Board Credit Committee                        |
+-----------------------------------------------------------------------------------+
```

4.3.3 **Tier I Approval Authority:** Junior Underwriting Officers (JUO) may independently approve applications up to ₹1,500,000 provided all baseline parameters in Clauses 4.1.1 through 4.1.4 meet or exceed standard policy thresholds without reliance on waivers.

4.3.4 **Tier II Approval Authority:** Senior Underwriting Officers (SUO) hold single-signatory authority for amounts from ₹1,500,001 up to ₹5,000,000.

4.3.5 **Tier III Approval Authority (Credit Committee):** Facilities exceeding ₹5,000,000 up to ₹25,000,000 must be reviewed and unanimously approved by the internal Credit Committee.
* 4.3.5.1 Quorum for the Credit Committee requires at least two (2) standing voting members: the Chief Risk Officer (CRO) or Head of Credit Analysis, and a designated Senior Credit Approver (SCA).

4.3.6 **Tier IV Approval Authority (Board Credit Committee):** Facilities exceeding ₹25,000,000 up to the single borrower limit of ₹50,000,000 must be approved by the Board Credit Committee, comprising the Managing Director, the Chief Credit Officer, and one Independent Director.

---

### 4.4 HUMAN SIGNATORY MANDATE FOR HIGH-VALUE DISBURSEMENTS

4.4.1 **Absolute Limit on Automated Approvals:** No loan approval or disbursement exceeding ₹5,000,000 (Five Million Indian Rupees) shall be executed relying solely on automated credit decisioning engines, algorithmic scoring models, or automated straight-through processing (STP) pipelines.

4.4.2 **Named Signatory Requirement:** Any loan approved above ₹5,000,000 requires the physical or verified digital signature (Class 3 PKI Certificate) of a designated, named human credit officer possessing appropriate delegation authority as defined under Clauses 4.3.5 and 4.3.6.

4.4.3 **Audit & Compliance Control:** The Core Banking System (CBS) and Loan Origination System (LOS) are strictly programmed to enforce a system lock on disbursement API calls for loan values > ₹5,000,000 until a valid, authenticated user ID tied to a human Credit Committee member attaches an authorized approval memorandum and cryptographic digital signature. Any system override attempt triggers an automated alert to the Head of Internal Audit and the Chief Compliance Officer within 60 minutes.

---

### 4.5 DEVIATION AND EXCEPTION MANAGEMENT

4.5.1 **Delegation of Exception Authority:** Financial ratio deviations (e.g., DSCR between 1.15x and 1.24x, or Current Ratio between 1.05x and 1.14x) may only be approved under Tier III or Tier IV authority. Underwriting Officers at Tier I and Tier II levels hold zero authority to grant policy deviations.

4.5.2 **Exception Cap:** The aggregate volume of approved loans containing policy deviations must not exceed 5.0% of total loan disbursements by value in any given fiscal quarter. The Risk Analytics Unit shall publish a monthly Deviation Tracking Report directly to the Board of Directors.
