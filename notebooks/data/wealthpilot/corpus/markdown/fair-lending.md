# Fair Lending and Non-Discrimination Standard

**ASHVA CAPITAL CREDIT POLICY MANUAL**  
**DOCUMENT REF:** C3-FLS-2024-V4  
**SUBJECT:** FAIR LENDING STANDARDS AND PROHIBITED CREDIT EVALUATION INPUTS  
**EFFECTIVE DATE:** OCTOBER 1, 2024  
**ISSUING AUTHORITY:** OFFICE OF THE CHIEF CREDIT OFFICER  

---

### 12.1.0 OBJECTIVE AND SCOPE

12.1.1 This standard applies to all automated decisioning engines (ADEs), algorithmic scoring models, manual underwriting workflows, and credit risk evaluations conducted by or on behalf of Ashva Capital.

12.1.2 The objective of this policy is to enforce absolute neutrality in credit granting, risk selection, line assignment, and pricing. Underwriting decisions must evaluate creditworthiness strictly through verified financial capacity, repayment history, and leverage metrics.

---

### 12.2.0 ENUMERATED PROTECTED ATTRIBUTES

12.2.1 Underwriters, risk models, credit analysts, and third-party data vendors are strictly prohibited from collecting, ingesting, storing, or evaluating any of the following Protected Attributes in connection with an application for credit:

*   **12.2.1.a Religion:** Religious affiliation, belief, practice, or lack thereof.
*   **12.2.1.b Caste:** Caste, sub-caste, clan, or tribal designation.
*   **12.2.1.c Gender:** Sex, gender identity, expression, or sexual orientation.
*   **12.2.1.d Marital Status:** Single, married, divorced, separated, or widowed status (except where required solely to verify joint liability or enforce a legal security interest).
*   **12.2.1.e Age:** Biological age, except for the sole purpose of confirming legal capacity to enter into a binding contract (minimum threshold: 18 years of age). Age-based declining or tiered scoring is prohibited.
*   **12.2.1.f Disability:** Physical, sensory, intellectual, or psychiatric disability, including receipt of public assistance or disability insurance benefits.
*   **12.2.1.g Region of Origin:** State, province, district, or country of birth, or historical national origin.

---

### 12.3.0 PROHIBITED PROXY VARIABLES

12.3.1 The variables listed below correlate with Protected Attributes and carry high risk of introducing unlawful bias. They are classified as Prohibited Proxy Variables and must be excluded from all credit scorecards, machine learning pipelines, and manual underwriting worksheets:

*   **12.3.1.a Postal Code Alone:** Geographic location at the postal code, PIN code, or neighborhood level. Credit risk models may utilize state-level macroeconomic indicators (e.g., state unemployment rates), but single postal codes or hyper-local geographic identifiers are banned as direct inputs or segmentation keys.
*   **12.3.1.b Applicant First Name:** Given names, middle names, or salutations. All applicant names must be stripped from model ingestion pipelines by the Data Engineering Team using Anonymization Protocol AP-02 prior to scorecard execution.
*   **12.3.1.c Institution of Education:** The identity, ranking, location, or tier of the secondary or tertiary educational institution attended by the applicant. Credit models may evaluate verified income, employment status, or industry tenure, but never the pedigree of the educational institution.
*   **12.3.1.d Language of Application:** The language selected by the applicant during digital onboarding, loan document presentation, or customer support interactions.

---

### 12.4.0 DISPARATE IMPACT TESTING AND MONITORING

12.4.1 **Testing Cadence:** The Fair Lending Risk Unit (FLRU), led by the Head of Credit Analytics (Dr. Aris Thorne), must run statistical disparate-impact audits on all active credit models and manual underwriting portfolios every **30 calendar days**, with formal quarterly reporting submitted to the Risk Management Committee within **10 calendar days** following quarter-end.

12.4.2 **Statistical Threshold (The 80% Rule):** Disparate impact is calculated using the Adverse Impact Ratio (AIR):

$$\text{AIR} = \frac{\text{Approval Rate of Protected Demographic Group}}{\text{Approval Rate of Control/Highest-Approving Group}}$$

*   If the AIR for any protected demographic proxy drops below **0.80 (80%)**, the model feature set fails compliance testing.
*   If an AIR failure occurs, the quantitative team must issue a **Model Suspension Notice** within **24 hours**.
*   The affected decision pipeline must revert to the previous validated non-discriminatory baseline model within **48 hours** of the audit finding.

---

### 12.5.0 VOID RATIONALE AND MANDATORY OVERRIDE RULE

12.5.1 Any underwriting decision—whether an approval, declination, line assignment, or risk-based price adjustment—that references, relies upon, or cites a Protected Attribute (12.2.0) or Prohibited Proxy Variable (12.3.0) in its approval notes, credit committee minutes, or model explainability log (e.g., SHAP/LIME feature attributions) is **void ab initio**.

12.5.2 Upon identification of a void rationale:
1.  The Credit Operations Supervisor must mark the decision status as "VOID - POLICY BREACH" in the Core Banking System within **4 business hours**.
2.  The loan file must be routed to the Chief Credit Officer (Elena Vance) for an independent re-underwriting within **24 business hours**.
3.  The original underwriter or model team responsible for the prohibited rationale must be flagged for internal compliance audit.

---

### 12.6.0 ADVERSE ACTION NOTICE REQUIREMENTS

12.6.1 Every applicant who is declined credit, or who receives a credit line offer below the requested amount by more than **20%**, must be issued an Adverse Action Notice.

12.6.2 **Timeline:** The Adverse Action Notice must be delivered via email or registered SMS within **72 hours** of the underwriting decision, and no later than **14 calendar days** from the date of application submission.

12.6.3 **Mandatory Contents:**
*   **Principal Reasons:** The notice must state precisely **1 to 4 principal financial reasons** for the decision (e.g., "Debt-to-Income ratio exceeds 45%", "Verified monthly income is less than ₹35,000", "Credit bureau record reflects >2 late payments in the past 12 months").
*   **Prohibited Statements:** Generic statements such as "Internal Policy Failure," "System Declination," or any reference to location, name, or language are prohibited.
*   **Bureaus Used:** Full contact details and credit score output of the credit reporting agency used in the evaluation.
*   **Right to Audit:** Explicit instructions informing the applicant of their right to request a full copy of their credit data file within **60 calendar days** at no cost.

---

### 12.7.0 GOVERNANCE AND NAMED EXCEPTIONS

12.7.1 **Zero-Tolerance Exception Rule:** No individual officer, underwriter, or executive—including the Chief Executive Officer—has the authority to grant a policy waiver or exception to Sections 12.2.0 (Protected Attributes) or 12.3.0 (Prohibited Proxies).

12.7.2 Any modification to the list of prohibited variables or statistical testing thresholds requires unanimous sign-off from:
1.  Chief Credit Officer — *Elena Vance*
2.  Chief Risk Officer — *Marcus Vance-Reid*
3.  Head of Regulatory Compliance — *Siddharth Nair*
