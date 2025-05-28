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

Policy ID: policy/1558  
Policy Name: General Requirements for Transportation Planning and Investment  
Type: Governance  
Description:  
Requires Metropolitan Planning Organizations (MPOs) to evaluate and report the aggregate transportation GHG emissions impacts of Regional Transportation Plans (RTPs) and Transportation Improvement Plans (TIPs), and integrate GHG emission impacts as part of project prioritization and selection.Requires MassDOT to evaluate and report the transportation GHG emissions of State Transportation Improvement Programs (STIPs) and state-funded projects not included in STIPs. MassDOT must also calculate the net GHG transportation reductions achieved through implementation of the projects and programs included in RTPs, TIPs, STIPs, and state-funded projects not included in STIPs

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/718
Name: CA Resilience Lead by Example Goal
Similarity: 0.6154
Score: 3
Type: Targets/Goal
Description: The Department of General Services shall leverage its management and ownership of the state's 19 million square feet in managed buildings, 51,000 vehicles and other physical assets and goods to minimize state government's carbon footprint. To accomplish this, the Department of General Services shall: c. Reduce greenhouse gas emissions and mitigate climate risk from the state's owned and future-leased buildings, d. Manage energy demand to maximize benefits to the grid, and
Resilience Detail: mitigate climate risk from the state's owned and future-leased buildings

Explanation: Legal Language: The policy uses unequivocally mandatory terms such as “shall” (e.g., “The Department of General Services shall leverage,” “shall reduce”), creating binding legal obligations for the agency.
Source of Authority: Likely codified in state law or regulation (implied by the directive to a state department and prescriptive language), granting it statutory enforceability.
Enforcement Mechanism: While explicit penalties are not detailed, compliance is inherent to the state’s governance framework. Failure to meet obligations could trigger administrative accountability (e.g., reporting to the legislature, budget sanctions).
Obligations: The Department of General Services is legally required to:
Minimize the state government’s carbon footprint.
Reduce GHG emissions and climate risks in state-owned/leased buildings.
Manage energy demand to benefit the grid.
Optionality/Incentives: No voluntary language or incentives—compliance is compulsory.


Case 2:
Policy ID: policy/1983
Name: Regional Transit Innovation Grant
Similarity: 0.6103
Score: 2
Type: Program
Description: The FY24 state budget allocated MassDOT $15 million in discretionary operating and capital funding to award to transit providers through the RTIG. At least 25 percent of the funding ($3,750,000) is reserved for rural areas.Eligible applications include projects that aim to enhance and expand existing transit services; implement new and innovative transit services; expand service hours or weekend service; improve rural connectivity; improve connectivity across regional transit service areas; transit electrification; and/or operating and capital expenses.

Explanation: Legal Language: The policy uses facilitative terms like “allocated,” “award,” and “reserved,” which emphasize voluntary participation. There is no mandatory language (e.g., “shall,” “must”) requiring transit providers to apply for or implement projects.
Source of Authority: Established through the state budget (FY24 allocation) and administered by MassDOT. It functions as a grant program, not a regulatory mandate.
Enforcement Mechanism: No penalties or compliance requirements for transit providers. Enforcement is limited to program administration (e.g., ensuring 25% of funds are reserved for rural areas, verifying eligibility criteria).
Obligations: Transit providers are not legally obligated to apply for grants or undertake projects. Participation is entirely optional. MassDOT must administer the funds according to budget directives but has no authority to compel action from external entities.
Optionality/Incentives: Grants act as financial incentives for transit providers to enhance services (e.g., electrification, expanded hours). Participation is voluntary—transit providers choose whether to submit eligible projects.

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