<script lang="ts">
	import { nanoid } from 'nanoid'; // Importing nanoid

	let todos = new Map<string, string>([
		[nanoid(), 'Make breakfast'],
		[nanoid(), 'Make lunch'],
		[nanoid(), 'Make dinner']
	]); // Todos database

	$: todosArr = Array.from(todos.entries()); // Declaring computed array from todos map

	let todoInput = ''; // Binded todo input value

	// OnSubmit method
	function onSubmit(e: Event) {
		e.preventDefault(); // Preventing default

		todos.set(nanoid(), todoInput); // Adding todo to todos map
		todos = todos; // Forcing rerender on component with todos map update

		todoInput = '';
	}

	function removeTodo(todoId: string) {
		todos.delete(todoId); // Deleting todo from todos map
		todos = todos; // Forcing rerender on component
	}
</script>

<div class="todo-container">
	<form on:submit={onSubmit}>
		<input type="text" bind:value={todoInput} />
		<button type="submit">Add</button>
	</form>

	<ul>
		<!-- Iterating through todosArray -->
		{#each todosArr as [id, todo]}
			<li>
				<span>{todo}</span>
				<button on:click={() => removeTodo(id)}>Remove</button>
			</li>
		{/each}
	</ul>
</div>

<style lang="scss" scoped>
	.todo-container {
		padding: 2rem;
	}
</style>
