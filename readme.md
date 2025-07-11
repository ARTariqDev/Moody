# Moody , beg to compile your code! (or don't and watch the compiler cry)

**Moody* is a playful, tone-sensitive programming language that only compiles your code if you’re polite enough. It supports basic control structures, recursion, and even enforces good manners through tone analysis.

## Features

- Moody keywords like `beg`, `plead`, `request`, `thanks`, `threaten`, and more
- Custom tone analysis (you must be polite to compile)
- Basic programming constructs: functions, variables, loops, conditionals
- Support for recursion and nested scopes
- Transpiles MoodyLang to Python and runs the result

## Tone Rules

To successfully compile:

- At least **3 polite ("good") keywords** must be used
- Overall tone score must be **≥ 6**
- Saying `thanks` is **mandatory**
- Overuse of any one keyword is discouraged and may throw errors

### Keyword Categories

- **GOOD:** `beg`, `prettyPlease`, `plead`, `request`, `thanks`
- **NEUTRAL:** `hey`, `sup`, `listen`, `yo`, `btw`, `proceed`
- **BAD:** `youBetter`, `dare`, `threaten`, `submit`, `now`

## Example MoodyLang Code

```moody
beg def factorial(n) {
    listen if (n == 0) {
        request 1;
    }
    plead request n * factorial(n - 1);
}

yo const x = 5;
humblyRequest print(factorial(x));
thanks
# Moody
