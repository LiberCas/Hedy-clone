import { createClass, addCustomizations } from '../../tools/classes/class.js';
import { loginForTeacher, logout} from '../../tools/login/login.js'
import { goToTeachersPage } from '../../tools/navigation/nav.js';

describe('Duplicate class tests', () => {
  it('Is able to duplicate class without adding second teachers', () => {
    loginForTeacher();
    const classname = createClass();
    addCustomizations(classname);
    goToTeachersPage();
    const duplicate_class = `test class ${Math.random()}`;

    // Click on duplicate icon
    cy.get('.no-underline > .fas').first().click();

    // Checks for input field
    cy.get('#modal-prompt-input').type(duplicate_class);
    cy.get('#modal-ok-button').click();

    cy.reload();

    cy.get(".view_class").contains(duplicate_class).click();
    cy.get("#customize-class-button").click();
    cy.get("#opening_date_container").should("not.be.visible")
    cy.get("#opening_date_label").click();
    cy.get("#opening_date_container").should("be.visible")
    cy.get("#enable_level_7").should('be.enabled');
    logout();
  })

  it('Is able to duplicate class with adding second teachers', () => {
    loginForTeacher();
    goToTeachersPage();

    cy.get("tr") // This class has second teachers.
    cy.get("#teacher_classes tbody .view_class")
      .each(($class, i) => {
          if ($class.text().includes("CLASS1")) {
            cy.get(`tbody :nth-child(${i+1}) .no-underline > .fas`).first().click();
          }
      })

    cy.get('#modal-yes-button').should('be.enabled').click();

    const duplicate_class = `test class ${Math.random()}`;
    cy.get('#modal-prompt-input').type(duplicate_class);
    cy.get('#modal-ok-button').click();

    cy.reload();

    cy.get(".view_class").contains(duplicate_class).click();
    cy.get("#invites-block").should('be.visible');
    cy.get("#customize-class-button").click();
    cy.get("#opening_date_container").should("not.be.visible")
    cy.get("#opening_date_label").click();
    cy.get("#opening_date_container").should("be.visible")
    cy.get("#enable_level_7").should('be.enabled');
  })
})
