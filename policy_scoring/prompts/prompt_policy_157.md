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

Policy ID: policy/157  
Policy Name: Delaware Clean Transportation Incentive Program  
Type: Program  
Description:  
As part of the Delaware Clean Transportation Incentive Program, the Delaware Department of Natural Resources and Environmental Control (DNREC) offers rebates for new or leased AFVs.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/200
Name: Illinois Finance Authority Climate Bank
Similarity: 0.4572
Score: 2
Type: Program
Description: The bill designates the Illinois Finance Authority, established in the Illinois Finance Authority Act, as a "Climate Bank" to leverage public-private partnerships to fund clean energy projects across the state. In its role as the Climate Bank of the State, the Authority shall have the power to: (i) administer programs and funds appropriated by the General Assembly for clean energy projects in eligible communities and environmental justice communities or owned by eligible persons, (ii) support investment in the clean energy and clean water, drinking water, and wastewater treatment, (iii) support and otherwise promote investment in clean energy projects to foster the growth, development, and commercialization of clean energy projects and related enterprises, and (iv) stimulate demand for clean energy and the development of clean energy projects

Explanation: Legal Language: The policy uses a mix of mandatory and non-binding terms. While the Illinois Finance Authority “shall have the power” to administer programs and support clean energy projects, the language focuses on enabling functions (e.g., “support,” “promote”) rather than imposing obligations on external actors.
Source of Authority: Established by statute (bill under the Illinois Finance Authority Act), granting the Climate Bank legal authority to operate. However, the program itself functions as a funding and partnership mechanism, not a regulatory mandate.
Enforcement Mechanism: No penalties or compliance requirements are specified. The Climate Bank’s role is to facilitate funding and partnerships, with participation by private entities or communities being voluntary.
Obligations: The Authority is legally obligated to administer programs and funds, but external actors (e.g., businesses, communities) are not required to participate. Compliance is optional for project applicants or partners.
Optionality/Incentives: Participation in Climate Bank programs is voluntary and incentivized through funding opportunities.


Case 2:
Policy ID: policy/1844
Name: Landfill methane emissions reduction grants
Similarity: 0.4057
Score: 2
Type: Program
Description: In 2023, the State Legislature appropriated $9.6M from Climate Commitment Act funds to help municipal solid waste (MSW) landfill owners comply with standards in a new Landfills-Methane Emissions law (Chapter 70A.540 RCW). Ecology is distributing these funds through a new grant program to help landfill owners and operators pay for expenses associated with complying with the law. Costs could include design, planning, installing or upgrading gas collection and control systems, increasing surface emissions monitoring, as well as other requirements.

Explanation: Legal Language: The policy description emphasizes assistance ("help," "pay for expenses") and does not use mandatory terms like "must" or "shall" for grant participation. Compliance obligations stem from the underlying law (Chapter 70A.540 RCW), not the grant itself.
Source of Authority: The grant program is a funding mechanism under the Climate Commitment Act, administered by the state Ecology department. The binding requirements originate from the statutory law (RCW), not the grant.
Enforcement Mechanism: The grants lack enforcement mechanisms (e.g., penalties), as they are financial incentives to support compliance with the separate legal mandate. Enforcement of landfill standards would occur under the law, not the grant program.
Obligations: Landfill owners are legally obligated to comply with the Landfills-Methane Emissions law, but participation in the grant program is voluntary. The policy does not create new obligations.
Optionality/Incentives: Grants are explicitly incentivized and optional—funding is provided to offset compliance costs, but landfill owners may choose whether to apply. Compliance with the law itself, however, remains mandatory.

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