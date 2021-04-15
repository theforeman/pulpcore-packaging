# pulpcore rpm packaging

The `rpm/*` branches contain RPM spec files for individual pulpcore versions and their dependencies.

## default branch

The default branch of this repository will always point at the latest packaged pulpcore version.

## Requirements

If you're just submitting a fix, you don't need anything special.

To build locally or release RPMs from this repo, you also require:

* [obal](https://github.com/theforeman/obal) 0.0.2 or higher
* [tito](https://github.com/dgoodwin/tito) 0.6.1 or higher
* [mock](http://fedoraproject.org/wiki/Projects/Mock) or koji client and an account (certificate) on koji.katello.org

## Built repos and usage within Katello

The packages built using this repository are deployed to:

https://yum.theforeman.org/pulpcore/

These repositories are included in Katello installations using the `katello-repos` RPM package.

## License

Spec files are generally based on Fedora spec files, which means that unless a
spec file contains an explicit license attribution within it, it is available
under the MIT license.
