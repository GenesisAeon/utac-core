# CLI Reference

The `utac` CLI provides direct access to UTAC logistic computations from the terminal.

## `utac fit`

Fit β to the UTAC logistic threshold from R and Θ sequences.

```
Usage: utac fit [OPTIONS]

Options:
  --r FLOAT     R values (repeatable)   [default: 1.0, 1.618, 2.718]
  --theta FLOAT Θ values (repeatable)   [default: 0.618, 1.0, 1.618]
```

```bash
utac fit
utac fit --r 2.0 --r 3.0 --theta 1.0 --theta 1.5
```

---

## `utac rig`

Calculate v_RIG (recursive implosive growth) at time t.

```
Usage: utac rig [OPTIONS] [T]

Arguments:
  T  Time value  [default: 10.0]

Options:
  -b, --beta FLOAT  β parameter  [default: 0.0625]
```

```bash
utac rig 10.0
utac rig 100.0 --beta 0.1
```

---

## `utac frame-principle`

Display the symbolic Frame-Principle equation σ(β(R−Θ)) = σ_Φ.

```bash
utac frame-principle
```

---

## `utac logistic`

Evaluate the UTAC logistic function σ(β(x − Θ)).

```
Usage: utac logistic [OPTIONS] X

Arguments:
  X  Input x

Options:
  -b, --beta FLOAT   β parameter  [default: 0.0625]
  -t, --theta FLOAT  Threshold Θ  [default: 0.0]
```

```bash
utac logistic 1.618
utac logistic 1.618 --beta 0.0625 --theta 1.0
```
