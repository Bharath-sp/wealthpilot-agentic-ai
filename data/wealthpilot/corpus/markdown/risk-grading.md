# Internal Risk Grading and Pricing Grid

# ASHVA CAPITAL INTERNAL CREDIT POLICY MANUAL
**Document Ref:** ACP-M-2024-V4  
**Section:** 4.0 Risk Grading Methodology and Underwriting Parameters  
**Effective Date:** 1 April 2024  
**Applies To:** All Credit Underwriters, Automated Decision Engines, and Risk Officers  

---

### 4.1 Purpose and Application Rule
4.1.1 This section establishes the official risk grading methodology of Ashva Capital. Underwriters and automated underwriting systems are strictly bound by the thresholds, pricing structures, tenor limits, and collateral mandates defined herein.

4.1.2 **Grade Assignment Rule:** An application shall be assigned the highest risk grade for which it simultaneously satisfies both the minimum Debt Service Coverage Ratio (DSCR) and the minimum bureau score criteria. If an applicant meets the criteria for multiple grades, the underwriting system shall select the grade offering the most favourable terms to the borrower.

4.1.3 **Base Rate:** The Ashva Capital lending base rate is fixed at 9.50% per annum. The indicative interest rate for any facility shall be calculated as the sum of the base rate (9.50%) and the designated basis point spread for the assigned grade.

---

### 4.2 Risk Grading Matrix
The underwriting system shall hold and enforce the following grading grid without exception:

1. **Grade A1**
   * **Quantitative Criteria:** DSCR $\ge 2.00$ **AND** Bureau Score $\ge 750$.
   * **Interest Rate Spread:** 150 basis points over base rate (Indicative Rate: 11.00%).
   * **Maximum Tenor:** 84 months.
   * **Collateral Cover:** 0%.

2. **Grade A2**
   * **Quantitative Criteria:** DSCR $\ge 1.75$ **AND** Bureau Score $\ge 700$.
   * **Interest Rate Spread:** 200 basis points over base rate (Indicative Rate: 11.50%).
   * **Maximum Tenor:** 72 months.
   * **Collateral Cover:** 25%.

3. **Grade B1**
   * **Quantitative Criteria:** DSCR $\ge 1.50$ **AND** Bureau Score $\ge 650$.
   * **Interest Rate Spread:** 275 basis points over base rate (Indicative Rate: 12.25%).
   * **Maximum Tenor:** 60 months.
   * **Collateral Cover:** 50%.

4. **Grade B2**
   * **Quantitative Criteria:** DSCR $\ge 1.35$ **AND** Bureau Score $\ge 600$.
   * **Interest Rate Spread:** 350 basis points over base rate (Indicative Rate: 13.00%).
   * **Maximum Tenor:** 60 months.
   * **Collateral Cover:** 75%.

5. **Grade C1**
   * **Quantitative Criteria:** DSCR $\ge 1.25$ **AND** Bureau Score $\ge 550$.
   * **Interest Rate Spread:** 450 basis points over base rate (Indicative Rate: 14.00%).
   * **Maximum Tenor:** 48 months.
   * **Collateral Cover:** 100%.

6. **Grade C2**
   * **Quantitative Criteria:** DSCR $\ge 1.15$ **AND** Bureau Score $\ge 500$.
   * **Interest Rate Spread:** 575 basis points over base rate (Indicative Rate: 15.25%).
   * **Maximum Tenor:** 36 months.
   * **Collateral Cover:** 125%.

7. **Grade D1**
   * **Quantitative Criteria:** DSCR $\ge 1.00$ **AND** Bureau Score $\ge 450$.
   * **Interest Rate Spread:** 725 basis points over base rate (Indicative Rate: 16.75%).
   * **Maximum Tenor:** 24 months.
   * **Collateral Cover:** 150%.

8. **Grade D2**
   * **Quantitative Criteria:** Anything falling below the D1 thresholds (DSCR $< 1.00$ or Bureau Score $< 450$).
   * **Interest Rate Spread:** 900 basis points over base rate (Indicative Rate: 18.50%).
   * **Maximum Tenor:** 12 months.
   * **Collateral Cover:** 150%.

---

### 4.3 Tenor Constraints and Exception Handling
4.3.1 The tenor offered to any borrower shall not exceed the maximum tenor prescribed for their assigned risk grade under Section 4.2, nor shall it exceed the maximum tenor stipulated for the specific industry sector under Section 9.0 of this manual, whichever is shorter.

4.3.2 If a borrower requests or qualifies for a tenor exceeding the allowable limit defined in 4.3.1, the automated engine shall tag the application with reason code **TENOR_ABOVE_LIMIT** and route the file directly to a human credit reviewer for manual assessment or rejection.

---

### 4.4 Collateral Valuation and Shortfall Rules
4.4.1 Collateral cover is expressed as a mandatory percentage of the total approved loan amount. Valuations must be established by an Ashva Capital-empanelled valuer prior to loan disbursement.

4.4.2 If the verified market value of the pledged collateral is less than the required percentage for the assigned grade, the system shall tag the application with reason code **COLLATERAL_SHORTFALL**.

4.4.3 Any application flagged with **COLLATERAL_SHORTFALL** shall be withheld from automated approval and routed to a human reviewer. Underwriters are prohibited from overriding this flag without explicit sign-off from the Regional Risk Head.

---

### 4.5 Automated Approval Limits and Restrictions
4.5.1 Applications assigned risk grades **A1 through C1** are eligible for automated approval by the digital underwriting engine, provided the requested loan amount does not exceed **1,000,000 rupees** (INR 1,000,000).

4.5.2 **Mandatory Human Review Rule:** Risk grades **C2, D1, and D2** are strictly ineligible for automated approval regardless of the loan size. Any application falling into Grade C2 or below must be routed to a human underwriter for manual evaluation.

---
*End of Section 4.0 - Ashva Capital Credit Policy Manual*
