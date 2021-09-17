<template>
  <!-- PART 4: Add your code here -->
  <div id="show">
    <h5 id="showName">{{name}}</h5>
    <span>
      <p class="counterLabel">Episodes seen: </p>
      <Counter :initial-count="episodes_seen"/>
    </span>
  </div>
</template>

<script>
// PART 4: Add your code here
import Counter from "./Counter.vue";

export default {
  props: {
    id: Number,
    name: String,
    episodes_seen: Number,
  },
  components: {
    Counter
  }
};
</script>

<style>
#showName {
  margin-bottom: 4px;
}

#show {
  margin-bottom: 16px;
}

p.counterLabel {
  display: inline-block;
  margin-right: 5px;
}
</style>
