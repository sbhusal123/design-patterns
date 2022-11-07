# Liskcov Substitution Principle

- If #(x) is provableabout obj of x of type T.
- Then #(y) must be provable for obj of y and type S.
- Keeping in min: S is a subtype of T.

**Conclusion**
- Child class objects should be able to replace the parent class without breaking the integrity.
- Whatever the parent can do, the descendants should at least be able to do that too.

