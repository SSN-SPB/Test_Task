package io.github.jditesting.pages;

import com.epam.jdi.light.elements.pageobjects.annotations.locators.*;
import com.epam.jdi.light.elements.composite.*;
import com.epam.jdi.light.elements.complex.*;
import com.epam.jdi.light.elements.common.*;
import com.epam.jdi.light.elements.complex.dropdown.*;
import com.epam.jdi.light.elements.complex.table.*;
import com.epam.jdi.light.ui.html.elements.complex.*;
import com.epam.jdi.light.ui.html.elements.common.*;
import io.github.jditesting.sections.*;

public class HomePage extends WebPage {
    @UI("header") public Header header;
    @UI("footer") public Footer footer;
    @UI("[name='main-title']") public Label mainTitle;
    @UI(".main-txt") public Text jdiText;
    @UI(".sidebar-menu") public Menu sidebarMenu;
	
}