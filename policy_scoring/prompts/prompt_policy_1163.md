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

Policy ID: policy/1163  
Policy Name: Washington Gas Energy Efficiency Standards  
Type: Standard  
Description:  
Establishes "efficiency performance requirements for natural gas distribution companies"

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/1007
Name: Small Product and Appliance Energy Efficiency Standards
Similarity: 0.6609
Score: 3
Type: Standard
Description: DEEP shall promulgate regulations for increased and additional appliance and product efficiency standards, pursuant to Section 16a-48 of the Connecticut General Statutes, to promote energy conservation and efficiency, provided that the subject appliances remain cost-effective for consumers who purchase and use them. New product categories or updates to existing product standards shall be selected based on the following criteria for each product category: A. there is an existing EPA ENERGY STAR standard or other state standard; B. there is an existing test procedure; C. there are multiple manufacturers producing at that standard; D. sufficient data for measurement and verification exists; and E. products manufactured to the standard are cost-effective for consumers

Explanation: Legal Language: The policy uses mandatory terms such as “shall promulgate regulations” and “shall be selected” (e.g., “DEEP shall promulgate regulations,” “new product categories or updates shall be selected”). These directives impose binding obligations on the state agency (DEEP) to act.
Source of Authority: Rooted in state law (Section 16a-48 of the Connecticut General Statutes), giving it statutory authority. The policy is not a voluntary guideline but a regulatory mandate.
Enforcement Mechanism: While penalties for non-compliance by manufacturers or retailers are not explicitly detailed here, the requirement for DEEP to promulgate regulations implies future enforcement tools (e.g., fines, product bans, certification requirements) will be established through those regulations.
Obligations: DEEP is legally obligated to develop and adopt efficiency standards meeting specified criteria (e.g., cost-effectiveness, alignment with ENERGY STAR). Manufacturers/retailers will be obligated to comply with the standards once regulations are finalized, though this policy focuses on the rulemaking process.
Optionality/Incentives: No voluntary language—compliance with the eventual standards will be mandatory for covered products. The criteria (e.g., “cost-effective for consumers”) guide rulemaking but do not make adoption optional.


Case 2:
Policy ID: policy/1186
Name: Minnesota Carbon Free Standards
Similarity: 0.5606
Score: 3
Type: Standard
Description: Carbon Free Standard: each electric utility must generate or procure sufficient electricity generated from a carbon-free energy technology to provide the electric utility's retail customers in Minnesota, or the retail customers of a distribution utility to which the electric utility provides wholesale electric service, so that the electric utility generates or procures an amount of electricity from carbon-free energy technologies that is equivalent to at least the following standard percentages of the electric utility's total retail electric sales to retail customers in Minnesota by the end of the year indicated: (1) 2030 80 percent for public utilities; 60 percent for other electric utilities (2) 2035 90 percent for all electric utilities (3) 2040 100 percent for all electric utilities.

Explanation: Legal Language: The policy uses unequivocally mandatory terms such as “must” (e.g., “each electric utility must generate or procure”) and specifies binding numerical targets (e.g., 80% by 2030) with statutory deadlines.
Source of Authority: Likely codified in state law or regulation (implied by the term “Standard” and the prescriptive structure), granting it legal enforceability.
Enforcement Mechanism: While explicit penalties are not detailed, the inclusion of compliance deadlines and thresholds suggests enforcement tools (e.g., fines, regulatory sanctions) are inherent to the legal framework governing utilities.
Obligations: All electric utilities in Minnesota are legally obligated to meet the carbon-free energy procurement/generation percentages by the deadlines. Compliance is non-discretionary, with stricter requirements for public utilities initially.
Optionality/Incentives: No voluntary language, exemptions, or incentives. Compliance is compulsory, with no opt-out mechanisms or rewards for participation.

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