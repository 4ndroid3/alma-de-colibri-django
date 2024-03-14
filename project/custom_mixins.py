class RegisterUserOnForm:
    """
    Mixin to automatically set the 'created_by' and 'updated_by' fields to the current user on save.
    """

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
