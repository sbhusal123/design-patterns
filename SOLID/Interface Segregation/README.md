# Interface Segregation Principle
- Principle States That: **“Clients should not be forced to depend upon interfaces that they do not use.”**

**What does that mean ??**
- A class implementating an interface should not be forced to implement a methods for an interface which is not in the concern of the class.
- This often violates a single responsibility principle.

**Example**
- Suppose you have an interface called ``MobileDevice`` which consists of two methods ``activate_gps`` and ``make_call``.
- Now, you created a two classes ``MobileWithGPS`` and ``MobileWithOutGPS``.
- For the foremost class, the interface works as intended.
- But for th other class, we saw that we actually dont need activate_gps.
