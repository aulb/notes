Read along notes for:
https://pomb.us/build-your-own-react/

const element = <h1 title="foo">Hello</h1>
const element = React.createElement(
    "h1",
    { title: "foo" },
    "Hello"
)

Element, two properties: type and props.
Type: string of DOM node < DOM node... ; tagName pass to document.createElement. Can also be a function? More about it later.

props is just like args. 
Special property under props, children.
Children is a string, usually an array with more elements. This is why elements are also trees. Recursive.

React.createElement
ReactDOM.render

const element = {
    type: "h1",
    props: {
        title: "foo",
        children: "Hello",
    },
}

const node = document.createElement(element.type)
node["title"] = element.props.title // But this is tedious no?

Since we only have string as children, we create textNode # How can we determine this?
If string - textNode
If obj - new DOM Element "node" in this example.

const text = document.createTextNode("")
text["nodeValue"] = element.props.children
node.appendChild(text)

# Exercise 1
const element = (
    <div id="foo">
        <a>bar</a>
        <b />
    </div>
)

1) create div element with props id: foo
2) for each children: --> recursive
    2a) create a element, children is textNode bar
    2b) create b element, 

# Basic function
function createElement(type, props, ...children) { // ...children keeps it an array
    return {
        type,
        props: {
            ...props,
            children,
        },
    }
}

createElement("div") returns 
{
    "type": "div",
    "props": { "children": [] },
}

# Basic function that tells the difference between textNode and obj
const Didact = {
    createElement,
}

function createElement(type, props, ...children) { // ...children keeps it an array
    return {
        type,
        props: {
            ...props,
            children: children.map(child => 
                typeof child === "object"
                    ? child
                    : createTextElement(child)
            ),
        },
    }
}

/** @jsx Didact.createElement */
function createTextElement(text) {
    return {
        type: "TEXT_ELEMENT", // if type === "TEXT_ELEMENT" createTextNode
        props: {
            nodeValue: text, // already taken care of here
            children: [], // Always need this
        },
    }
}

### Render function
function render(element, container) {
    const dom = 
        element.type === "TEXT_ELEMENT"
            ? document.createTextNode("")
            : document.createElement(element.type)

    const isProperty = key => key !== "children"
    Object.keys(element.props)
        .filter(isProperty)
        .forEach(name => {
            dom[name] = element.props[name]
        })    

    // Children is empty for textNode
    element.props.children.forEach(child =>
        render(child, dom)
    )

    container.appendChild(dom)
}

### Concurrent mode, refactor
function render(element, container) {
    const dom = 
        element.type === "TEXT_ELEMENT"
            ? document.createTextNode("")
            : document.createElement(element.type)

    const isProperty = key => key !== "children"
    Object.keys(element.props)
        .filter(isProperty)
        .forEach(name => {
            dom[name] = element.props[name]
        })    

    // Children is empty for textNode
    element.props.children.forEach(child =>
        render(child, dom)
    )

    container.appendChild(dom)
}

let nextUnitOfWork = null

function workLoop(deadline) {
    let shouldYield = false
    while (nextUnitOfWork && !shouldYield) {
        nextUnitOfWork = performUnitOfWork(
            nextUnitOfWork
        )
        shouldYield = deadline.timeRemaining() < 1
    }
    requestIdleCallback(workLoop) // https://developer.mozilla.org/en-US/docs/Web/API/Window/requestIdleCallback
}

function performUnitOfWork(nextUnitOfWork) {

}

/**
PROBLEM WITH RECURSIVE RENDERING
Once we start rendering, we won’t stop until we have rendered the complete element tree. If the element tree is big, it may block the main thread for too long. And if the browser needs to do high priority stuff like handling user input or keeping an animation smooth, it will have to wait until the render finishes.
*/

# Fibers
Fiber tree
For each fiber:
 - Add element to DOM
 - Create fiber for element's children
 - Select next unit of work

Child, parent, sibling
Fiber has a link to first child.
DFS on child

function createDom(fiber) {
    const dom = 
        fiber.type === "TEXT_ELEMENT"
            ? document.createTextNode("")
            : document.createElement(fiber.type)

    const isProperty = key => key !== "children"
    Object.keys(fiber.props)
        .filter(isProperty)
        .forEach(name => {
            dom[name] = fiber.props[name]
        })    

    return dom
}

function render(element, container) {
    nextUnitOfWork = {
        dom: container, // the parent
        props: {
            children: [element],
        },
    }
}

let nextUnitOfWork = null...

function workLoop(deadline) {
    let shouldYield = false
    while (nextUnitOfWork && !shouldYield) {
        nextUnitOfWork = performUnitOfWork(
            nextUnitOfWork
        )
        shouldYield = deadline.timeRemaining() < 1>
    }
    requestIdleCallback(workloop)
}

requestIdleCallback(workLoop)

function performUnitOfWork(fiber) {
    // add dom node?
    if (!fiber.dom) {
        fiber.dom = createDom(fiber)
    }

    // Problem: adding as we go, incomplete UI 
    if (fiber.parent) {
        fiber.parent.dom.appendChild(fiber.dom)
    }

    // create new fibers
    const elements = fiber.props.children
    let index = 0
    let prevSibling = null

    while (index < elements.length) {
        const element = elements[index]

        const newFiber = {
            type: element.type,
            props: elements.props,
            parent: fiber,
            dom: null,
        }

        // Not everyone is going to have a children
        if (index === 0) {
            fiber.child = newFiber
        } else {
            prevSibling.sibling = newFiber // adding sibling to 
        }

        prevSibling = newFiber
        index++
    }

    if (fiber.child) {
        return fiber.child
    }
    let nextFiber = fiber
    while (nextFiber) {
        if (nextFiber.sibling) {
            return nextFiber.sibling
        }
        nextFiber = nextFiber.parent
    }
}

# Render and commit 
function commitRoot() { // next
    // Add nodes to dom
}

// This was changed
function render(element, container) {
    wipRoot = {
        dom: container,
        props: {
            children: [element],
        },
    }
    nextUnitOfWork = wipRoot
}

let nextUnitOfWork = null
let wipRoot = null // This one

function workLoop(deadline) {
    let shouldYield = false
    while (nextUnitOfWork && !shouldYield) {
        nextUnitOfWork = performUnitOfWork(
            nextUnitOfWork
        )
        shouldYield = deadline.timeRemaining() < 1>
    }

    if (!nextUnitOfWork && wipRoot) {
        commitRoot()
    }

    requestIdleCallback(workloop)
}

# Reconciliation 
function commitRoot() {
    commitWork(wipRoot.child)
    wipRoot = null
}

function commitWork(fiber) {
    if (!fiber) {
        return
    }
    const domParent = fiber.parent.dom
    domParent.appendChild(fiber.dom)
    commitWork(fiber.child)
    commitWork(fiber.sibling)
}

Updating and deleting nodes.