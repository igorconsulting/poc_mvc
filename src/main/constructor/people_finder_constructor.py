from views.people_finder_view import PeopleFinderView

def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    
    # Controller
    person_fider_informations = people_finder_view.person_finder_view()

    # Send to controller
    