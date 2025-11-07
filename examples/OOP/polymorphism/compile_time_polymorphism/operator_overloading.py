# ===========================================================
# POINT2D OPERATOR OVERLOADING --> COMPILE-TIME POLYMORPHISM
# ===========================================================

class Point2D:
    """
    Demonstrates operator overloading in Python using magic methods.

    Operators overloaded (magic methods):
        - __add__ : + (point + point)
        - __sub__ : - (point - point)
        - __mul__ : * (point * scalar)
        - __rmul__ : * (scalar * point)
        - __truediv__ : / (point / scalar)
        - __eq__ : == (equality)
        - __ge__ : >= (component-wise)
        - __len__ : returns number of attributes len(point)
        - __str__ / __repr__ : print-friendly representation

    This mimics compile-time polymorphism in statically typed languages,
    where operator resolution depends on operand types.

    C++ Equivalent:
        class Point2D {
        public:
            double x, y;
            Point2D(double x, double y) : x(x), y(y) {}
            Point2D operator+(const Point2D& p) { return Point2D(x + p.x, y + p.y); }
            Point2D operator-(const Point2D& p) { return Point2D(x - p.x, y - p.y); }
            Point2D operator*(double scalar) { return Point2D(x * scalar, y * scalar); }
            friend Point2D operator*(double scalar, const Point2D& p) { return Point2D(p.x * scalar, p.y * scalar); }
            Point2D operator/(double scalar) { return Point2D(x / scalar, y / scalar); }
            bool operator==(const Point2D& p) { return x == p.x && y == p.y; }
            // etc.
        };

    Java Equivalent (no operator overloading, use methods instead):
        class Point2D {
            double x, y;
            Point2D(double x, double y) { this.x = x; this.y = y; }
            Point2D add(Point2D p) { return new Point2D(x + p.x, y + p.y); }
            Point2D sub(Point2D p) { return new Point2D(x - p.x, y - p.y); }
            Point2D mul(double scalar) { return new Point2D(x * scalar, y * scalar); }
            Point2D rmul(double scalar) { return new Point2D(x * scalar, y * scalar); }
            Point2D div(double scalar) { return new Point2D(x / scalar, y / scalar); }
            boolean equals(Point2D p) { return x == p.x && y == p.y; }
            // etc.
        }
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self: 'Point2D', other: 'Point2D'):
        """Overloads the + operator for Point2D + Point2D"""
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self: 'Point2D', other: 'Point2D'):
        """Overloads the - operator for Point2D - Point2D"""
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self: 'Point2D', scalar: float):
        """Left multiplication: point * scalar"""
        return Point2D(self.x * scalar, self.y * scalar)

    def __rmul__(self: 'Point2D', scalar: float):
        """Right multiplication: scalar * point"""
        return Point2D(scalar * self.x, scalar * self.y)

    def __truediv__(self: 'Point2D', scalar: float):
        """Overloads the / operator for Point2D / scalar"""
        return Point2D(self.x / scalar, self.y / scalar)

    def __eq__(self: 'Point2D', other: 'Point2D'):
        """Overloads the == operator for Point2D equality"""
        return self.x == other.x and self.y == other.y

    def __ge__(self: 'Point2D', other: 'Point2D'):
        """Overloads the >= operator for Point2D (component-wise)"""
        return self.x >= other.x and self.y >= other.y

    def __len__(self: 'Point2D'):
        """Overloads the len() function to return number of attributes"""
        return len(self.__dict__)

    def __str__(self: 'Point2D'):
        """Overloads the str() function for print-friendly representation"""
        return f"Point2D({self.x}, {self.y})"
    
    def __repr__(self: 'Point2D'):
        """Overloads the repr() function for unambiguous representation"""
        return self.__str__()


def main():
    print("#" * 60)
    print("Demonstration of Point2D operator overloading")
    print("#" * 60)

    # Basic point instances
    p1 = Point2D(2, 3)
    p2 = Point2D(4, 1)
    p3 = Point2D(2, 3)

    # Addition, subtraction
    print("Addition:", p1 + p2)         # Point2D(6, 4) -> uses __add__
    print("Subtraction:", p1 - p2)      # Point2D(-2, 2) -> uses __sub__

    # Scalar multiplication
    print("p1 * 2:", p1 * 2)            # Point2D(4, 6) -> uses __mul__
    print("3 * p1:", 3 * p1)            # Point2D(6, 9) -> uses __rmul__

    # Division
    print("p1 / 2:", p1 / 2)            # Point2D(1.0, 1.5) -> uses __truediv__

    # Equality
    print("p1 == p2:", p1 == p2)        # False -> uses __eq__
    print("p1 == p3:", p1 == p3)        # True -> uses __eq__
    print("p1 is p3:", p1 is p3)        # False (different instances) -> identity check

    # Comparison and len
    p4 = Point2D(6, 4)
    p5 = Point2D(3, 4)
    p6 = Point2D(4, 3)
    p7 = p5 + p2                        # Point2D(7, 5) -> uses __add__
    p8 = p7 + p6 - (p1 + p3 + p4)       # Point2D(1, -2) -> uses __add__ and __sub__

    points = [p1, p2, p3, p4, p5, p6, p7, p8]

    print("\nListing points and their attribute lengths:")
    for i, pt in enumerate(points, start=1):
        print(f"Point P{i}: {pt}, length = {len(pt)}")

    # Component-wise comparisons
    print("\nComponent-wise comparisons:")
    print("p1 == p2:", p1 == p2)
    print("p3 >= p4:", p3 >= p4)
    print("p5 == p6:", p5 == p6)


if __name__ == "__main__":
    main()
