# exposure-report-starter

A starter template for generating exposure reports from structured inputs. This project is intended to help teams standardize how they collect inputs, score risk, and present findings. It does **not** perform independent verification of inputs and should not be treated as authoritative without external validation.

## Intended Use
- Compile known data about an entity, asset, or system into a consistent report format.
- Provide a quick, repeatable way to communicate **risk posture** based on supplied data.
- Support internal reviews, stakeholder updates, and decision-making workflows.

**Not intended for:**
- Real-time threat detection or monitoring.
- Legal, compliance, or regulatory determinations without expert review.
- Automated enforcement actions.

## Input Schema
Inputs are provided as JSON with the following top-level shape:

```json
{
  "report_metadata": {
    "report_id": "string",
    "generated_at": "ISO-8601 timestamp",
    "subject": "string",
    "prepared_by": "string"
  },
  "data_sources": [
    {
      "name": "string",
      "description": "string",
      "collected_at": "ISO-8601 timestamp",
      "provenance": "string"
    }
  ],
  "findings": [
    {
      "id": "string",
      "title": "string",
      "description": "string",
      "evidence": "string",
      "severity": "low | medium | high",
      "likelihood": "low | medium | high",
      "impact": "low | medium | high",
      "status": "open | mitigated | accepted"
    }
  ],
  "assumptions": ["string"],
  "limitations": ["string"],
  "notes": "string"
}
```

### Minimal Example
```json
{
  "report_metadata": {
    "report_id": "RPT-001",
    "generated_at": "2024-05-01T12:00:00Z",
    "subject": "Acme Corp - Public Web App",
    "prepared_by": "Security Team"
  },
  "data_sources": [
    {
      "name": "Customer Questionnaire",
      "description": "Self-reported responses",
      "collected_at": "2024-04-28T09:30:00Z",
      "provenance": "Provided by Acme Corp"
    }
  ],
  "findings": [
    {
      "id": "F-001",
      "title": "No MFA on admin accounts",
      "description": "Administrative accounts do not require MFA.",
      "evidence": "Questionnaire response Q12",
      "severity": "high",
      "likelihood": "medium",
      "impact": "high",
      "status": "open"
    }
  ],
  "assumptions": [
    "Responses are accurate and complete."
  ],
  "limitations": [
    "No system access was provided to validate controls."
  ],
  "notes": "This report is based solely on provided information."
}
```

## Report Structure
Generated reports should follow this structure (order can be adjusted as needed):
1. **Executive Summary**
2. **Scope & Subject**
3. **Data Sources & Provenance**
4. **Risk Scoring Overview**
5. **Findings** (grouped by severity)
6. **Assumptions & Limitations**
7. **Recommendations / Next Steps**
8. **Appendix** (raw input, references)

## Risk Scoring Methodology
Each finding includes severity, likelihood, and impact. The overall risk rating uses the following rubric:

- **Low**: Limited impact, low likelihood, or well-contained exposure.
- **Medium**: Material impact or moderate likelihood, requiring mitigation planning.
- **High**: Significant impact and/or high likelihood that demands prompt attention.

When combining factors, use judgment and document the rationale in the finding description or notes.

## Example Output
```markdown
# Exposure Report: Acme Corp - Public Web App

## Executive Summary
This report summarizes exposure risks based on self-reported data. No independent validation was performed.

## Data Sources & Provenance
- Customer Questionnaire (Provided by Acme Corp, collected 2024-04-28)

## Findings
### High
- **F-001: No MFA on admin accounts**
  - Severity: High | Likelihood: Medium | Impact: High
  - Evidence: Questionnaire response Q12
  - Status: Open

## Assumptions & Limitations
- Responses are accurate and complete.
- No system access was provided to validate controls.
```

## Ethical Use
- Use this template to **communicate risk** and support responsible decision-making.
- Do not use outputs to shame, penalize, or misrepresent subjects.
- Ensure findings are reviewed by qualified personnel before action.

## Limitations
- **Data provenance matters:** reports are only as reliable as the inputs and their sources.
- **No independent verification:** findings are derived exclusively from supplied data.
- **Scope-constrained:** results do not account for unknown assets, hidden dependencies, or unreported controls.
- **Time-bound:** inputs may be stale; validate before making decisions.

## Data Provenance & Verification Disclaimer
All findings, risk ratings, and summaries are based on the data provided in the input schema and the stated data sources. This template does not perform independent verification, technical validation, or continuous monitoring. Users must verify critical information with primary sources or direct assessment before relying on the report.
