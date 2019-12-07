# Author: Mamadou Bah


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


##############################
# Class Rectangle
##############################
class Rectangle:
    'class that represents a rectangle in the plane'

    def __init__(self, bottom_left_coord, top_right_coord, rect_color):
        ''' (Rectangle, Point, Point, String) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.bottom_left = bottom_left_coord
        self.top_right = top_right_coord
        self.color = rect_color

    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns the coordinates of the bottom left point'''
        return self.bottom_left

    def get_top_right(self):
        '''(Rectangle)->Point
        Returns the coordinates of the top right point'''
        return self.top_right

    def get_color(self):
        '''(Rectangle)->str
        Returns the color of the rectangle'''
        return self.color

    def reset_color(self, new_color):
        '''(Rectangle)->None
        Resets the color of the rectangle to new_color'''
        self.color = new_color

    def get_perimeter(self):
        '''(Rectangle)->int
        Computes the perimeter of the rectangle'''
        length = ((self.top_right.get()[0])-(self.bottom_left.get()[0]))
        width = ((self.top_right.get()[1])-(self.bottom_left.get()[1]))
        perimeter = 2*(length+width)
        return perimeter

    def get_area(self):
        '''(Rectangle)->int
        Computes the area of the rectangle'''
        length = ((self.top_right.get()[0])-(self.bottom_left.get()[0]))
        width = ((self.top_right.get()[1])-(self.bottom_left.get()[1]))
        area = (length*width)
        return area

    def move(self, dx, dy):
        '''(Rectangle)->None
        Moves the calling rectangle by dx in the x direction and by dy in the y-direction'''
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    def intersects(self, other):
        '''(Rectangle, Rectangle)->bool
        Returns True if the calling rectangle intersects the given rectangle and False otherwise.'''
        return not (self.top_right.get()[0] < other.bottom_left.get()[0]
                    or self.bottom_left.get()[0] > other.top_right.get()[0]
                    or self.top_right.get()[1] < other.bottom_left.get()[1]
                    or self.bottom_left.get()[1] > other.top_right.get()[1])

    def contains(self, xcoord, ycoord):
        '''(Rectangle, int, int)->bool
        Returns True if that point is inside of the calling rectangle and False otherwise.'''
        return (self.bottom_left.get()[0] <= xcoord
                and self.top_right.get()[0] >= xcoord
                and self.bottom_left.get()[1] <= ycoord
                and self.top_right.get()[1] >= ycoord)

    # Added three methods that override python's object methods
    # (and make my class user friendly as suggested by the test cases)
    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.bottom_left.__eq__(other.bottom_left) == self.top_right.__eq__(other.top_right)

    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation Rectangle(Point(xc,0),Point(1,1),red)'''
        return "Rectangle("+self.bottom_left.__repr__()+","+self.top_right.__repr__()+",'"+str(self.color)+"')"

    def __str__(self):
        '''(Rectangle)->str
        Returns nice user friendly string representation as suggested by the test cases'''
        return "I am a "+self.color+" rectangle with bottom left corner at "+self.bottom_left.__str__()+" and top right corner at "+self.top_right.__str__()

##############################
# Class Canvas
##############################


class Canvas:

    def __init__(self):
        ''' (Canvas) -> None
        initialize a Canvas that represents a collection of Rectangles'''
        self.canvas_list = []

    def add_one_rectangle(self, rectangle):
        ''' (Canvas, Rectangle) -> None
        Adds a rectangle to the canvas list'''
        self.canvas_list.append(rectangle)

    def count_same_color(self, color):
        ''' (Canvas, str) -> int
        Returns the number of rectangle with the specified color'''

        count = 0
        if(len(self.canvas_list) == 0):
            return count
        else:
            for rect in self.canvas_list:
                if(rect.get_color() == color):
                    count += 1
            return count

    def total_perimeter(self):
        ''' (Canvas, str) -> int
        Returns the sum of the perimeters of all the rectangles in the calling canvas'''
        total_perimeter = 0
        if(len(self.canvas_list) == 0):
            return 0
        else:
            for rect in self.canvas_list:
                total_perimeter = total_perimeter + rect.get_perimeter()
            return total_perimeter

    def min_enclosing_rectangle(self):
        ''' (Canvas) -> Rectangle
        Returns the minimum enclosing rectangle that contains all the rectangles in the calling canvas'''

        if(len(self.canvas_list) == 0):
            return Rectangle(Point(0, 0), Point(0, 0), "red")
        else:
            all_rect_xcoord_list = []
            all_rect_ycoord_list = []
            # The minimum x coordinate of all rectangles
            min_xcoord = 0
            # The maximum x coordinate of all rectangles
            max_xcoord = 0
            # The minimum y coordinate of all rectangles
            min_ycoord = 0
            # The maximum y coordinate of all rectangles
            max_ycoord = 0

            for rect in self.canvas_list:
                all_rect_xcoord_list.append(rect.get_bottom_left().get()[0])
                all_rect_xcoord_list.append(rect.get_top_right().get()[0])

                all_rect_ycoord_list.append(rect.get_bottom_left().get()[1])
                all_rect_ycoord_list.append(rect.get_top_right().get()[1])

            # find the minimum x coordinate of all rectangles
            min_xcoord = min(all_rect_xcoord_list)
            # find the maximum x coordinate of all rectangles
            max_xcoord = max(all_rect_xcoord_list)
            # find the minimum y coordinate of all rectangles
            min_ycoord = min(all_rect_ycoord_list)
            # find the maximum y coordinate of all rectangles
            max_ycoord = max(all_rect_ycoord_list)

            # Returns the corresponding object of type Rectangle of
            # any color I prefer (Note: I choosed "red" for the color)
            return Rectangle(Point(min_xcoord, min_ycoord), Point(max_xcoord, max_ycoord), "red")

    def common_point(self):
        ''' (Canvas) -> bool
        Returns True if there exists a point that intersects all rectangles in the calling canvas'''
        result = True
        current_rect = 0
        for i in range(len(self.canvas_list)):
            for j in range(i + 1, len(self.canvas_list)):
                if(not self.canvas_list[i].intersects(self.canvas_list[j])):
                    result = False
                    break
        return result

    # Added two methods that override python's object
    # methods (and make my class user friendly as suggested by the test cases)

    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation of the Canvas'''
        result = ""
        for rect in self.canvas_list:
            result = result + rect.__repr__()+","
        return "Canvas("+result+")"

    def __str__(self):
        '''(Canvas)->str
        In this case we chose the same representation as in __repr__'''
        result = ""
        for rect in self.canvas_list:
            result = result + rect.__str__()+","
        return "Canvas("+result+")"
