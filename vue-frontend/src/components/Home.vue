<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions complete/>
    <!-- PART 4: Modify the Show component to accept all of these props -->
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />
    <div id="addNewShowForm">
      <label id="showNameLabel" for="showName">Show name:</label>
      <input type="text" id="showName" name="showName" v-model=inputValue>
      <button type="button" @click="onAddShow(inputValue)" :disabled="inputValue.length === 0">Add a new show</button>
      <p id="errorMessage">{{errorMessage}}</p>
    </div>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  data() {
    return {
      nextInt: 0, // statefulness for id generation
      shows: [], // we create all initial shows in the created hook, by calling the initializeShows method (so that we can consistently handle the auto-incrementing ids)
      inputValue: "",
      errorMessage: "",
    };
  },
  methods: {
    onAddShow: function(showName) {
      if (!showName.length) { return; } // no-op if input value is empty

      if (this.shows.some(show => show.name === showName)) {
        this.errorMessage = "There is already a show with that name";
        return;
      }

      // add a new show to the data array
      this.shows.push({
        id: this.getNextId(), // auto-incrementing id (could also be a computed property)
        name: showName,
        episodes_seen: 0,
      });

      this.inputValue = ""; // empty the text input
      this.errorMessage = ""; // clear the previous error (if any)

      document.getElementById("addNewShowForm").scrollIntoView();
    },
    getNextId: function() {
      return ++this.nextInt;
    },
    initializeShows: function() {
      const initialShows =  [
          { name: "Game of Thrones", episodes_seen: 0 },
          { name: "Naruto", episodes_seen: 220 },
          { name: "Black Mirror", episodes_seen: 3 }
        ];

      initialShows.forEach((show) => {
        show.id = this.getNextId();
        this.shows.push(show);
      });
    },
  },
  created: function() {
    this.initializeShows();
  }
};
</script>

<style>
label#showNameLabel  {
  margin-right: 5px;
}

#errorMessage {
  color: red;
}
</style>


