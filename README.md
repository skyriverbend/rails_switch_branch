# rails_switch_branch

## Usage

To use this script, you must be in the root directory of a Rails project that
is using git. You should also make sure that your directory does not contain any
uncommitted changes. Then run:

    $ python rails_switch_branch.py name_of_another_branch

Running the above will do the following:

1. Roll back any migrations on your current branch which do not exist on the
other branch
2. Discard any changes to the db/schema.rb file
3. Check out the other branch
4. Run any new migrations existing in the other branch
5. Update your test database

## TODO - pull-requests glady accepted =)
- Check if git directory is dirty. If so, do not run.
