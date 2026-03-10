# Config & Constants Policy

Rules for managing configuration values, constants, and default values across the project.

## Rules

### 1. No Unexplained Magic Numbers

Every literal value in source code must be either:
- A named constant with a descriptive name, or
- An obviously self-explanatory value (e.g., `0`, `1`, `true`, `""`)

**Bad:**
```
if items.len() > 512 { split_batch(); }
sleep(Duration::from_millis(150));
let scale = 0.0254;
```

**Good:**
```
const MAX_BATCH_SIZE: usize = 512;  // GPU upload limit per frame
if items.len() > MAX_BATCH_SIZE { split_batch(); }

const DEBOUNCE_MS: u64 = 150;  // Prevents redundant reloads during rapid input
sleep(Duration::from_millis(DEBOUNCE_MS));

const INCHES_TO_METERS: f64 = 0.0254;
let scale = INCHES_TO_METERS;
```

### 2. Tunable Values Belong in Config

Values that may change across environments, deployments, or user preferences must not be hardcoded. They belong in a configuration layer.

**Examples of tunable values:**
- Buffer sizes, cache limits, batch sizes
- Timeouts, retry counts, polling intervals
- UI defaults (window size, font size, colors)
- Feature flags

**Examples of non-tunable values (constants are fine):**
- Mathematical constants (PI, conversion factors)
- Protocol-mandated values
- Compile-time-fixed type sizes

### 3. Defaults Must Have a Single Source of Truth

Each default value must be defined in exactly one place. Other code references that definition — never duplicates it.

**Pattern:**
```
// config/defaults.rs (or equivalent)
pub const DEFAULT_CACHE_SIZE: usize = 256;

// usage site — references, not redefines
let cache_size = config.cache_size.unwrap_or(DEFAULT_CACHE_SIZE);
```

### 4. Constants Must Be Named Descriptively

The name should explain **what** the value represents, not just **where** it's used.

**Bad:** `LIMIT`, `THRESHOLD`, `SIZE`, `VALUE`
**Good:** `MAX_CONCURRENT_LOADS`, `STALE_CACHE_THRESHOLD_SECS`, `GPU_UPLOAD_BATCH_SIZE`

### 5. Config Layering

When a project grows, configuration should support layering:

```
Hardcoded defaults  →  Config file  →  Environment variables  →  CLI flags
```

Each layer overrides the previous. The leftmost is always available as a fallback.

## Enforcement

- During `/analyze` and `/audit`, flag unexplained magic numbers.
- During code review, verify that new tunable values are in config, not hardcoded.
- The change impact checklist includes a config/constants check.
