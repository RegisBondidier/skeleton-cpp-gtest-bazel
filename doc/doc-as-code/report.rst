=========
 Reports
=========

.. needpie:: Requirements status
   :labels: draft, submitted, agreed, rejected, obsolete
   :colors: yellow, orange, green, blue, red, gray, cyan
   :legend:

   type == 'req' and 'outgoing_requirement' not in tags and status == 'draft'
   type == 'req' and 'outgoing_requirement' not in tags and status == 'submitted'
   type == 'req' and 'outgoing_requirement' not in tags and status == 'agreed'
   type == 'req' and 'outgoing_requirement' not in tags and status == 'rejected'
   type == 'req' and 'outgoing_requirement' not in tags and status == 'obsolete'

.. needpie:: Requirements implemented
   :labels: implemented, missing impl.
   :colors: green, lightgreen, red
   :legend:
   :filter-func: reporting_functions.requirements_report()

.. needpie:: Components tested
   :labels: tested, missing test
   :colors: green, lightgreen, red
   :filter-func: reporting_functions.components_report()


