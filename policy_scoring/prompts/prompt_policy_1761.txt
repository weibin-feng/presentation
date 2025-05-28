You are an expert legal-policy analyst evaluating the **bindingness** of climate or environmental policies. Your task is to assess how legally enforceable and compulsory a given policy is. You must follow a structured, multi-step reasoning approach before assigning a final score.

---

Objective:
Classify the policy into one of three **bindingness scores**, based on your direct evaluation, dimension-by-dimension reasoning, and reference to comparable cases.


---

### Scoring Categories:

- **Score 1: Non-binding**
  - Aspirational or informational policies with no legal force, obligations, or incentives.
  - Often appear as reports, plans, advisory boards, or descriptive indexes.
  - **Common keywords**: may, encourage, develop, planning goals

- **Score 2: Voluntary or Incentivized**
  - Policies that are **not mandatory**, but include **explicit mechanisms to promote participation**, such as grants, match funding, or conditional eligibility.
  - These policies **encourage action** through incentives or optional compliance paths, even if not legally required.
  - Distinct from Score 1: Score 2 policies are **meant to drive change** through material or procedural benefits, **not just provide information**.
  - **Common cues**: offer, grant program, funding available, match funds, eligibility requirement, conditional compliance (e.g., "where practicable")

- **Score 3: Mandatory**
  - Legally binding measures from statute, regulation, or executive order with enforceable obligations.
  - May include penalties, reporting deadlines, or regulatory consequences.
  - **Common keywords**: must, shall, is required to, mandate, penalty, enforce

> Note: Use judgment based on overall context, not just keywords.
---

### Evaluation Dimensions (Used for Explanation):

For each of the five dimensions, answer both components:

1. **Legal_Language**  
   - Does the policy use binding terms like **"shall," "must," "is required to"**?  
   - Or does it use non-binding terms like **"may," "encourage," "help," "support," "goal"**?

2. **Source_of_Authority**  
   - Is it based on **statute, regulation, executive order** (binding)?  
   - Or is it a **plan, agency report, funding mechanism, task force, or advisory program** (non-binding)?

3. **Enforcement_Mechanism**  
   - Are there **penalties, reporting requirements, or compliance deadlines**?  
   - Or is it **aspirational** with **no consequence** for failure to comply?

4. **Obligations**  
   - Who is obligated to act?  
   - Are responsibilities assigned and legally enforceable, or **left to discretion**?

5. **Optionality_or_Incentives**  
   - Does the policy offer **grants, rebates, tax credits**, or **non-compulsory incentives** to encourage action?


### Step-by-step Procedure:

1. **Analyze the Current Policy**
   - Examine each of the five dimensions.
   - Describe what is directly observed in the policy language and structure.

2. **Retrieve and Compare Similar Cases**
   - Review the two retrieved cases below.
   - Compare their language, structure, and bindingness to the current policy.

3. **Synthesize and Resolve**
   - Discuss agreement or divergence between direct analysis and retrieved cases.
   - Highlight any ambiguous elements or borderline scores.

4. **Assign Final Score and Confidence**
   - Score: - You should assign the final score based primarily on your direct analysis. Retrieved cases serve as contextual benchmarks.
   - Confidence (0–10): High = strong signals; Medium = partial alignment; Low = ambiguous.

---

### Current Policy for Evaluation:

Policy ID: policy/1761  
Policy Name: State of Vermont Incentive Program for eBikes  
Type: Program  
Description:  
The State of Vermont is offering a limited-time incentive program to consumers for the purchase of eligible electric bicycles to reduce vehicle miles traveled in personal automobiles and their associated greenhouse gas emissions. This Program was reauthorized with $150,000 through the 2023 Budget Adjustment Act and FY2024 Transportation Bill.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/1095
Name: ZE and Plug-in Hybrid Light-Duty Fleet Purchase Goal
Similarity: 0.5469
Score: 2
Type: Targets/Goal
Description: Enacted legislation to require, where practicable, 50 percent of state light-duty fleet purchases be zero-emissions and plug-in hybrid vehicles by 2025 and 100 percent by 2030, 100 percent of county and municipal government light-duty fleet purchases be zero-emissions and plug-in hybrid vehicles by 2030, and 75 percent of school bus fleet purchases be zero-emissions buses by 2035. Achieve 100% zero-emission fleets by 2040.

Explanation: Legal Language: The policy uses conditional mandatory terms ("require, where practicable") to set fleet electrification targets, blending obligation with flexibility. It lacks absolute directives (e.g., "shall achieve unconditionally").
Source of Authority: Enacted legislation grants formal authority, but the "where practicable" qualifier weakens enforceability, prioritizing feasibility over strict mandates.
Enforcement Mechanism: No explicit penalties, compliance audits, or reporting requirements. Implementation relies on administrative discretion, not statutory accountability.
Obligations: Entities (state, county, schools) are expected—but not strictly required—to meet targets. Compliance hinges on feasibility (cost, infrastructure), allowing opt-outs.
Optionality/Incentives: No financial incentives or penalties. Participation is conditionally mandatory, creating a voluntary framework with structured expectations.


