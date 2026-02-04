# Data Model

This starter uses a simple, synthetic data model to describe exposure inputs.
Replace field names and definitions with your own internal schema as needed.

## Example Entities

### Exposure Source
| Field | Description |
| --- | --- |
| `source_id` | Synthetic identifier for the source system. |
| `source_name` | Human-readable label for the source. |
| `refresh_cadence` | Expected update frequency (for example, daily). |

### Exposure Record
| Field | Description |
| --- | --- |
| `record_id` | Synthetic identifier for the exposure record. |
| `source_id` | Foreign key linking back to the exposure source. |
| `exposure_type` | Category label such as "Example Type A". |
| `reported_at` | Timestamp indicating when the record was reported. |
