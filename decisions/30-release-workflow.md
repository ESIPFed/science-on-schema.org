# Use Release Process Based on GitFlow

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/30

## Status ##
_Accepted_

## Decision ##

We will use a [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/)-inspired release model to track proposed changes, their implementation, and the associated Architectural Decision Record.

## Context ##
Because people will review our guidance documents online, it will be helpful to be explicit about versioning and releases of the guidance and other documents.  In particular, in GitHub, users will normally see the `master` branch, which therefore should reflect the current stable release of the documentation (rather than confusing people with in-progress proposed changes that are not yet released).

Consequently, we will use a [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/)-inspired release model in which the `master` branch always reflects the current stable release, a `develop` branch is used for merging finished proposals being prepared for release, and `feature` branches are used for creating changes to implement specific proposals that are reflected in an Architectural Decision Record.  For changes that do not require a formal decision via an ADR, such as spelling corrections, grammatical rewording, etc., maintainers can commit changes directly to the `develop` branch, and other contributors can do a pull request directly against the `develop` branch.  The use of feature branches is really focused on managing proposals that need discussion, review, and a decision through an ADR. Maintainers will make judgement calls on whether an ADR is needed, and might convert contributed pull requests to a feature branch if they determine that an ADR is needed.

The release workflow that we propose is described in detail in the `CONTRIBUTING.md` document. Some highlights:

- The `master` branch of the GitHub repository always reflects the most current release
- A `develop` branch is used for development work to extend the guidelines for each of the ADRs and for other more minor changes 
- Each ADR is associated with a pull request against the `develop` branch, and the PR should reference the issue number for the ADR in the template
    - Any PRs should be merged into the `develop` branch when they have been approved as a good implementation of the ADR
- The `develop` branch is merged into master and tagged to create a new release when it has been approved for release
- Pull requests should be based on a separate `feature` branch that is appropriately named for the feature and include the issue # that is being addressed for the feature (e.g., `feature_30_release_workflow`)
- Discussion of the proposed ADR should occur in the associated GitHub issue
- When agreement has been reached, the proposed changes and the ADR should be updated in the `feature` branch, and then merged into the `develop` branch.
- When the set of features targeted for a release are complete and review has been finished, the `develop` branch will be merged into the `master` branch and tagged as a release.
- Release tags will follow semantic versioning, and should be used to create an associated release on GitHub that allows files to be downloaded.

## Consequences ##

- People can easily follow the current stable release guidelines on the GitHub page
- The community can easily propose changes through pull requests against the development branch
- Minor changes that don't require a decision happen easily and directly on `develop`
- There are clear linkages between github issues, the ADR decision process, and the release process
- Development for core committers is somewhat more complicated as people need to understand and use the branching model, but this doesn't affect third-party contributors
- Some contributors might accidentally submit pull requests against the `master` branch, which will need to be retargeted by a maintainer against the `develop` branch before it can be merged
