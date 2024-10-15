from manim import *


def get_horizontal_line_to_graph(axes, function, x, width, color):
    result = VGroup()
    line = DashedLine(
        start=axes.c2p(0, function.underlying_function(x)),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color,
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    result.add(line, dot)
    return result


def get_arc_lines_on_function(
    graph, plane, dx=1, line_color=WHITE, line_width=1, x_min=None, x_max=None
):

    dots = VGroup()
    lines = VGroup()
    result = VGroup(dots, lines)

    x_range = np.arange(x_min, x_max, dx)
    colors = color_gradient([BLUE_B, GREEN_B], len(x_range))

    for x, color in zip(x_range, colors):
        p1 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x, graph))
        p2 = Dot().scale(0.7).move_to(plane.input_to_graph_point(x + dx, graph))
        dots.add(p1, p2)
        dots.set_fill(colors, opacity=0.8)

        line = Line(
            p1.get_center(),
            p2.get_center(),
            stroke_color=line_color,
            stroke_width=line_width,
        )
        lines.add(line)

    return result


class Func(Scene):
    def construct(self):

        k = ValueTracker(0)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(x_range=[0, 20, 2], y_range=[100, 600, 60], x_length=6, y_length=3)
            .add_coordinates()
            .shift(LEFT * 3.5)
        )

        func1 = plane1.plot(
            lambda x: (-1 / 5) * x ** 3 + 5*x**2 + 100 , x_range=[0, 20], color=RED_C
        )
        func1_lab = (
            MathTex(r"Q(t)=-\frac{1}{5}t^3 + 5t^2 + 100")

            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                Create(func1),
                Write(func1_lab),
                run_time=5,
                lag_ratio=0.5,
            )
        )
        self.wait(10)


class Derivatives(Scene):
    def construct(self):

        k = ValueTracker(0)  # Tracking the end values of stuff to show

        # Adding Mobjects for the first plane
        plane1 = (
            NumberPlane(x_range=[0, 20, 2], y_range=[100, 600, 60], x_length=6, y_length=3)
            .add_coordinates()
            .shift(LEFT * 3.5)
        )

        func1 = plane1.plot(
            lambda x: (-1 / 5) * x ** 3 + 5*x**2 + 100 , x_range=[0, 20], color=RED_C
        )
        func1_lab = (
            MathTex(r"Q(t)=-\frac{1}{5}t^3 + 5t^2 + 100")

            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=2,
                secant_line_color=YELLOW,
            )
        )

        dot = always_redraw(
            lambda: Dot().move_to(
                plane1.c2p(k.get_value(), func1.underlying_function(k.get_value()))
            )
        )

        # Adding Mobjects for the second plane
        plane2 = (
            NumberPlane(x_range=[0, 20, 2], y_range=[0, 50, 5], x_length=6, y_length=3)
            .add_coordinates()
            .shift(RIGHT * 3.5)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: (-3/5)*x ** 2 + 10*x, x_range=[0, k.get_value()], color=GREEN
            )
        )
        func2_lab = (
            MathTex(r"Q'(t)=-\frac{3}{5}t^2 + 10t")
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2, function=func2, x=k.get_value(), width=2, color=YELLOW
            )
        )
        value_label = always_redraw(
          lambda: MathTex(f"{func1.underlying_function(k.get_value()):.2f}")
          .next_to(dot, DOWN, buff=0.2)
          .set_color(WHITE)
      )

        t_value_text = (
            Tex("t = ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .shift(LEFT * 2)  # Shift the entire label group to the left
            .add_background_rectangle()
        )

        # Adding the "Q(t) =" label
        q_value_text = (
            Tex("$\\Rightarrow$ "," Q(t) = ")  # Label for the Q(t) value
            .next_to(t_value_text, RIGHT, buff=1.0)  # Place to the right of t-value
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        # Display the t-value (dx_value)
        dx_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(k.get_value())  # t value at the current point
            .next_to(t_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        )

        # Display Q(t) value (function value at t)
        q_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(func1.underlying_function(k.get_value()))  # Function value Q(t)
            .next_to(q_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        )

        # Group the labels and values together
        t_q_group = VGroup(t_value_text, dx_value, q_value_text, q_value).arrange(RIGHT, buff=0.2)

        t_q_group.next_to(plane1, DOWN, buff=0.5)


        dx_value_text = (
            Tex("t = ")  # Label for the t-value
            .next_to(plane2, DOWN, buff=0.1)
            .set_color(YELLOW)
            .shift(LEFT * 2)  # Shift the entire label group to the left
            .add_background_rectangle()
        )

        # Adding the "Q(t) =" label
        slope_value_text = (
            Tex("$\\Rightarrow$ "," Q'(t) = ")  # Label for the Q(t) value
            .next_to(dx_value_text, RIGHT, buff=1.0)  # Place to the right of t-value
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        # Display the t-value (dx_value)
        dx_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(k.get_value())  # t value at the current point
            .next_to(dx_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        )

        # Display Q(t) value (function value at t)
        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=2)
            .set_value(func2.underlying_function(k.get_value()))  # Function value Q(t)
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(YELLOW)
        )

        # Group the labels and values together
        slope_group = VGroup(dx_value_text, dx_value, slope_value_text, slope_value).arrange(RIGHT, buff=0.2)
        slope_group.next_to(plane2, DOWN, buff=0.5)
        # Add the group to the scene

        # slope_value_text = (
        #     Tex("Q'(t)= ")  # Label for the slope value
        #     .next_to(plane2, DOWN, buff=0.1)
        #     .set_color(YELLOW)
        #     .add_background_rectangle()
        # )

        # # Create the dx (t) value display (x or t value for the slope)
        # dx_value = always_redraw(
        #     lambda: DecimalNumber(num_decimal_places=2)
        #     .set_value(k.get_value())  # t value at the current point
        #     .next_to(slope_value_text, RIGHT, buff=0.1)
        #     .set_color(YELLOW)  # Set same color as the slope
        # )

        # # Create slope value display (Q'(t) value or derivative)
        # slope_value = always_redraw(
        #     lambda: DecimalNumber(num_decimal_places=2)
        #     .set_value(func2.underlying_function(k.get_value()))  # Derivative value Q'(t)
        #     .next_to(dx_value, RIGHT, buff=0.5)  # Position slope after t
        #     .set_color(YELLOW)  # Same color as dx_value
        # ).add_background_rectangle()

        # # Grouping the dx (t) value and Q'(t) value together
        # x_slope_group = VGroup(dx_value, slope_value).arrange(RIGHT, buff=0.2)


        # Playing the animation
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_lab),
                Write(func2_lab),
                run_time=4,
                lag_ratio=0.5,
            )
        )
        self.add(moving_slope, moving_h_line, func2, t_q_group,value_label, slope_group, dot)
        self.play(k.animate.set_value(50/3), run_time=8, rate_func=linear)
        self.wait()

