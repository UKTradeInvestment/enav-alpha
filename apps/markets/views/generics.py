from django.views.generic import ListView, DetailView, FormView, TemplateView


class EnavViewMixin(object):
    """
    Mixin class to get/set the desired solution in the request, and modify the template name rendered based upon it
    """

    # Default solution number
    solution = 1

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

    def get_template_names(self, *args, **kwargs):
        """
        Modify the template name the view will render by inserting the solution number before the last '.'
        e.g. 'template.html' will become 'template.X.html' where X is the solution number
        Also includes the standard template name as a fallback if there is no solution-specific template to use
        """

        # Split the template name on '.' and insert into the resulting list, the solution number we need to show
        template_name_components = self.template_name.split('.')
        template_name_components.insert(-1, str(self.solution))

        # Form the override template name and insert it into the standard result
        override_template = ".".join(template_name_components)
        templates = super().get_template_names(*args, **kwargs)
        templates.insert(0, override_template)
        return templates

    def get_context_data(self, *args, **kwargs):
        # Add the solution to the context before rendering
        self._get_solution()
        context = super().get_context_data(*args, **kwargs)
        context['solution'] = self.solution
        return context


class EnavListView(EnavViewMixin, ListView):
    pass


class EnavDetailView(EnavViewMixin, DetailView):
    pass


class EnavFormView(EnavViewMixin, FormView):
    pass


class EnavTemplateView(EnavViewMixin, TemplateView):
    pass
