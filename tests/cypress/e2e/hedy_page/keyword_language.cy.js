import {goToHedyPageWithEnKeywords} from "../tools/navigation/nav";

describe('when the user changes their language to Arabic', () => {
  beforeEach(() => {
    goToHedyPageWithEnKeywords();
    cy.get('#editor > .cm-editor > .cm-scroller > .cm-content').click();
    cy.get('#editor').type("print Hallo!'\n");
    cy.getBySel('language-dropdown').click();
    cy.getBySel('switch-lang-ar').click();

    // switch back and forth
    cy.getBySel('kwlang-switch-btn').click();
    cy.getBySel('kwlang-switch-toggle').click();
  });

  it('initially has keywords in Arabic', () => {
    cy.contains('#editor > .cm-editor > .cm-scroller > .cm-content > .cm-line', 'قول').should('be.visible');
    cy.contains('#editor > .cm-editor > .cm-scroller > .cm-content > .cm-line', 'print').should('not.exist');
  });

  it('the keyword language switcher at the top can switch keywords to English', () => {
    cy.getBySel('kwlang-switch-btn').click();
    cy.getBySel('kwlang-switch-toggle').click();

    cy.contains('#editor > .cm-editor > .cm-scroller > .cm-content > .cm-line', 'قول').should('not.exist');
    cy.contains('#editor > .cm-editor > .cm-scroller > .cm-content > .cm-line', 'print').should('be.visible');
  });
})
