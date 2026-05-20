# Target of project
Demo of comparing UI WEB screenshots within pytest/Playwright TAF (Test Automation Framework)

# Run tests

To run tests use command <br>
<i><b> pytest -v </i></b><br>
within project's root directory

# Images explanation<br>
<br>
<b>Permanent files in project: </b><br>
<li>\mask_snapshots\mask_image.png - Screen the mask on areas of screenshot that should be applied for images</li><br>
<li>\reference_snapshots\reference.png -  expected view of actual screenshot with applied mask image</li><br>
<li>\test_snapshots\actual_demo1.png - Preserved for the test scenarios </li><br>
<i>Remark: the other files are used to update mask_image.png and reference.png for specific scenarios </i><br>
<br>
<b>Images created during the test:</b> <br>
<li>\test_snapshots\actual.png - Actual screenshot </li><br>
<li>\test_snapshots\actual_with_applied_mask.png -  actual image with applied mask image</li><br>
<li>\differences_snapshots\found_differences.png - test creates it <b>if the difference is found </b></li><br> 
<br>
<b>Compared files:</b><br>
\test_snapshots\actual_with_applied_mask.png vs reference.png\reference_snapshots\reference.png <br>
<br>
<b>The difference's sensitivity adjusting</b> <br>
diff = diff.convert("L")  # grayscale - "L" - the most convenient mode of comparing<br>
diff = diff.point(lambda x: 255 if x > 0 else 0) - define content of found_differences.png <br>
- Possible changing: - x > 0 can be e.g. x > 7 - decreases sensitivity<br>
<br>
<br>
<b>Test scenarios</b><br>
Scenario 1 basic<br>
<li>mask_image.png == mask_image_init.png</li><br>
<li>reference.png == reference_good.png</li><br>
<li>Tests pass</li><br>
<br>
Scenario 2 modified failed<br>
<li>mask_image.png == mask_image_init.png</li><br>
<li>reference.png == reference_good.png</li><br>
<li><b>Line <i>page_content.make_screen_shot(actual_image)</i> is commented</b></li><br>
<li><b>actual.png == actual_modified_for_test.png</b></li><br>
<li>Tests fails</li><br>
The images: \differences_snapshots\found_differences.png and \test_snapshots\actual_with_applied_mask.png contain text:<br>
"constant text"<br>
<br>
