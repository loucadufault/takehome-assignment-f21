<template>
    <!-- <p>I'm a Counter!</p> -->
    <span id="counter">
      <p id="countValue">{{count}}</p>
      <button class="squareBtn" v-on:click="count--">-</button>
      <button class="squareBtn" v-on:click="count++">+</button>
    </span>
</template>

<script>
export default {
  props: {
    initialCount: {
      type: Number,
      default: 0, // keep compatibility with usage by router in /counter route
    }
  },
  data() {
    return {
      count: this.initialCount,
    };
  }
};
</script>

<style>
button.squareBtn {
  border: none;
  height: 20px;
  width: 20px;
  line-height: 20px;
}

p#countValue {
  display: inline-block;
  margin-bottom: 1px;
  margin-right: 5px;
}
</style>

