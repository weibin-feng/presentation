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

Policy ID: policy/37  
Policy Name: Transformative Climate Communities (TCC) Program  
Type: Program  
Description:  
The Transformative Climate Communities (TCC) Program empowers the communities most impacted by pollution to choose their own goals, strategies, and projects to reduce greenhouse gas emissions and local air pollution.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/1369
Name: Colorado Climate Corps
Similarity: 0.6325
Score: 2
Type: Program
Description: Colorado Climate Corps is a multi-pronged strategy to address climate change and advance the Governor’s bold goal of moving Colorado’s electric grid to 100% renewable sources by 2040 and protecting the environment for future generations, by any of the following:
Providing critical capacity and support to local governments, especially county commissions, to develop and execute climate action plans and/or projects;
Building upon and expanding existing conservation and youth corps to do hands-on projects, including wildfire and flood mitigation;
Implementing additional environment and energy projects with nonprofits, higher education, Tribes, and local or state government that accelerate the adoption of clean, renewable resources and energy efficiency, advancing electrification efforts in our transportation sector, mitigate against droughts, floods, and wildfires, and ensuring the conservation of our public lands and wildlife.
Colorado Climate Corps is a collaboration with the Colorado Interagency Climate Team.

Explanation: Legal Language: The policy uses facilitative terms like “providing,” “building upon,” and “implementing” but lacks mandatory directives (e.g., “must,” “shall”). Participation by local governments, nonprofits, or other entities is framed as optional support rather than a legal requirement.
Source of Authority: Likely established via executive initiative or interagency collaboration (Colorado Interagency Climate Team), not statutory law. The Governor’s renewable energy goal is aspirational, not codified as a binding mandate for the Corps itself.
Enforcement Mechanism: No penalties or compliance deadlines. The program focuses on capacity-building and project implementation through partnerships, with no enforcement tools for non-participation.
Obligations: Target actors (local governments, nonprofits, etc.) are not legally obligated to engage with the Climate Corps. The program offers assistance but does not impose requirements.
Optionality/Incentives: Participation is voluntary and incentivized through support for climate projects (e.g., funding, technical assistance).


Case 2:
Policy ID: policy/1893
Name: Make it in Michigan Competitiveness Fund Climate Justice Challenge
Similarity: 0.5353
Score: 2
Type: Program
Description: In November 2023, the EPA released the Environmental and Climate Justice Community Change Grants program, allocating $2 billion to benefit disadvantaged communities through projects to reduce pollution, increase community climate resilience, and build community response capacity. The program design integrated nationwide community and stakeholder input, and the resulting grants will focus on community-driven and place-based initiatives to advance environmental justice and climate equity.
The State of Michigan announced in May 2024 that through the Make it in Michigan Competitiveness Fund it will provide five percent (5%) match funding of the total awarded amount for eligible Community Change Grant applications awarded by the EPA to fund projects benefiting disadvantaged community(ies) in Michigan, provided that the application for the Community Change Grant is fully submitted to the EPA prior to August 1, 2024.

Explanation: Legal Language: The policy uses conditional terms like “provided that” for eligibility but lacks mandatory language (e.g., “shall” or “required”). Participation hinges on voluntary action (submitting an application by the deadline).
Source of Authority: The program stems from state funding (Michigan Competitiveness Fund) and complements the EPA’s federal grant program. It operates as a financial incentive mechanism, not a standalone law or regulation.
Enforcement Mechanism: No penalties are specified. The August 1, 2024, deadline acts as an eligibility criterion for receiving the match funding, but non-participation does not incur consequences.
Obligations: Applicants for EPA grants are not legally obligated to seek or accept Michigan’s 5% match. Participation is optional, targeting those who want supplemental state funding.
Optionality/Incentives: The 5% match is purely incentivized—projects can proceed with EPA grants alone. The policy encourages timely applications but does not mandate action.

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