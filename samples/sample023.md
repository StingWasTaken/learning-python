# Sample 23

You’ve stumbled upon one of those Python quirks where things look like **private/protected** in other languages, but actually they’re not! Let me break it down:

---

## 1. `_protected` (single underscore)

* This is **just a convention** in Python.
* It means: *“This method/attribute is intended for internal use, don’t touch it from outside unless you know what you’re doing.”*
* The interpreter does **not enforce** anything — you can still call it from anywhere.

```python
obj = Parent()
obj._protected()   # Works, but "bad style"
```

So `_protected` is **not** like `protected` in Java or C# — it’s purely by naming convention.

---

## 2. `__private` (double underscore)

* This is **name mangling**, not true private.
* Python rewrites the method name internally to include the class name.
* In your case, `__private` in `Parent` becomes `_Parent__private`.

That’s why in `Child`, calling `self.__private()` fails, because Python looks for `_Child__private`, which doesn’t exist.

If you want to call it, you’d have to do:

```python
self._Parent__private()
```

---

## 3. Was it introduced later?

Nope 🙂 This has been in Python since the early days (at least Python 2).

* Single underscore = **convention for protected**.
* Double underscore = **name mangling to avoid accidental overrides in subclasses**.

But Python’s philosophy is *“we are all consenting adults here”*. There’s no enforced `private` or `protected` like in Java/C#.

---

✅ **Summary**:

* `_method` → convention: “don’t use outside the class” (but you *can*).
* `__method` → name-mangling: helps avoid accidental conflicts in subclasses, not real privacy.

---

Do you want me to show you how your `Child` class can still call `Parent.__private()` properly, with a small code snippet?
