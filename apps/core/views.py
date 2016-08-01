from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'homepage.html'
    solution = 1  # Default solution to use

    def get_context_data(self, *args, **kwargs):
        # Add the solution to the context before rendering
        self._get_solution()
        context = super().get_context_data(*args, **kwargs)
        context['solution'] = self.solution
        return context

    def _get_solution(self):
        # Try and get the desired solution from the request
        GET_solution = self.request.GET.get('solution', None)
        if GET_solution is not None:
            # parse the GET arg into an int, and this is our desired solution
            self.solution = int(GET_solution)
        else:
            # Not in the request, so get it from the session
            if 'solution' in self.request.session:
                self.solution = self.request.session['solution']

        # We got a solution number from the GET args, or from the session
        # Make sure it's saved back into the session
        self.request.session['solution'] = self.solution
