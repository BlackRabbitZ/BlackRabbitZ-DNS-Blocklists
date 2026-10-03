# Validator Fix – 2026-10-03

Fixed cumulative profile ordering for `lists/platforms/software-hardware-telemetry/main/`.

| Profile | Before | After |
|---|---:|---:|
| Light | 75 | 75 |
| Normal | 28 | 75 |
| Pro | 73 | 80 |
| Pro++ | 76 | 80 |
| Ultimate | 84 | 85 |

Rule restored: `Light ⊆ Normal ⊆ Pro ⊆ Pro++ ⊆ Ultimate`.
