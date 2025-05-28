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

Policy ID: policy/1683  
Policy Name: Oregon Clean Vehicle Rebate Program  
Type: Program  
Description:  
The Oregon Clean Vehicle Rebate Program (OCVRP) offers rebates for Oregon drivers who purchase or lease electric vehicles. It is not a tax credit. DEQ designed the Program to reduce vehicle emissions by encouraging the purchase or lease of electric vehicles instead of gas vehicles.Standard Rebate$2,500 off a new eligible vehicle with a battery capacity of 10 kWh or more$1,500 off a new eligible vehicle with a battery capacity of less than 10 kWh$750 off an eligible new zero-emission motorcycleCharge Ahead Rebate$5,000 off a new or used eligible vehicle.EQUITY DETAILThe Charge Ahead Rebate provides low- to moderate-income households and low-income service providers a $5,000 rebate toward the purchase or lease of eligible new or used zero-emission vehicles.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/1095
Name: ZE and Plug-in Hybrid Light-Duty Fleet Purchase Goal
Similarity: 0.4773
Score: 2
Type: Targets/Goal
Description: Enacted legislation to require, where practicable, 50 percent of state light-duty fleet purchases be zero-emissions and plug-in hybrid vehicles by 2025 and 100 percent by 2030, 100 percent of county and municipal government light-duty fleet purchases be zero-emissions and plug-in hybrid vehicles by 2030, and 75 percent of school bus fleet purchases be zero-emissions buses by 2035. Achieve 100% zero-emission fleets by 2040.

Explanation: Legal Language: The policy uses conditional mandatory terms ("require, where practicable") to set fleet electrification targets, blending obligation with flexibility. It lacks absolute directives (e.g., "shall achieve unconditionally").
Source of Authority: Enacted legislation grants formal authority, but the "where practicable" qualifier weakens enforceability, prioritizing feasibility over strict mandates.
Enforcement Mechanism: No explicit penalties, compliance audits, or reporting requirements. Implementation relies on administrative discretion, not statutory accountability.
Obligations: Entities (state, county, schools) are expected—but not strictly required—to meet targets. Compliance hinges on feasibility (cost, infrastructure), allowing opt-outs.
Optionality/Incentives: No financial incentives or penalties. Participation is conditionally mandatory, creating a voluntary framework with structured expectations.


Case 2:
Policy ID: policy/1082
Name: Multi-Unit Dwelling (MUD) Electric Vehicle (EV) Charging Station Deployment Working Group
Similarity: 0.4475
Score: 3
Type: Governance
Description: Multi-Unit Dwelling (MUD) Electric Vehicle (EV) Charging Station Deployment Assessment The Hawaii State Energy Office must convene a working group to evaluate opportunities and barriers for installing EV charging stations in MUDs. The working group must:
Assess barriers to EV charging stations at MUDs;
Consider changes to state statutes and administrative code to support EV charging station deployment at MUDs;
Identify best practices for EV charging station installations at MUDs;
Create guidelines for EV charging stations in MUDs;
Develop solutions for EV charging cost recovery and electrical capacity management; and,
Develop recommendations for installing shared-use EV charging stations at MUDs.
The working group must prepare a report of its findings, recommendations, and proposed legislation and submit it to the Hawaii Legislature 20 days prior to the 2023 legislative session.

Explanation: Legal Language: The policy uses mandatory terms such as “must” (e.g., “The Hawaii State Energy Office must convene,” “the working group must prepare a report”), creating binding obligations for action.
Source of Authority: Likely statutory or regulatory, as it directs a state agency (Hawaii State Energy Office) to convene the working group and imposes formal reporting requirements to the legislature.
Enforcement Mechanism: While penalties are not explicitly stated, the requirement to submit a report to the legislature by a specific deadline implies accountability mechanisms (e.g., legislative oversight, potential follow-up mandates).
Obligations: The Hawaii State Energy Office is legally obligated to convene the working group, and the working group is required to complete defined tasks (e.g., assessing barriers, drafting guidelines) and submit legislative recommendations.
Optionality/Incentives: No voluntary language or incentives—compliance is compulsory. The working group’s activities and reporting are mandatory, not discretionary.

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