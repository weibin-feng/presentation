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

Policy ID: policy/1519  
Policy Name: Transformational Affordable Housing Revolving Loan Fund Program  
Type: Program  
Description:  
The loan program will provide flexible, low-interest, and below-market rate loan funding to assist eligible recipients in completing the eligible loan projects identified in the bill. The program can include financing for energy improvements in affordable housing, which will fund incremental up-front costs for efficient, electric measures, and renewable energy systems for both existing buildings and new housing construction.EQUITY DETAILFocus on affordable housing

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/200
Name: Illinois Finance Authority Climate Bank
Similarity: 0.5984
Score: 2
Type: Program
Description: The bill designates the Illinois Finance Authority, established in the Illinois Finance Authority Act, as a "Climate Bank" to leverage public-private partnerships to fund clean energy projects across the state. In its role as the Climate Bank of the State, the Authority shall have the power to: (i) administer programs and funds appropriated by the General Assembly for clean energy projects in eligible communities and environmental justice communities or owned by eligible persons, (ii) support investment in the clean energy and clean water, drinking water, and wastewater treatment, (iii) support and otherwise promote investment in clean energy projects to foster the growth, development, and commercialization of clean energy projects and related enterprises, and (iv) stimulate demand for clean energy and the development of clean energy projects

Explanation: Legal Language: The policy uses a mix of mandatory and non-binding terms. While the Illinois Finance Authority “shall have the power” to administer programs and support clean energy projects, the language focuses on enabling functions (e.g., “support,” “promote”) rather than imposing obligations on external actors.
Source of Authority: Established by statute (bill under the Illinois Finance Authority Act), granting the Climate Bank legal authority to operate. However, the program itself functions as a funding and partnership mechanism, not a regulatory mandate.
Enforcement Mechanism: No penalties or compliance requirements are specified. The Climate Bank’s role is to facilitate funding and partnerships, with participation by private entities or communities being voluntary.
Obligations: The Authority is legally obligated to administer programs and funds, but external actors (e.g., businesses, communities) are not required to participate. Compliance is optional for project applicants or partners.
Optionality/Incentives: Participation in Climate Bank programs is voluntary and incentivized through funding opportunities.


Case 2:
Policy ID: policy/1999
Name: California Clean Energy Planning Program
Similarity: 0.5344
Score: 2
Type: Program
Description: This solicitation has two purposes: 1) make $1,050,000 available to California Native American tribes for clean energy future planning as well as to better enable their participation in statewide clean energy and energy infrastructure planning activities and 2) make $500,000 available to local government entities to develop new or updated land use planning documents that support and advance the development of clean energy in their jurisdiction.

Explanation: Legal Language: The policy uses facilitative terms like “available” and “develop” without mandatory directives (e.g., “shall” or “must”). Participation is framed as optional, not compulsory.
Source of Authority: Likely established through administrative funding (state budget or agency allocation), not statutory law. It functions as a grant program, not a regulatory mandate.
Enforcement Mechanism: No penalties or compliance requirements for tribes or local governments. Enforcement applies only to grant administration (e.g., ensuring funds are used as stipulated).
Obligations: Participation is voluntary—tribes and local governments are not legally required to apply for funding or undertake planning activities.
Optionality/Incentives: Grants act as financial incentives to encourage clean energy planning, but adoption remains discretionary.

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