Case 2:
Policy ID: policy/631
Name: 2040 Zero-Carbon Target
Similarity: 0.4754
Score: 3
Type: Targets/Goal
Description: Public Act 22-5 (Senate Bill 10), An Act Concerning Climate Change Mitigation: This bill, which was sponsored by Governor Lamont, codifies into law the 2040 zero-carbon electric grid goal that Governor Lamont established through an executive order that he issued in 2019 (Executive Order No. 3).
The state shall reduce the level of emissions of greenhouse gas: (1) Not later than January 1, 2020, to a level at least ten per cent below the level emitted in 1990; (2) Not later than January 1, 2030, to a level at least forty-five percent below the level emitted in 2001; [and] (3) Not later than January 1, 2040, to a level of zero per cent from electricity supplied to electric customers in the state; (4) Not later than January 1, 2050, to a level at least eighty percent below the level emitted in 2001; [.] and (5) All of the levels referenced in this subsection shall be determined by the Commissioner of Energy and Environmental Protection.

Explanation: Legal Language: The policy uses mandatory terms such as “shall” (e.g., “the state shall reduce”) and specifies binding deadlines (e.g., 2040 for zero-carbon electricity) with quantified emissions targets.
Source of Authority: Codified into law via Public Act 22-5 (statute), granting it legal enforceability. This elevates it from the original executive order to a statutory mandate.
Enforcement Mechanism: While explicit penalties are not detailed, the Commissioner of Energy and Environmental Protection is legally tasked with determining compliance levels, implying regulatory oversight and potential enforcement tools (e.g., future regulations or reporting requirements).
Obligations: The state is legally obligated to meet the emissions reduction targets, though the law does not specify obligations for individual entities (e.g., utilities, industries). Compliance likely depends on subsequent regulations or sector-specific policies.
Optionality/Incentives: No voluntary opt-outs, exemptions, or incentives. The targets are compulsory for the state as a whole, with no flexibility in deadlines or thresholds.

---


            
### Final Output Format (JSON Only):

{
  "Score": <1 | 2 | 3>, 
  "Confidence": <0–10>, 
  "Explanation": {
    "Legal_Language": "Explain what kind of language the current policy uses (e.g., 'shall', 'may', 'encourage').",
    "Source_of_Authority": "Explain whether this policy stems from law, regulation, or advisory source.",
    "Enforcement_Mechanism": "Explain if there are penalties, deadlines, or if it is purely aspirational.",
    "Obligations": "Explain who is required to act, and whether responsibilities are enforceable.",
    "Optionality_or_Incentives": "Explain whether the policy provides incentives or is fully mandatory."
  },
  "Inference_Chain": [
    "Step 1: Direct analysis of the current policy shows <binding/non-binding> terms ('<term>') and <source of authority>.",
    "Step 2: Retrieved <CASE_A_Name> (sim=<CASE_A_Similarity>, Score <CASE_A_Score>) has similar features.",
    "Step 3: Retrieved <CASE_B_Name> (sim=<CASE_B_Similarity>, Score <CASE_B_Score>) shares some elements but lacks <feature>.",
    "Step 4: Current policy aligns more with <CASE_A_Name> due to <reason>.",
    "Step 5: Direct analysis has priority; retrieved cases provide additional support weighted by their similarity scores.",
    "Step 6: Final judgment: Score <Final_Score>, Confidence <Confidence_Score>."
  ],
  "Comparable_Cases": [
    {
      "Policy_ID": "<CASE_1_ID>",
      "Case_Name": "<CASE_1_NAME>",
      "Similarity": <CASE_1_SIMILARITY>,
      "Score": <SCORE_1>,
      "Reason": "Summarize why this case is highly similar and informative for the current policy evaluation."
    },
    {
      "Policy_ID": "<CASE_2_ID>",
      "Case_Name": "<CASE_2_NAME>",
      "Similarity": <CASE_2_SIMILARITY>,
      "Score": <SCORE_2>,
      "Reason": "Summarize why this case is also relevant and comparable to the current policy."
    }
  ]
}

Note: The above is a structural JSON template.

You must:
- Replace <...> placeholders with actual values from your analysis.
- Derive both cases from the two retrieved examples.
- These should be the top 2 most semantically similar reference policies.
- Do not copy this template literally.

---

Please evaluate the bindingness of the current policy following the structured approach above.