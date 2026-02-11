# Target of project
Demo of comparing UI WEB screenshots within pytest/Playwright TAF (Test Automation Framework)

# Run tests

Run command <br>
<i><b> pytest -v </i></b><br>
within project's root directory

# UI test image comparing explanation<br>
##Screenshot's agenda
<li>actual.png - Actual screenshot, created during the test </li> 
<li>mask_image.png - Screen the mask on areas of screenshot that should be applied for images</li>
<li>reference.png -  expected view of actual screenshot with applied mask image</li> 
<li>tested_image.png -  actual image with applied mask image</li> 
<li>found_differences.png - file created if the differences  is found </li> 

##Screenshot's agenda<br>
Compared files: tested_image.png and reference.png<br>

##Screenshot's agenda<br>
diff = diff.convert("L")  # grayscale - "L" - the most convenient mode of comparing<br>
diff = diff.point(lambda x: 255 if x > 0 else 0) - define content of found_differences.png <br>
- Possible changing: - x > 0 can be e.g. x > 7 - decreases sensitivity

##Demo scenarios<br>
### Scenario 1 basic
<li>mask_image.png == mask_image_init.png</li>
<li>reference.png == reference_good.png</li>
<li>Line <i>page_content.make_screen_shot(actual_image)</i> is uncommented</li>
<li>Tests pass</li>

### Scenario 2 modified failed
<li>mask_image.png == mask_image_init.png</li>
<li>reference.png == reference_good.png</li>
<li>Line <i>page_content.make_screen_shot(actual_image)</i> is commented</li>
<li><b>actual.png == actual_modified_for_test.png</b></li>
<li>Tests fails</li>
- found_differences.png and tested_image.png contains text - "constant text"

### Scenario 3 modified Fixed
<li>mask_image.png == mask_image_init.png</li>
<li><b>reference.png == reference_modified_for_test.png (or tested_image.png from test 2) </b> </li>
<li>Line <i>page_content.make_screen_shot(actual_image)</i> is commented</li>
<li>actual.png == actual_modified_for_test.png</li>
<li>Tests pass</li>

### Scenario 4 corrupted failed
<li>mask_image.png == mask_image_init.png</li>
<li><b>reference.png == reference_good.png<b></li>
<li>Line <i>page_content.make_screen_shot(actual_image)</i> is commented</li>
<li><b>actual.png == actual_corrupted_for_test.png</b></li>
<li>Tests fails</li>
- found_differences.png and tested_image.png contains text - "unexpected text"

### Scenario 5 corrupted Fixed
<li><b>mask_image.png == mask_image_corrected.png</b></li>
<li><b>reference.png == reference_with_mask_for_corrupted_actual.png</b></li>
<li>Line <i>page_content.make_screen_shot(actual_image)</i> is commented</li>
<li>actual.png == actual_corrupted_for_test.png</li>
<li>Tests pass</li>
