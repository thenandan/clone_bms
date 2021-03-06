from orator.migrations import Migration


class CreateMovieTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('movies') as table:
            table.increments('id')
            table.string('name')
            table.text('description')
            table.integer('play_time')  # In Minutes
            table.datetime('release_date')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('movies')
