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

Policy ID: policy/319  
Policy Name: Michigan Advisory Council on Environmental Justice (MAC-EJ)  
Type: Governance  
Description:  
The state’s first Environmental Justice advisory council. The MAC-EJ members represent an intentional combination of frontline activists, advocacy organizations, academia, tribal representation, local governments, business and industry, public health, and labor. The MAC-EJ is an advisory body for Environmental Justice actions spearheaded by the Interagency Environmental Justice Response Team and the Office of Environmental Justice Public Advocate.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/697
Name: Environmental Justice Advisory Board
Similarity: 0.7182
Score: 1
Type: Governance
Description: The Environmental Justice Advisory Board is a volunteer board. The Governor and Executive Director of CDPHE appoint its 12 members.
The Board serves Colorado by:
Coordinating with the Environmental Justice Ombudsperson.
Advising CDPHE on best practices for engaging disproportionately impacted communities.
Responding to environmental justice policy matters referred by the Governor’s Office or CDPHE.
Creating and overseeing an environmental justice grants program.

Explanation: Legal Language: The policy uses non-mandatory terms such as “serves,” “coordinating,” “advising,” and “responding,” which denote advisory or facilitative roles. The board’s activities are described as voluntary, with no binding directives (e.g., “shall” or “must”).
Source of Authority: Established through executive appointment (Governor and CDPHE) but structured as a volunteer board. It lacks statutory or regulatory authority, operating as an advisory body rather than a legally mandated entity.
Enforcement Mechanism: No penalties, compliance deadlines, or enforcement tools are mentioned. The board’s recommendations and grants program are discretionary.
Obligations: Board members participate voluntarily, and there is no legal obligation for CDPHE, the Governor, or other entities to act on the board’s advice.
Optionality/Incentives: Participation in the board and adherence to its guidance are entirely optional. The grants program may incentivize community projects, but the board itself has no binding authority.


Case 2:
Policy ID: policy/1208
Name: Justice Forty Oversight Committee
Similarity: 0.7007
Score: 1
Type: Governance
Description: Justice Forty Oversight Committee to study and make findings and recommendations regarding environmental justice in this State. And to “locate and help organize disadvantaged communities” so that they can benefit from federal grants, loans and investments.

Explanation: Legal Language: The policy uses non-binding terms such as "study," "make findings and recommendations," and "help organize." These indicate advisory or facilitative roles without enforceable mandates (e.g., no "shall" or "must").
Source of Authority: Likely established through executive or administrative action (not codified in law), given the lack of reference to statutory authority. The committee’s role is advisory, not regulatory.
Enforcement Mechanism: No penalties, compliance deadlines, or oversight tools are mentioned. The committee cannot compel action or enforce its recommendations.
Obligations: The committee’s work is limited to studying issues and assisting communities in accessing federal funds. External actors are not legally obligated to follow its guidance or participate in its programs.
Optionality/Incentives: Participation by communities is voluntary. While federal grants and loans act as incentives, the committee itself has no authority to mandate or condition access to these funds.

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