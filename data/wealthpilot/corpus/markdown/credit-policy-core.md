# Ashva Capital Credit Policy Manual: Core Underwriting Standards

# ASHVA CAPITAL — INTERNAL CREDIT POLICY MANUAL
**Document Reference:** CP-SME-2026-V4  
**Applies To:** All SME Term Loan Underwriting and Automated Decision Engines  
**Effective Date:** 1 January 2026  

---

## SECTION 1: PURPOSE AND SCOPE

1.1 This manual establishes the binding credit standards, decision paths, and approval authorities for all Small and Medium Enterprise (SME) term loan applications processed by Ashva Capital. Underwriters and automated underwriting systems are strictly bound by these provisions and may not exercise discretion outside the parameters defined herein.

1.2 The Lending Base Rate of Ashva Capital is fixed at 9.50 percent per annum for all calculations requiring a baseline rate, distinct from the assessment rates applied under Section 2.

---

## SECTION 2: CORE FINANCIAL ELIGIBILITY STANDARDS

2.1 **Operating History:** The applicant business must demonstrate a minimum continuous operating history of 24 months prior to the date of application, verified via statutory filings or bank statement analysis.

2.2 **Debt-Service Coverage Ratio (DSCR):**
2.2.1 DSCR is defined as EBITDA divided by Total Annual Debt Service.
2.2.2 Total Annual Debt Service is calculated as the sum of existing annual debt service plus the first twelve monthly instalments on the proposed loan, computed on a reducing balance at the assessment rate of 14.00 percent per annum.
2.2.3 The minimum allowable DSCR is 1.25x, or the applicable sector floor where that sector floor is higher than 1.25x.

2.3 **Worked DSCR Calculation:**
Underwriters shall apply the following standardized formula and numerical structure for all baseline verifications:
* EBITDA: 2,400,000 rupees
* Existing annual debt service: 600,000 rupees
* Proposed loan: 2,000,000 rupees over a 48-month tenor, where the first twelve monthly instalments at the 14.00 percent assessment rate total 655,835 rupees.
* Total Annual Debt Service = 600,000 + 655,835 = 1,255,835 rupees.
* $\text{DSCR} = \frac{2,400,000}{1,255,835} = 1.91\text{x}$.

2.4 **Leverage Limit:** Maximum allowable leverage—defined as existing total debt plus the proposed loan—may not exceed 6.0 times EBITDA.

2.5 **Current-Ratio Floor:** The applicant must maintain a minimum current ratio of 1.10. Any application reflecting a current ratio below 1.10 fails this standard.

---

## SECTION 3: BUREAU SCORING AND RISK GRADES

3.1 **Bureau Score Thresholds by Grade:** Applicant risk grades shall be mapped strictly against verified bureau scores as follows:
* Grade A1: Minimum bureau score of 750
* Grade A2: Minimum bureau score of 700
* Grade B1: Minimum bureau score of 650
* Grade B2: Minimum bureau score of 600
* Grade C1: Minimum bureau score of 550
* Grade C2: Minimum bureau score of 500
* Grade D1: Minimum bureau score of 450
* Grade D2: Bureau score below 450 (Adverse Bureau Record)

3.2 **Adverse Bureau Records and Past Delinquencies:**
3.2.1 A bureau score below 450 constitutes an adverse bureau record.
3.2.2 A past delinquency is defined as any historical 90-day delinquency, or any written-off amount equal to or exceeding 500,000 rupees.

---

## SECTION 4: APPLICATION DISPOSITION PATHS

4.1 **Declined Applications:** An application shall be declined automatically by the system or manually by an underwriter if any of the following conditions are met:
* DSCR is below 1.00;
* The bureau record is adverse (score below 450);
* The business has operated for less than 24 months; or
* The assigned risk grade is D2.

4.2 **Borderline Applications:** An application is classified as borderline and must be routed to a human reviewer if any of the following conditions occur (and the application is not subject to mandatory declination under Clause 4.1):
* Any standard other than those in Clause 4.1 is missed;
* There is a recorded past delinquency;
* The requested tenor exceeds the maximum permitted by the risk grade or sector rules;
* The collateral is valued at less than the cover required by the risk grade;
* A numerical figure required to test a core standard is missing; or
* The assigned risk grade is C2 or D1.

4.3 **Approvable Applications:** If an application meets all core financial, bureau, and collateral standards without triggering Clauses 4.1 or 4.2, it is classified as approvable.

---

## SECTION 5: APPROVAL AUTHORITIES AND SIGN-OFF MANDATES

5.1 **Approval Authority by Loan Size:** Final sanctioning authority is strictly demarcated by the total principal amount of the loan:
* **Loans up to 1,000,000 rupees:** Credit Officer
* **Loans up to 5,000,000 rupees:** Credit Committee
* **Loans exceeding 5,000,000 rupees:** Board Credit Committee

5.2 **Named Signatory Requirement:** No loan exceeding 5,000,000 rupees may be approved without the explicit sign-off of a named human signatory holding a designated mandate on the Board Credit Committee.

5.3 **Automated Approval Restrictions:**
5.3.1 The automated underwriting system may approve an application without human intervention *only if* all of the following cumulative criteria are met:
1. The application is classified as approvable under Clause 4.3;
2. The loan amount is no more than 1,000,000 rupees; and
3. The assigned risk grade is C1 or better (C1, B2, B1, A2, or A1).
5.3.2 Everything else—including any borderline application, any declined application, any loan exceeding 1,000,000 rupees, or any grade of C2, D1, or D2—requires mandatory human sign-off by the appropriate authority defined in Clause 5.1.
