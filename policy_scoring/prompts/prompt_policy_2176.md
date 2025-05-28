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

Policy ID: policy/2176  
Policy Name: Delaware Social Vulnerability Index  
Type: Analysis and Tools  
Description:  
Delaware’s My Healthy Communities uses the Social Vulnerability Index (SVI) developed by the US Centers for Disease Control and Prevention to help identify traditionally under-served and under-represented populations on topics such as air and water quality, health status, healthy lifestyles and community safetyThe SVI’s objective is to allow key stakeholders to design more beneficial and efficient response strategies and predict the level of support and resources needed in an area following a disastrous event. It allows for improved response preparation, funding allocation, and resource distribution proportionally across communities by their vulnerability.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/2174
Name: Vermont Social Vulnerability Index
Similarity: 0.6818
Score: 1
Type: Analysis and Tools
Description: The Vermont Social Vulnerability Index shows the number of vulnerability measures above the 90th percentile for Vermont census tracts. For each of the vulnerability measures, census tracts in the 90th percentile of vulnerability were assigned a flag. This SVI exhibits the sum of all flags for each census tract. There are a total of 16 measures in the SVI.

Explanation: Legal Language: The policy uses descriptive terms ("shows," "assigned a flag") to present data without imposing obligations or directives (e.g., "must," "shall"). It functions as an analytical tool, not a regulatory requirement.
Source of Authority: Likely developed by a state agency as an informational resource, not codified in law or regulation.
Enforcement Mechanism: No penalties, compliance requirements, or oversight mechanisms. The index is purely a data visualization tool.
Obligations: No legal obligations are imposed on users (e.g., agencies, communities) to act based on the index. Its purpose is to inform, not compel.
Optionality/Incentives: No incentives or penalties tied to the index. Use of the data is entirely voluntary.


Case 2:
Policy ID: policy/1580
Name: Green and Healthy Task Force
Similarity: 0.5069
Score: 3
Type: Governance
Description: BEGINNING JULY 1, 2023, MEET QUARTERLY FOR A PERIOD OF 3 YEARS; ADVANCE THE ALIGNMENT, BRANDING, AND COORDINATION OF RESOURCES TO MORE EFFECTIVELY DELIVER GREEN AND HEALTHY HOUSING FOR LOW–INCOME HOUSEHOLDS IN THE STATE; EXAMINE THE PUBLIC AND PRIVATE RESOURCES NEEDED TO ADDRESS THE HOUSING NEEDS OF LOW–INCOME COMMUNITIES; DEVELOP POLICY AND STATUTORY RECOMMENDATIONS TO ELIMINATE BARRIERS TO LOW–INCOME HOUSEHOLDS ACHIEVING HEALTHY, ENERGY–EFFICIENT, AND AFFORDABLE, AND LOW–EMISSIONS HOUSING; AND ENGAGE WITH INTERESTED PARTIES AND COLLABORATE WITH OTHER ENTITIES THAT CAN HELP ADVANCE THE GOALS OF THE TASK FORCE, INCLUDING EXPERTS IN THE FIELD OF HEALTHY AND, ENERGY–EFFICIENT, AND LOW–EMISSIONS HOUSING. ON OR BEFORE JULY 1, 2024, AND EACH JULY 1 THROUGH 2027, THE TASK FORCE SHALL REPORT ITS FINDINGS AND RECOMMENDATIONS TO THE SECRETARY OF HEALTH, THE SECRETARY OF THE ENVIRONMENT, THE COMMISSION, THE GOVERNOR, AND, IN ACCORDANCE WITH § 2–1257 OF THE STATE GOVERNMENT ARTICLE, THE GENERAL ASSEMBLY.

Explanation: Legal Language: The policy uses mandatory terms such as “shall” (e.g., “the Task Force shall report its findings”) and specifies deadlines (e.g., “on or before July 1, 2024”). These terms impose clear obligations.
Source of Authority: The task force is tied to statutory law (§ 2–1257 of the State Government Article), indicating it was established through legislative authority, which carries legal weight.
Enforcement Mechanism: While penalties are not explicitly stated, the statutory foundation implies accountability mechanisms (e.g., governmental oversight) for meeting reporting deadlines and operational requirements (e.g., quarterly meetings).
Obligations: The task force is legally obligated to meet quarterly, develop recommendations, and submit annual reports to state officials and the legislature. Participation in the task force itself is likely mandatory for appointed members.
Optionality/Incentives: No voluntary opt-outs or incentives are mentioned. The policy creates binding procedural requirements for the task force, even though its recommendations may later require separate adoption to become enforceable.

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