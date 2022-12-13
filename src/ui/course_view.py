from tkinter import ttk, constants
from services.course_service import course_service

class CourseListView:
    """Kurssien listauksesta vastaava näkymä."""

    def __init__(self, root, courses):
        """Luokan konstruktori. Luo uuden kurssilistausnäkymän.
        
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            courses:
                Lista Course-olioita, jotka näkymässä näytetään
            handle_set_course_done:
                Kutsuttava-arvo, jota kutsutaan kun kurssi on suoritettu. Saa argumentiksi suoritetun kurssin id-arvon.
        """

        self._root = root
        self._courses = courses
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_course_item(self, course):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=course.content)

        set_done_button = ttk.Button(
            master=item_frame,
            text="Done",
            command=lambda: self._handle_set_course_done(course.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        set_done_button.grid(
            row=0,
            column=1,
            padx=6,
            pady=6,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for course in self._courses:
            self._initialize_course_item(course)


class CourseView:
    """Kurssien listauksesta ja lisäämisestä vastaava näkymä."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden kurssinäkymän.
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
        """

        self._root = root
        self._frame = None
        self._create_course_entry = None
        self._course_list_frame = None
        self._course_list_view = None

        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Poistaa näkymän."""
        self._frame.destroy()

    def _handle_set_course_done(self, course_id):
        course_service.set_course_done(course_id)
        self._initialize_course_list()

    def _initialize_course_list(self):
        if self._course_list_view:
            self._course_list_view.destroy()

        courses = course_service.get_undone_courses()

        self._course_list_view = CourseListView(
            self._course_list_frame,
            courses,
            self._handle_set_course_done
        )

        self._course_list_view.pack()


    def _handle_add_course(self):
        course_content = self._add_course_entry.get()

        if course_content:
            course_service.add_course(course_content)
            self._initialize_course_list()
            self._add_course_entry.delete(0, constants.END)

    def _initialize_footer(self):
        self._add_course_entry = ttk.Entry(master=self._frame)

        add_course_button = ttk.Button(
            master=self._frame,
            text="Add",
            command=self._handle_add_course
        )

        self._add_course_entry.grid(
            row=2,
            column=0,
            padx=6,
            pady=6,
            sticky=constants.EW
        )

        add_course_button.grid(
            row=2,
            column=1,
            padx=6,
            pady=6,
            sticky=constants.EW
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._course_list_frame = ttk.Frame(master=self._frame)

        self._initialize_footer()

        self._course_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)