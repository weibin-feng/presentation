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

Policy ID: policy/1971  
Policy Name: Clean Transit Enterprise  
Type: Program  
Description:  
This enterprise is created within the Colorado Department of Transportation to support public transit electrification planning efforts, facility upgrades, fleet motor vehicle replacement, as well as construction and development of electric motor vehicle charging and fueling infrastructure. The bill allows the enterprise to impose a clean transit retail delivery fee to fund its operations, and to issue grants, loans or rebates to support electrification of public transit.

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.




Case 1:
Policy ID: policy/1983
Name: Regional Transit Innovation Grant
Similarity: 0.5710
Score: 2
Type: Program
Description: The FY24 state budget allocated MassDOT $15 million in discretionary operating and capital funding to award to transit providers through the RTIG. At least 25 percent of the funding ($3,750,000) is reserved for rural areas.Eligible applications include projects that aim to enhance and expand existing transit services; implement new and innovative transit services; expand service hours or weekend service; improve rural connectivity; improve connectivity across regional transit service areas; transit electrification; and/or operating and capital expenses.

Explanation: Legal Language: The policy uses facilitative terms like “allocated,” “award,” and “reserved,” which emphasize voluntary participation. There is no mandatory language (e.g., “shall,” “must”) requiring transit providers to apply for or implement projects.
Source of Authority: Established through the state budget (FY24 allocation) and administered by MassDOT. It functions as a grant program, not a regulatory mandate.
Enforcement Mechanism: No penalties or compliance requirements for transit providers. Enforcement is limited to program administration (e.g., ensuring 25% of funds are reserved for rural areas, verifying eligibility criteria).
Obligations: Transit providers are not legally obligated to apply for grants or undertake projects. Participation is entirely optional. MassDOT must administer the funds according to budget directives but has no authority to compel action from external entities.
Optionality/Incentives: Grants act as financial incentives for transit providers to enhance services (e.g., electrification, expanded hours). Participation is voluntary—transit providers choose whether to submit eligible projects.


Case 2:
Policy ID: policy/1259
Name: EV Charging Stations Requirements for New State Facility Construction
Similarity: 0.5433
Score: 3
Type: Standard
Description: (b) On and after January 1, 2023, the Commissioner of Administrative Services shall require each new construction of a state facility, the total project costs of which exceed one hundred thousand dollars, to be installed with level two electric vehicle charging stations in at least twenty per cent of the designated parking spaces for cars or light duty trucks at such facility. (c) On and after January 1, 2023, a municipality shall require each new construction of a commercial building or multiunit residential building with thirty or more designated parking spaces for cars or light duty trucks to include electric vehicle charging infrastructure that is capable of supporting level two electric vehicle charging stations or direct current fast charging stations in at least ten per cent of such parking spaces. A municipality may, through its legislative body, require any such commercial building or multiunit residential building to include such electric vehicle charging infrastructure in more than ten per cent of such parking spaces.

Explanation: Legal Language: The policy uses mandatory terms such as “shall require” (e.g., “the Commissioner shall require,” “a municipality shall require”) for the baseline requirements (20% for state facilities, 10% for commercial/residential buildings). The term “may” applies only to optional stricter standards beyond 10%.
Source of Authority: Likely statutory or regulatory (e.g., state building codes or administrative law), given the prescriptive language and delegation of authority to the Commissioner and municipalities.
Enforcement Mechanism: Compliance is tied to construction permits and project approvals (implied by the focus on new construction). Non-compliance could result in denial of permits or failure to meet building code standards, though penalties are not explicitly stated.
Obligations: State facilities and municipalities are legally obligated to enforce the minimum EV charging infrastructure percentages (20% for state facilities, 10% for commercial/residential). Municipalities have discretion to exceed the 10% threshold but must enforce the base requirement.
Optionality/Incentives: The 10% requirement for commercial/residential buildings is mandatory, with optionality only for stricter standards. No financial incentives are mentioned—compliance is compulsory for covered projects.

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